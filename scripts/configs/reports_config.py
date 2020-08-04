# Here config of reports

####################
# Redmine
####################
project_name = 'Reports_of_scans'

# here types of scans. By type of scan get issue name into redmine functions.
# If you want rename issue. Change values of type scan.
scan_types = {'Full': 'Weekly_OWASP_ZAP(Full_scan)',
              'Regression': 'Daily_OWASP_ZAP(Regression)',
              'API': 'API scan'}

# Set category ID for issue. If you don't have category ID, please, set it None value
category_id = 111
description_of_issue = "*Reports of owasp ZAP*"

####################
# slack
####################
slack_channel = '#sec_channel'
slack_channel_id = 'AA01GG02DD'  # find it into browser string
slack_user_name = "SecRobot"
slack_hook = 'https://hooks.slack.com/services/T11AAAT1/A1A1ABCDEF/Aa111123ldssaASd'
slack_token = 'xoxb-111111112-2222222222-adfsfFA23ASdfafAS'
slack_url = 'https://mycorp.slack.com'

#################################################
# Defect Dojo conf (product, engagement)
#################################################

dd_name_of_product = 'MyProduct'
dd_name_of_engagement = "DASTs"
dd_scan_type = "ZAP Scan"
dd_scan_tag = "ZAP-daily"
