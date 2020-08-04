contextName = 'Api-scan'
contextIncludeURL = ['^http[s]?:\/\/api\.example\.com.*']
contextExcludeURL = ['^http[s]?:\/\/.*example\.com\/auth$']

# full list Technology
contextTechnologyAll = ['Db', 'Db.CouchDB', 'Db.Firebird', 'Db.HypersonicSQL', 'Db.IBM DB2', 'Db.Microsoft Access',
                        'Db.Microsoft SQL Server', 'Db.MongoDB', 'Db.MySQL', 'Db.Oracle', 'Db.PostgreSQL',
                        'Db.SAP MaxDB', 'Db.SQLite', 'Db.Sybase',
                        'Language', 'Language.ASP', 'Language.C', 'Language.JSP/Servlet', 'Language.Java',
                        'Language.JavaScript', 'Language.PHP', 'Language.Python', 'Language.Ruby', 'Language.XML',
                        'OS', 'OS.Linux', 'OS.MacOS', 'OS.Windows',
                        'SCM', 'SCM.Git', 'SCM.SVN',
                        'WS', 'WS.Apache', 'WS.IIS', 'WS.Tomcat']

# Technology list that was included into context
contextTechnology = ['Db', 'Db.MySQL', 'Language', 'Language.Java', 'Language.JavaScript', 'Language.PHP',
                     'Language.XML',
                     'OS', 'OS.Linux', 'SCM', 'SCM.Git',
                     'WS', 'WS.Tomcat']

#Spider configs

spider_maxchildren = '20'


# Set a policy name that was created
scanPolicyName = 'API_minimal'


# ascan_exclude_params. Format is [parameter_name, type, url].
# all numbers of types you can get throught ascan.excludedParamTypes
ascan_exclude_params = [['Access-Token', '8'],
                        ['access_token', '4'],
                        ['login', '37', contextIncludeURL[0][:-2] + '\/auth$'],
                        ['password', '37', contextIncludeURL[0][:-2] + '\/auth$']]

ascan_exclude_urls = [contextIncludeURL[0][:-2] + '\/auth$']

thread_per_host = 5

log_pass = {"login": "user@example.com", "password": "password"}

site = "https://api.example.com/"
spec_path = "specification"
token_data = "access_token"
#create replacer. It variable define is description
replacer_name = "Add access token header"
