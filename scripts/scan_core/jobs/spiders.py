from scan_core import spider, ajax, forcedUser, colors
from scan_core.shared_core import get_context_id_by_name
from time import sleep

##################################################################
#                                                                #
#                           SPIDER                               #
#                                                                #
##################################################################


def spider_scan(context_name='Default Context', user_id=None, target=None, maxchildren=None, recurse=True, thread_count=5,
                ajax_scan=False, robot_txt=True, sitemap_txt=True, postforms=True, request_wait_time=200):

    """ Return scan ID if needed"""

    # Set options of spider

    spider.set_option_parse_robots_txt(robot_txt)
    spider.set_option_parse_sitemap_xml(sitemap_txt)
    spider.set_option_post_form(postforms)
    spider.set_option_request_wait_time(int(request_wait_time))
    if 0 < thread_count<=50:
        spider.set_option_thread_count(int(thread_count))
    else:
        print("Incorrect thread number. It should be from 1 to 50")
    if ajax_scan:
        run_ajax_spider(context_name=context_name, user_id=user_id, target=target)

    print(colors.Bcolors.CN + 'Starting spider-scan for context ' + context_name)

    if user_id is not None:
        print(colors.Bcolors.Y + 'Scan for userId ' + user_id)
        scan_id = spider.scan_as_user(contextId=get_context_id_by_name(contextname=context_name),
                                      userid=user_id, url=target, maxchildren=maxchildren, recurse=recurse)
        sleep(2)  # give the spider chance to start
        while int(spider.status(scan_id)) < 100:
            print('\rSpider progress: ' + spider.status(scan_id) + '%', end='')
        return scan_id

    if user_id is None:
        scan_id = spider.scan(url=target, contextname=context_name, maxchildren=maxchildren, recurse=recurse)
        sleep(2)  # give the spider chance to start
        while int(spider.status(scan_id)) < 100:
            print('\rSpider progress: ' + spider.status(scan_id) + '%', end='')
        return scan_id





##################################################################
#                                                                #
#                           AJAX Spider                          #
#                                                                #
##################################################################

# ajax потом разбираться отдельно буду более глубоко. Пока не понятны его опции
def run_ajax_spider(context_name='Default Context', user_id=None, target=None):
    print('\n' + colors.Bcolors.CN + 'Starting Ajax-spider-scan for context ' + context_name)
    if user_id is not None:
        print('Set forced user mode enabled: ' + forcedUser.set_forced_user_mode_enabled(boolean=True))
        print('Set user ID for forced user mode into ajax_scan: ' + user_id +
               forcedUser.set_forced_user(contextid=get_context_id_by_name(context_name), userid=user_id))
        print(colors.Bcolors.Y + 'Ajax scan for User ID: ' + user_id + ' -> '
               + ajax.scan(url=target, contextname=context_name, inscope=True))
        sleep(10)  # Give the ajax spider a chance to start
        while ajax.status != 'stopped':
            print(colors.Bcolors.CN + '\r' + 'Ajax Spider is ' + ajax.status, end='')
            sleep(5)
        else:
            print('\n' + colors.Bcolors.Y + 'Ajax scan' + user_id + ' -> '
                   + ajax.scan(url=target, contextname=context_name, inscope=True))
            sleep(10)  # Give the ajax spider a chance to start
            while ajax.status != 'stopped':
                print(colors.Bcolors.CN + '\r' + 'Ajax Spider is ' + ajax.status, end='')
                sleep(5)
