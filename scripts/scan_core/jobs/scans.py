"""Here functions for active, passive scans"""

from time import sleep
from scan_core import ascan, colors
from scan_core.shared_core import get_context_id_by_name


##############################################################################################################
#
#                                   CONFIG
############################################################################################################


def set_ascan_options(tread_per_host=40, host_per_scan=2, max_results_to_list=1000,
                      max_rule_duration=0, max_scan_duration=0, delay_when_scanning=0,
                      inject_in_header=False):
    """Config ascan that sets into Options -> Active scan.
    More is here https://www.zaproxy.org/docs/desktop/ui/dialogs/options/ascan/"""

    # Configs thred_per_host
    if 0 < int(tread_per_host) <= 50:
        ascan.set_option_thread_per_host(int(tread_per_host))
    else:
        print(colors.Bcolors.R + "Incorrect thread_per_host value. thread_per_host value set is 40")
        ascan.set_option_thread_per_host(40)

    # Config host_per_scan
    if 0 < int(host_per_scan) <= 5:
        ascan.set_option_host_per_scan(int(host_per_scan))
    else:
        print(colors.Bcolors.R + "Incorrect host_per_scan value. host_per_scan value set is 2")

    # Config max_results_to_list
    if type(max_results_to_list) == int and max_results_to_list > 0:
        ascan.set_option_max_results_to_list(max_results_to_list)
    else:
        print(colors.Bcolors.R + "Incorrect max_resuls_to_list value. max_results_to_list value set is 1000")
        ascan.set_option_max_results_to_list(1000)

    # Config max_rule_duration
    if type(max_rule_duration) == int and max_rule_duration >= 0:
        ascan.set_option_max_rule_duration_in_mins(max_rule_duration)
    else:
        print(colors.Bcolors.R + "Incorrect max_rule_duration value. max_rule_duration value set is 0(unlimited)")
        ascan.set_option_max_rule_duration_in_mins(0)

    # Config max_scan_duration
    if type(max_scan_duration) == int and max_scan_duration >= 0:
        ascan.set_option_max_scan_duration_in_mins(max_scan_duration)
    else:
        print(colors.Bcolors.R + "Incorrect max_scan_duration value. max_scan_duration value set is 0(unlimited)")
        ascan.set_option_max_scan_duration_in_mins(0)

    # Config delay into msec
    if type(delay_when_scanning) == int and delay_when_scanning >= 0:
        ascan.set_option_delay_in_ms(delay_when_scanning)
    else:
        print(
            colors.Bcolors.R + "Incorrect delay_when_scan_scanning value. delay_when_scan_scanning value set is 0(unlimited)")
        ascan.set_option_delay_in_ms(0)

    # Config inject_into_header
    # If this option is selected the active scanner will inject the request header X-ZAP-Scan-ID
    # with the ID of the scanner that's sending the HTTP requests.
    if type(inject_in_header) == bool:
        ascan.set_option_inject_plugin_id_in_header(inject_in_header)
    else:
        print("Incorrect inject_in_header value. Please, set inject_in_header value is bool type")

    print(colors.Bcolors.G + "Ascan options was successfully set")
def remove_exclude_params_from_ascan(param):

    '''Remove params from ascan. Uses into exclude_params_ascan function'''
    [ascan.remove_excluded_param(elem['idx']) for elem in ascan.excluded_params if elem['parameter'] == param]

def exclude_params_from_ascan(params):
    """ Get list with list into. [[parameter_name, type, url]] if url empty, use *"""
    try:
        for elem in params:

            if len(elem) == 3 and type(elem[0]) == str and type(elem[1]) == str and type(elem[2]) == str:
                remove_exclude_params_from_ascan(elem[0])
                ascan.add_excluded_param(name=elem[0], type=elem[1], url=elem[2])
            elif len(elem) == 2 and type(elem[0]) == str and type(elem[1]) == str:
                remove_exclude_params_from_ascan(elem[0])
                ascan.add_excluded_param(name=elem[0], type=elem[1])
            else:
                print(colors.Bcolors.R + "Incorrect value type or lengs of exclude_params_from_ascan func")
    except TypeError:
        print(colors.Bcolors.R + "Incorrect params variable type or format.")
    except IndexError:
        print(colors.Bcolors.R + 'Incorrect elements of params, it should be list')
    else:
        print(colors.Bcolors.G + "Exclude params for ascan was set.")

def scan_input_vector(exclude_params=None, add_url_query_params=False, http_header_scan=False):
    """Define scan input vector of advanced options active scan. Functionality not full"""
    if exclude_params is not None:
        exclude_params_from_ascan(exclude_params)
    ascan.set_option_scan_headers_all_requests(http_header_scan)
    ascan.set_option_add_query_param(add_url_query_params)

def excluded_url_from_ascan(urls):
    """Urls must be list type"""
    ascan.clear_excluded_from_scan() #clear previous configs
    try:
        [ascan.exclude_from_scan(url) for url in urls]
    except TypeError:
        print(colors.Bcolors.R + "Incorrect parameter urls type in excluded_url_from_ascan function")
    else:
        print(colors.Bcolors.G + "Urls was successfuly added to ascan exclude params")

################################################################################################################
#
#                   SCAN
################################################################################################################
def start_ascan(context_name='Default Context', user_id=None, scan_policy=None, postdata=True, recurse=None):
    print('\n' + colors.Bcolors.CN + "Active Scan with Context " + context_name)

    if user_id is not None:
        print('start Active scan with UserId ' + user_id)
        scan_id = ascan.scan_as_user(contextid=get_context_id_by_name(context_name), userid=user_id, postdata=postdata,
                                     scanpolicyname=scan_policy, recurse=recurse)
        sleep(2)
        while int(ascan.status(scan_id)) < 100:
            print('\r', colors.Bcolors.CN + 'Active Scan progress: ' + ascan.status(scan_id) + '%', end='')
            sleep(2)
    else:
        scan_id = ascan.scan(contextid=get_context_id_by_name(context_name), postdata=postdata,
                             scanpolicyname=scan_policy, recurse=recurse, method=None)
        sleep(2)
        while int(ascan.status(scan_id)) < 100:
            print('\r', colors.Bcolors.CN + 'Active Scan progress: ' + ascan.status(scan_id) + '%', end='')
            sleep(2)
    sleep(5)  # Get chanse active scan to be comlited
    print('\nActive Scan for Context ' + context_name + ' completed')



