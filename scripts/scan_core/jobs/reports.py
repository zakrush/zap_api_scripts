from datetime import datetime
from scan_core import core, colors, redmine
from configs import reports_config as config
from io import BytesIO
import os


def check_type_scan(type_of_scan):
    try:
        return True, config.scan_types[type_of_scan]
    except KeyError:
        return False, 'Incorrect set type of scan into function. ' \
                      'Please set type_of_scan value as ' + \
               ' or '.join([key for key in list(config.scan_types.keys())])


def report_gen(type_file='html'):
    if not (type_file == 'html' or type_file == 'xml' or type_file == 'json'):
        print('Incorrect type field. Function report_get support only html, xml or json')
    else:
        current_data = datetime.now()
        dir_name = os.path.abspath('../reports')
        filename = f'{dir_name}/{current_data.strftime("%Y-%m-%d")}.{type_file}'
        with open(filename, 'w') as f:
            if type_file == 'html':
                f.write(core.htmlreport())
            elif type_file == 'xml':
                f.write(core.xmlreport())
            else:
                f.write(core.jsonreport())
        print(colors.Bcolors.G + 'Report is complited')
        return filename


###############################
# REDMINE
###############################

def find_issue_into_project(type_of_scan="Full"):
    check, text = check_type_scan(type_of_scan)
    if check:
        project = redmine.project.get(config.project_name)

        for item in project.issues:
            if item.subject == text:
                return item
            else:
                return None
    else:
        print(colors.Bcolors.R + text)


def check_issue(type_of_scan='Full'):
    if find_issue_into_project(type_of_scan=type_of_scan) is None:
        return False
    else:
        return True


def create_issue(type_of_scan='Full', add_zap_report=False):
    """See https://python-redmine.com/resources/issue.html#create
    Generate only html_report"""
    check, text = check_type_scan(type_of_scan)
    if check:
        try:
            category_id = config.category_id
        except AttributeError:
            category_id = None
        try:
            description = config.description_of_issue
        except AttributeError:
            description = None
        if type(add_zap_report) == bool:
            if not add_zap_report:
                issue = redmine.issue.create(
                    project_id=config.project_name,
                    subject=config.scan_types[type_of_scan],
                    description=description,
                    category_id=category_id
                )
                print(colors.Bcolors.G + "Issue was created")
                return issue
            else:
                filename = "report-" + datetime.now().strftime("%Y-%m-%d") + '.html'
                issue = redmine.issue.create(
                    project_id=config.project_name,
                    subject=config.scan_types[type_of_scan],
                    description=description,
                    category_id=category_id,
                    uploads=[{'path': BytesIO(core.htmlreport().encode('utf-8')),
                              'filename': filename, 'content_type': 'text/html'}]
                )
                print(colors.Bcolors.G + "Issue was created with report file")
                return issue
        else:
            print(colors.Bcolors.R + "Invalid add_zap_report")
    else:
        print(colors.Bcolors.R + text)


def add_redmine_issue_notes(type_of_scan='Full'):
    """Report generated into issue_notes by zap.core.report
    https://python-redmine.com/resources/issue.html#journals"""
    check, text = check_type_scan(type_of_scan)
    if check:
        if not check_issue(type_of_scan=type_of_scan):
            create_issue(type_of_scan=type_of_scan, add_zap_report=True)

        else:
            filename = "report-" + datetime.now().strftime("%Y-%m-%d") + '.html'
            issue_id = find_issue_into_project(type_of_scan=type_of_scan).id
            result = redmine.issue.update(issue_id,
                                          notes="Report was added.\n *_Type of report:_ " + type_of_scan.title() +
                                                'scan*',
                                          upload=[
                                              {'path': BytesIO(core.htmlreport().encode('utf-8')),
                                               'filename': filename, 'content_type': 'text/html'}])
            if result:
                print(colors.Bcolors.G + "Report was saccessful upload to redmine.")
            else:
                print(colors.Bcolors.R + 'Something WRONG while load report to REDMINE')
    else:
        print(colors.Bcolors + text)


####################################
#   Slack
#####################################
