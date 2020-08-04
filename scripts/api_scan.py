import requests
from configs import config_api_scan as config
from scan_core.shared_core import disable_all_replacer
import scan_core.setup.init_context as context
from scan_core import zap
from scan_core.jobs import scans
from scan_core.jobs.reports import report_gen
from scan_core import slack
import sys

disable_all_replacer()  # disable_all_replacer becouse if it set in "enable" proxy change the header
context_id = context.set_contex_properties(contextname=config.contextName,
                                           include_url=config.contextIncludeURL,
                                           exclude_url=config.contextExcludeURL,
                                           technology=config.contextTechnology)
context.remove_default_context()
token = requests.post(config.site + "auth", json=config.log_pass).json()[config.token_data]
# Load API from url
print(f'Remove replace rule {config.replacer_name} ==> {zap.replacer.remove_rule(config.replacer_name)}')
print(f'Add replacer rule {config.replacer_name} ==> ' + zap.replacer.add_rule(description=config.replacer_name,
                                                                               enabled=True,
                                                                               matchtype="REQ_HEADER",
                                                                               matchstring="Access-Token",
                                                                               matchregex=False,
                                                                               replacement=token))

zap.openapi.import_url(url=config.site + config.spec_path, hostoverride=config.site)

scans.set_ascan_options(tread_per_host=config.thread_per_host, host_per_scan=1)
scans.exclude_params_from_ascan(config.ascan_exclude_params)
scans.excluded_url_from_ascan(config.ascan_exclude_urls)

# Start Ascan
try:
    scans.start_ascan(context_name=config.contextName, scan_policy=config.scanPolicyName)
except ValueError:
    print("Scan_id does not exist. Proxy is empty.")
    slack.post_message_to_slack("ERROR! Proxy is empty!")
    sys.exit()
except Exception as e:
    print("Error:", e)
    slack.post_message_to_slack("Error: " + str(e))
    sys.exit()

# Reports cooking
else:
    html_report = report_gen()
    slack.upload_file(file=html_report)
