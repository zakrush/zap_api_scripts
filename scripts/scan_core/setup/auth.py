from scan_core import script, colors, users, auth


def set_script_based_auth(scriptname=None, engine=None, filename=None, description=None):
    """In case we use the scriptBasedAuthentication method, load the script.
    Filename - is directory where saved the policy into system where run ZAP(docker or other).
    Before run this you should load script file into system thought scp or docker cp command"""
    if scriptname and engine and filename is not None:
        print(colors.Bcolors.CN + "LOAD Auth script" + scriptname)
        print(colors.Bcolors.Y + "Load is: " + colors.Bcolors.CL + script.load(scriptname=scriptname,
                                                                               scripttype='authentication',
                                                                               scriptengine=engine,
                                                                               filename=filename,
                                                                               scriptdescription=description))
    else:
        print(colors.Bcolors.R + "scriptname, engine or filename is empty")


def set_json_based_auth(auth_params, context_id=None):
    # {"methodConfigParams":[{"name":"loginUrl",
    #                               "mandatory":"true"},
    #                               {"name":"loginRequestData",
    #                               "mandatory":"true"},
    #                               {"name":"loginPageUrl",
    #                               "mandatory":"false"}]}

    # {"method": {"loginUrl": "https://regression-test-qa1.timebook.ru/idealApi/auth",
    #            "methodName": "jsonBasedAuthentication",
    #            "loginPageUrl": "https://regression-test-qa1.timebook.ru/?r=site/login",
    #            "loginRequestData": {"login": "{%password%}", "password": "QWRe@323wdsa"}}}

    return auth.set_authentication_method(contextid=context_id, authmethodname='jsonBasedAuthentication',
                                          authmethodconfigparams=auth_params)


def create_user(users=None, contextname='Default Context'):
    """Create users from users_list for Current Context Name.
     If Context name don't set use Default Context"""
    print(colors.Bcolors.CN + "Create users")
    if users is not None:
        user_list = users
        user_id_list = list()
        context_id = get_context_id_by_name(contextname=contextname)

        for user in user_list:
            user_name = user.get('name')
            user_id = users.new_user(contextid=context_id, name=user_name)
            user_id_list.append(user_id)
            print(colors.Bcolors.Y + 'Create user:', user + ' ID ' + user_id, end=' ')
            users.set_user_name(contextid=context_id, userid=user_id, name=user_name)
            users.set_authentication_credentials(contextid=context_id, userid=user_id,
                                                 authcredentialsconfigparams=user.get('credentials'))
            print("enabled -> " + users.set_user_enabled(contextid=context_id, userid=user_id, enabled=True))
            return user_id_list
    else:
        print(colors.Bcolors.R + 'users field is empty.')
