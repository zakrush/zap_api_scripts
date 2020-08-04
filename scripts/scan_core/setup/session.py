from scan_core import core, colors



def new_session(session_name="Untitled_Session"):
    print(colors.Bcolors.CN + 'Create ZAP session: ' + session_name + ' -> ' +
           colors.Bcolors.CL + core.new_session(name=session_name, overwrite=True))


def load_session(session_name="Untitled_Session"):
    print(colors.Bcolors.CN + 'Load ZAP session: ' + session_name + ' -> ' +
           + colors.Bcolors.CL + core.load_session(name=session_name))


def add_global_exclude_urls(global_exclude_url):
    """globalExcludeUrls MUST to be LIST TYPE"""
    print(colors.Bcolors.CN + 'Add Global Exclude URLs regular expressions:')
    [print(regex + '->' + core.exclude_from_proxy(regex=regex)) for regex in global_exclude_url]
