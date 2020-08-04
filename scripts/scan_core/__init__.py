from scan_core import api_conf
from zapv2 import ZAPv2
from redminelib import Redmine
from slack import Slack


def init_zap_api(local_proxy=api_conf.zapProxy, api_key=api_conf.zap_key):
    return ZAPv2(proxies=local_proxy, apikey=api_key)


def init_redmine_api(url=api_conf.redmine_url, version=api_conf.redmine_version, api_key=api_conf.redmine_key):
    return Redmine(url, version=version, key=api_key)


# ZAP variables
zap = init_zap_api()
core = zap.core
ascan = zap.ascan
forcedUser = zap.forcedUser
spider = zap.spider
ajax = zap.ajaxSpider
script = zap.script
context = zap.context
auth = zap.authentication
users = zap.users
sessionManagement = zap.sessionManagement
replacer = zap.replacer

# Redmine variables
redmine = init_redmine_api()

# Slack variable
slack = Slack(webhook=api_conf.slack_hook, token=api_conf.slack_token,
           channel_id=api_conf.slack_channel_id, channel=api_conf.slack_channel,
           slack_url=api_conf.slack_url)
