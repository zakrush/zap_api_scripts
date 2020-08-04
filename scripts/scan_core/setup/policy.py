from scan_core import colors, ascan
from scan_core.api_conf import import_folder


def import_scan_policy(policy_name=None):
    """Import ascan policy. Import from internal folder of ZAP Docker. Thsi folder is mapping from git repo.
     If policy_name is not set, create 'Medium default policy'."""
    default_policy_name = "Medium default policy"

    if policy_name is not None:
        if policy_name.find(".policy") == -1:
            policy_name_full = policy_name + ".policy"
        else:
            policy_name_full = policy_name

        absolute_path = f"{import_folder}/{policy_name_full}"
        print(absolute_path)
        import_answ = ascan.import_scan_policy(absolute_path)
        if import_answ == "OK" or import_answ == "already_exists":
            print(f'{absolute_path} was loaded')
            return policy_name
        else:
            print(f"ERROR OF IMPORT policy {policy_name}: {import_answ}")
            create_scan_policy(policy_name=default_policy_name)
            return default_policy_name
    else:
        create_scan_policy(policy_name=default_policy_name)
        return default_policy_name


def create_scan_policy(policy_name=None, strenghth='Medium', alert_threshold='Medium'):
    """Create Policy and set for all ids one level of strenghth and alert_threshold.
    strenghth and alert_threshold  is Medium by default """
    if policy_name is not None:
        ascan.remove_scan_policy(scanpolicyname=policy_name)
        print(colors.Bcolors.CN + " ADD scan policy:" + colors.Bcolors.CL + ' ' + policy_name +
              ' -> ' + ascan.add_scan_policy(scanpolicyname=policy_name))
        for policy_id in range(0, 5):
            # Set alert Threshold for all scans
            ascan.set_policy_alert_threshold(id=policy_id,
                                             alertthreshold=alert_threshold,
                                             scanpolicyname=policy_name)
            # Set attack strength for all scans
            ascan.set_policy_attack_strength(id=policy_id,
                                             attackstrength=strenghth,
                                             scanpolicyname=policy_name)
    else:
        print(colors.Bcolors.R + "policy_name field is empty!")


def change_scan_policy_ids_by_whitelist(ascanid=None, policy_name='Default Policy'):
    """Enable all active scanners in policy that get into ascanid parameter.
    If policy name is empty it chage Default_Policy"""
    if ascanid is not None:
        print("Disable all scaners -> " + ascan.disable_all_scanners(scanpolicyname=policy_name))
        # Enable some active scanners
        print("Enable given scan IDs -> " + ascan.enable_scanners(ids=ascanid, scanpolicyname=policy_name))
    else:
        print(colors.Bcolors.R + 'ascanid is empty!')


def change_scan_policy_ids_by_blacklist(ascanid=None, policy_name='Default Policy'):
    """Disable all ascan ids for policy get by ids parameter. If policy name is empty it chage Default_Policy."""
    if ascanid is not None:
        print('Enable all scanners -> ' +
              ascan.enable_all_scanners(scanpolicyname=policy_name))
        # Disable some active scanners
        print('Disable given scan IDs -> ' +
              ascan.disable_scanners(ids=ascanid,
                                     scanpolicyname=policy_name))
    else:
        print(colors.Bcolors.R + 'ascanid is empty!')
