"""
Here config for connect to zap and Start ZAP
"""
#######################################################
# ZAP API
#######################################################
# MANDATORY. Define the API key generated by ZAP and used to verify actions.
zap_key = '1111111111111111111'

# MANDATORY. Define the listening address of ZAP instance
zapProxy = {"http": "127.0.0.1:8090", "https": "127.0.0.1:8090"}

# Folder was mounted and use for import into DockerZAP
import_folder = "/home/zap/.ZAP/policies.external"

#######################################################
# Redmine API
#######################################################
redmine_key = '1111111111111111111111111111'
redmine_url = 'https://redmine.example.com'
redmine_version = '2.2.2'

#######################################################
# DefectDojo API
#######################################################
dd_host = 'https://defectdojo.example.com'
dd_key = 'fsdafp231lfafm12'
dd_user = 'autotest'
