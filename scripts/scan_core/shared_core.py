'''
This module used shared main function ZAP and variable. Before it was used, you should edit api_conf.py variable.
'''

from datetime import datetime
from . import colors
from time import sleep

from . import context, core, replacer


def get_context_id_by_name(contextname=None):
    if contextname is not None:
        return context.context(contextname)['id']
    else:
        print('Contextname field is empty!')


def go_to_urls(target=None, urls=None, followredirects=True):
    """Function for initial and building site-tree"""
    if target is not None:
        print(colors.Bcolors.CN + 'Access URL: ' + colors.Bcolors.CL + target)
        core.access_url(url=target, followredirects=followredirects)
    if urls is not None:
        for url in urls:
            core.access_url(url=url, followredirects=followredirects)


def disable_all_replacer():
    """Disable all replace rule. It should set after script."""
    for elem in replacer.rules:
        replacer.set_enabled(description=elem["description"], bool=False)
