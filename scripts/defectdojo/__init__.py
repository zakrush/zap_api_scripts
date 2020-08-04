"""
COPIED FROM https://github.com/DefectDojo/defectdojo_api/tree/master/defectdojo_api
"""
import defectdojo.defectdojo_apiv2 as defectdojo
import json
import os
import time
import datetime
import scan_core.api_conf as conf


class DefectDojoTB(defectdojo_apiv2.DefectDojoAPIv2):
    def __init__(self, host=conf.dd_host, api_token=conf.dd_key, user=conf.dd_user, verify_ssl=True, timeout=60,
                 proxies=None, user_agent=None, cert=None, debug=False, product_name=None, engagement_name=None):
        self.product_name, self.engagement_name = product_name, engagement_name
        super().__init__(host, api_token, user, api_version='v2', verify_ssl=verify_ssl, timeout=timeout,
                         proxies=proxies, user_agent=user_agent, cert=cert, debug=debug)

    def get_product_id(self):
        if self.product_name is not None:
            projects_list = self.list_products(name=self.product_name)
            if projects_list.count() == 0:
                print(f"Project {self.product_name.upper()} not found.")
            elif projects_list.count() == 1:
                return projects_list.data['results'][0]['id']
            else:
                wrong_string = "Something wrong. Founded projects: "
                print(wrong_string, end="")
                [print(" " * len(wrong_string), str(project['name'])) for project in projects_list.data['results']]
        else:
            print("Setup product_name variable")

    @property
    def get_engagements_id(self):
        if self.product_name is not None and self.engagement_name is not None:
            result = self.list_engagements(product_id=self.get_product_id(),
                                           name_contains=self.engagement_name)
            if result.count() == 0:
                print("Engagements not found in project")
            else:
                eng_list = dict()
                for eng in result.data['results']:
                    if eng['name'].find(self.engagement_name) != -1:
                        eng_list[eng['id']] = eng['name']
                if len(eng_list) == 0:
                    print(f"Engagement with name cotaining \"{self.engagement_name}\" "
                          f"wasn't found in product {self.product_name}")
                elif len(eng_list) == 1:
                    print(f'Engagement with name cotaining {self.engagement_name} was found.')
                    return [key for key in eng_list.keys()][0]
                else:
                    print(f"Please detail name of engagements. Was found: {','.join(eng_list.values())}")

        else:
            print('Setup product_name and engagements_name in get_engagements_id function')

    def import_tb_scan(self, scan_type=None, file=None, active=True, verified=False, close_old_findings=False,
                       skip_duplicates=False, scan_date=datetime.datetime.now().strftime('%Y-%m-%d'), tags=None,
                       minimum_severity='Info'):

        if scan_type and file and tags:
            return self.upload_scan(engagement_id=self.get_engagements_id,
                                    scan_type=scan_type,
                                    file=file,
                                    active=active,
                                    verified=verified,
                                    close_old_findings=close_old_findings,
                                    skip_duplicates=skip_duplicates,
                                    scan_date=scan_date,
                                    tags=tags,
                                    minimum_severity=minimum_severity
                                    )
        else:
            return f"'scan_type' is '{scan_type}' or 'file' is '{file}', 'tags' is '{tags}' " \
                   f"is not defined when importing report"
