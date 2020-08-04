import defectdojo.defectdojo_apiv2 as defectdojo
import json
import os
import time
import datetime
import configs.reports_config as conf




dd = defectdojo.DefectDojoAPIv2(conf.dd_host, conf.dd_key, conf.dd_user, debug=False)


def get_product_id(product_name=None):
    if product_name is not None:
        projects_list = dd.list_products(name=product_name)
        if projects_list.count() == 0:
            print(f"Project {product_name.upper()} not found.")
        elif projects_list.count() == 1:
            return projects_list.data['results'][0]['id']
        else:
            wrong_string = "Something wrong. Founded projects: "
            print(wrong_string, end="")
            for project in projects_list.data['results']:
                print(" " * len(wrong_string), str(project['name']))

    else:
        print("Setup product_name variable")


def get_engagements_id(product_name=None, engagements_name=None):
    if product_name is not None and engagements_name is not None:
        result = dd.list_engagements(product_id=get_product_id(product_name=product_name),
                                     name_contains=engagements_name)
        if result.count() == 0:
            print("Engagements not found in project")
        else:
            eng_list = dict()
            for eng in result.data['results']:
                if eng['name'].find(name_of_engament) != -1:
                    eng_list[eng['id']] = eng['name']
            if len(eng_list) == 0:
                print(f"Engagement with name cotaining \"{engagements_name}\" wasn't found in product {product_name}")
            elif len(eng_list) == 1:
                print(f'Engagement with name cotaining {engagements_name} was found.')
                return [key for key in eng_list.keys()][0]
            else:
                print(f"Please detail name of engagements. Was found: {','.join(eng_list.values())}")
            # print(f"Engagement was found {result.data['results'][0]['id']['name']}")

    else:
        print('Setup product_name and engagements_name in get_engagements_id function')


eng_id = get_engagements_id(product_name=name_of_product, engagements_name=name_of_engament)

print(dd.upload_scan(engagement_id=eng_id, scan_type="ZAP Scan",
                     file='/home/dmitriy/DevSecOps/ZAP/reports/regression.xml',
                     active=True,
                     verified=False,
                     close_old_findings=False,
                     skip_duplicates=False,
                     scan_date=datetime.datetime.now().strftime('%Y-%m-%d'),
                     tags="ZAP-daily"))
