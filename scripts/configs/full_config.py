'''
Here all config variables that can be
'''

sessionName = 'Untitled Session'

# Define the list of global exclude URL regular expressions. List can be empty.
# The expressions must follow the java.util.regex.Pattern class syntax
# The following example excludes every single URL except http://localhost:8081
globalExcludeUrl = ['^(?:(?!http:\/\/localhost:8081).*).$']

#################
# PROXY CONFIGS #
#################

proxyAddress = 'my.corp.proxy'
proxyPort = '8080'
# Define the addresses to skip in case useProxyChain is True. Ignored
# otherwise. List can be empty.
skipProxyAddresses = ('127.0.0.1;'
                      'localhost')

# For Proxy auth
proxyUsername = ''
proxyPassword = ''
proxyRealm = ''

#For proxy auth script
proxyScriptName = 'proxyScript.js'
# Script engine values: "Oracle Nashorn" for Javascript,
# "jython" for python, "JSR 223 JRuby Engine" for ruby
proxyScriptEngine = 'Oracle Nashorn'
# Absolute local path into DOCKER container
proxyScriptFileName = '/zap/scripts/proxy/proxyScript.js'
proxyScriptDescription = 'This is a description'

###################
# CONTEXT CONFIGS #
###################

contextName = 'regression-test'
# MANDATORY only if defineNewContext is False. Disregarded otherwise.
# Corresponds to the ID of the context to use

# Define Context Include URL regular expressions. You have to put the URL you want to test in this list.
contextIncludeURL = ['^http[s]?:\/\/.*example\.com.*']
# Define Context Exclude URL regular expressions.
contextExcludeURL = ['^http[s]?:\/\/.*example\.com\/\site\/log(in|out)$']

#Here full technology list. It's is for save format of technology

contextTechnologyAll = ['Db', 'Db.CouchDB', 'Db.Firebird', 'Db.HypersonicSQL', 'Db.IBM DB2', 'Db.Microsoft Access',
                     'Db.Microsoft SQL Server', 'Db.MongoDB', 'Db.MySQL', 'Db.Oracle', 'Db.PostgreSQL',
                     'Db.SAP MaxDB', 'Db.SQLite', 'Db.Sybase',
                     'Language', 'Language.ASP', 'Language.C', 'Language.JSP/Servlet', 'Language.Java',
                     'Language.JavaScript', 'Language.PHP', 'Language.Python', 'Language.Ruby', 'Language.XML',
                     'OS', 'OS.Linux', 'OS.MacOS', 'OS.Windows',
                     'SCM', 'SCM.Git', 'SCM.SVN',
                     'WS', 'WS.Apache', 'WS.IIS', 'WS.Tomcat']

contextTechnology = ['Db', 'Db.MySQL', 'Language', 'Language.Java', 'Language.JavaScript', 'Language.PHP', 'Language.XML',
                     'OS', 'OS.Linux', 'SCM', 'SCM.Git',
                     'WS', 'WS.Tomcat']


# Define the session management method for the context. Possible values are:
# "cookieBasedSessionManagement"; "httpAuthSessionManagement"
# "cookieBasedSessionManagement" set by default
sessionManagement = 'cookieBasedSessionManagement'


###############
# AUTH MODULE #
###############


# Define authentication method for the context. Possible values are:
# "manualAuthentication"; "scriptBasedAuthentication"; "httpAuthentication";
# "formBasedAuthentication"
authMethod = 'manualAuthentication'


# Script auth
authScriptName = 'TwoStepAuthentication.js'
# Script engine values: Oracle Nashorn for Javascript
# jython for python, JSR 223 JRuby Engine for ruby, zest
authScriptEngine = 'Oracle Nashorn'
# Absolute local path into DOCKER container
authScriptFileName = '/zap/scripts/authentication/TwoStepAuthentication.js'
authScriptDescription = 'This is a description'

# Each name/value pair of authParams are expected to be "x-www-form-urlencoded"
# Here is an example for scriptBasedAuthentication method:
authParams = ('scriptName=' + authScriptName + '&'
                                               'Submission Form URL=http://localhost:8081/WebGoat/j_spring_security_check&'
                                               'Username field=username&'
                                               'Password field=password&'
                                               'Target URL=http://localhost:8081/WebGoat/welcome.mvc')
## Here is an example for formBasedAuthentication method:
authParams = ('loginUrl=http://localhost:8081/WebGoat/j_spring_security_check&'
              'loginRequestData=username%3D%7B%25username%25%7D%26'
              'password%3D%7B%25password%25%7D')
##Here is an example for httpAuthentication method:
# authParams = ('hostname=http://www.example.com&'
#              'realm=CORP\\administrator&'
#              'port=80')


# Define either a loggedin or a loggedout indicator regular expression.
# It allows ZAP to see if the user is always authenticated during scans.
indicatorRegex = '\QLocation: http://localhost:8081/WebGoat/login.mvc\E'


#Define the list of users, with name and credentials (in x-www-form-urlencoded format)
## Here is an example with the script NashornTwoStepAuthentication.js:
userList = [
    {'name': 'guest', 'credentials': 'Username=guest&Password=guest'},
    {'name': 'webgoat', 'credentials': 'Username=webgoat&Password=webgoat'}
]
## Here is an example with formBasedAuthentication:
# userList = [
#    {'name': 'guest', 'credentials': 'username=guest&password=guest'},
#    {'name': 'webgoat', 'credentials': 'username=webgoat&password=webgoat'}
# ]

# MANDATORY only if useContextForScan is True. Ignored otherwise. List can be
# empty. Define the userid list. Created users will be added to this list later

###########################################################################
#                                                                         #
#                               SCAN MODULE                               #
#                                                                         #
###########################################################################

# Define the target site to test
target = 'https://regression-test-qa.example.com'

# You can specify other URL in order to help ZAP discover more site locations
# List can be empty
applicationURL = []

############
# POLICY   #
############
#Set a policy name
scanPolicyName = 'Custom_regression_policy'


# Use zap.ascan.scanners() to list all ascan IDs.
## In the example bellow, the first line corresponds to SQL Injection scan IDs,
## the second line corresponds to some XSS scan IDs
ascanIds = [40018, 40019, 40020, 40021, 40022, 40024, 90018,
            40012, 40014, 40016, 40017]

# Set the alert Threshold and the attack strength of enabled active scans.
# Currently, possible values are:
# Low, Medium and High for alert Threshold
# Low, Medium, High and Insane for attack strength
alertThreshold = 'Medium'
attackStrength = 'Low'


#directoryName for save of reports
home_directory = '/home/dmitriy/.ZAP/reports/'

