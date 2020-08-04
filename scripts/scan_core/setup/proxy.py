from scan_core import core, colors, script


def set_proxy_chain(proxy_address = None, proxy_port = None, skip_proxy_addresses = None):
    if proxy_address and proxy_address is not None:
        print(colors.Bcolors.CN + 'Enable outgoing proxy chain: ' + colors.Bcolors.CL
               + core.set_option_use_proxy_chain(boolean=True))
        print(colors.Bcolors.Y + 'Set outgoing proxy name: ' + colors.Bcolors.CL + proxy_address + ' -> ' +
               core.set_option_proxy_chain_name(string=proxy_address))
        print(colors.Bcolors.Y + 'Set outgoing proxy port: ' + colors.Bcolors.CL + proxy_port + ' -> ' +
               core.set_option_proxy_chain_port(integer=proxy_port))
    else:
        print(colors.Bcolors.R + "proxy_adress or/and proxy_port is empty!")
    if skip_proxy_addresses is not None:
        print(colors.Bcolors.Y + 'Skip names for outgoing proxy: ' + colors.Bcolors.CL + skip_proxy_addresses + ' -> ' +
               core.set_option_proxy_chain_skip_name(string=skip_proxy_addresses))


def set_proxy_auth(username=None, password=None, proxy_realm=None):
    if username and password is not None:
        print(colors.Bcolors.CN + 'Set outgoing proxy chain authentication: ' + colors.Bcolors.CL +
               core.set_option_use_proxy_chain_auth(boolean=True))
        print(colors.Bcolors.Y + 'Set outgoing proxy username -> ' + colors.Bcolors.CL +
               core.set_option_proxy_chain_user_name(string=username))
        print(colors.Bcolors.Y + 'Set outgoing proxy password -> ' + colors.Bcolors.CL +
               core.set_option_proxy_chain_password(string=password))
    else:
        print(colors.Bcolors.R + 'username and/or password is empty!')
    if proxy_realm is not None:
        print('Set outgoing proxy realm: ' + proxy_realm + ' -> ' +
               core.set_option_proxy_chain_realm(string=proxy_realm))


def set_proxy_script(scriptname=None, engine=None, filename=None, description=None):
    if scriptname and engine and filename is not None:
        print(colors.Bcolors.CN + 'Load and enable Proxy Script')
        script.remove(scriptname=scriptname)
        print(colors.Bcolors.Y + 'Load proxy script' + name + ': ' + colors.Bcolors.CL +
               script.load(scriptname=scriptname, scripttype='proxy', scriptengine=engine,
                           filename=filename, scriptdescription=description))
        print(colors.Bcolors.Y + 'Enable proxy script ' + colors.Bcolors.B + name +
               colors.Bcolors.CL + script.enable(scriptname=scriptname))
    else:
        print(colors.Bcolors.R + 'scriptname or/and engine or/and filename is empty')