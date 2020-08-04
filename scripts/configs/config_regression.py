contextName = 'regression-test'
contextIncludeURL = ['^http[s]?:\/\/regression-test-qa[1-9].*\.example\.com.*']
contextExcludeURL = ['^http[s]?:\/\/.*example\.com\/site\/log(in|out)$']

# full list Technology
contextTechnologyAll = ['Db', 'Db.CouchDB', 'Db.Firebird', 'Db.HypersonicSQL', 'Db.IBM DB2', 'Db.Microsoft Access',
                        'Db.Microsoft SQL Server', 'Db.MongoDB', 'Db.MySQL', 'Db.Oracle', 'Db.PostgreSQL',
                        'Db.SAP MaxDB', 'Db.SQLite', 'Db.Sybase',
                        'Language', 'Language.ASP', 'Language.C', 'Language.JSP/Servlet', 'Language.Java',
                        'Language.JavaScript', 'Language.PHP', 'Language.Python', 'Language.Ruby', 'Language.XML',
                        'OS', 'OS.Linux', 'OS.MacOS', 'OS.Windows',
                        'SCM', 'SCM.Git', 'SCM.SVN',
                        'WS', 'WS.Apache', 'WS.IIS', 'WS.Tomcat']

# Technology list that will include into context
contextTechnology = ['Db', 'Db.MySQL', 'Language', 'Language.Java', 'Language.JavaScript', 'Language.PHP',
                     'Language.XML',
                     'OS', 'OS.Linux', 'SCM', 'SCM.Git',
                     'WS', 'WS.Tomcat']

# Authentication
logged_out_indicator = '\QPlease input login and password\E'
login_page_url = 'https://regression-test-qa.example.com/site/login'
login_url = 'https://regression-test-qa.example.com/api/auth'
auth_params = 'loginUrl=https://regression-test-qa.example.com/api/auth&loginPageUrl=https://regression-test-qa.example.com/site/login&' \
              'loginRequestData={"login": "{%login%}", "password": "{%password%}"}'
#auth_params = ('loginUrl=https://regression-test-qa.example.com/api/auth')
               #'loginPageUrl=https://regression-test-qa.example.com/site/login'
               #'loginRequestData={"login": "{%login%}", "password": "{%password%}"}')

#Spider configs

spider_maxchildren = '20'

# Define the session management method for the context. Possible values are:
# "cookieBasedSessionManagement"; "httpAuthSessionManagement"
sessionManagement = 'cookieBasedSessionManagement'

# Set a policy name that was created
scanPolicyName = 'Custom_regression_policy'
"policy for import shold saved to policy folder"
ImportedPolicyName = "regression-fast"

# In the example bellow, the first line corresponds to SQL Injection scan IDs,
# the second line corresponds to some XSS scan IDs
# Use zap.ascan.scanners() to list all ascan IDs.
ascanIds = [40018, 40019, 40020, 40021, 40022, 40024, 90018,
            40012, 40014, 40016, 40017]

# ascan_exclude_params. Format is [parameter_name, type, url].
# all numbers of types you can get throught ascan.excludedParamTypes
ascan_exclude_params = [['Access-Token', '8'],
                        ['access_token', '4'],
                        ['login', '37', contextIncludeURL[0][:-2] + '\/api\/auth$'],
                        ['password', '37', contextIncludeURL[0][:-2] + '\/api\/auth$']]

ascan_exclude_urls = [contextIncludeURL[0][:-2] + '\/api\/auth$']

thread_per_host = 10
alertThreshold = 'Medium'
attackStrength = 'Medium'
