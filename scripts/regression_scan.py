import configs.config_regression as conf
from scan_core import slack
from configs import reports_config as r_conf
import scan_core.setup.init_context as context_init
from scan_core.setup.policy import import_scan_policy
import scan_core.jobs.scans as scans
from scan_core.jobs.reports import report_gen, add_redmine_issue_notes
from scan_core.jobs.spiders import spider_scan
import sys
import scan_core.setup.session as set_session
import argparse
from defectdojo import DefectDojoTB
import datetime

parser = argparse.ArgumentParser(description="ZAP API for regression test",
                                 usage='Use optional arguments for setting of scanning. If all argsuments is empty, '
                                       'script init CONTEXT, doing ActiveScan and send report to slack')

parser.add_argument('-ns', '--new_session', action='store_true',
                    help="Initilize new session, and do excluded. WARN: all data collection will be clear."
                         "Don't use this argument with other arguments")
parser.add_argument('-s', '--spider', action='store_true',
                    help="Use spider for scanning")
parser.add_argument('-sd', '--slack_disable', action='store_false',
                    help="Send report to slack")
parser.add_argument('-rm', '--redmine', action='store_true',
                    help="Send report to redmine")
parser.add_argument('-dd', '--dojo', action='store_false',
                    help="Send report to DefectDojo")
args = parser.parse_args()


if args.new_session:
    set_session.new_session()

else:
    context_id = context_init.set_contex_properties(contextname=conf.contextName,
                                                    include_url=conf.contextIncludeURL,
                                                    exclude_url=conf.contextExcludeURL,
                                                    technology=conf.contextTechnology)
    # Remove "Default context" for exclude all scans not in scope.
    context_init.remove_default_context()
    policy_name = import_scan_policy(policy_name=conf.ImportedPolicyName)
    print(f"{policy_name} was applied for ascan")

    if args.spider:
        spider_scan(context_name=conf.contextName, maxchildren=conf.spider_maxchildren, ajax_scan=False)

    # Config Ascan
    scans.set_ascan_options(tread_per_host=conf.thread_per_host)
    scans.exclude_params_from_ascan(conf.ascan_exclude_params)
    scans.excluded_url_from_ascan(conf.ascan_exclude_urls)

    # Start Ascan
    try:
        print(f"Start ASCAN with Context {conf.contextName} and policy {policy_name}")
        scans.start_ascan(context_name=conf.contextName, scan_policy=policy_name)
    except ValueError:
        print("Scan_id does not exist. Proxy is empty.")
        slack.post_message_to_slack("ERROR! Proxy is empty!")
        sys.exit()
    except Exception as e:
        print("Error:", e)
        slack.post_message_to_slack("Error: " + str(e))
        sys.exit()

    # Gen html-report

    html_report = report_gen()

    if args.slack_disable:
        slack.upload_file(file=html_report)

    # Send report to redmine
    if args.redmine:
        add_redmine_issue_notes(type_of_scan='Regression')

    # Send results to DefectDojo
    if args.dojo:
        xml_report = report_gen(type_file='xml')
        dd = DefectDojoTB(product_name=r_conf.dd_name_of_product, engagement_name=r_conf.dd_name_of_engagement)

        print('Upload report to DefectDojo:', dd.import_tb_scan(scan_type=r_conf.dd_scan_type,
                                                                file=xml_report,
                                                                scan_date=datetime.datetime.now().strftime('%Y-%m-%d'),
                                                                tags=r_conf.dd_scan_tag))
