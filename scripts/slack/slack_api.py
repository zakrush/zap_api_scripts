import requests
import json
import time


class Slack:
    def __init__(self, webhook=None, token=None, channel_id=None, channel=None, slack_url=None):
        """Init Slack sender.
        :param webhook: Webhook for slack APP (e.g. https://hooks.slack.com/services/sadASFDA)
        It using only in posting messages in slack channel by Slack Application. Hook copied from slack application
        config
        :param token: Token for slack. It using by bot. (e.g. xoxb-123456789012-1234567890123-dasdasdf)
        :param channel_id: channel id that can be found in browser string
        :param channel: channel name (e.g. #channel)
        :param slack_url: URL of slack (e.g. https://company.slack.com)
        """
        self.hook = webhook
        self.token = token
        self.channel = channel
        self.channel_id = channel_id
        self.slack_url = slack_url
        self.header = {'content-type': 'application/json'}

    def post_message_to_slack(self, text):
        slack_answer = requests.post(self.hook, json={'text': text},
                                     headers=self.header)
        if slack_answer.status_code == 200:
            return slack_answer
        else:
            print("Slack return ", slack_answer.status_code)

    def upload_file(self, report_from='Daily_OWASP_ZAP(Regression)', file=None):
        """
        Upload file to slack channel
        :param report_from: Default setup as "Daily_OWASP_ZAP(Regression). This text was printed in initial comment
        :param file: full path to file for upload
        :return: slack answer (request object)
        """
        if file:
            try:
                slack_answer = requests.post(
                    self.slack_url + '/api/files.upload',
                    {
                        'token': self.token,
                        'channels': self.channel,
                        'initial_comment': report_from
                    },
                    files={'file': open(file, 'rb')})
            except FileNotFoundError:
                self.post_message_to_slack(f"*{file}* not FOUND")
            else:
                if self.check_answer(slack_answer):
                    return slack_answer
        else:
            print("File didn't setup.")

    @staticmethod
    def check_answer(answer):
        if answer.status_code != 200:
            print('Error into request body for Slack. Status code is ' + answer.status_code)
            return False
        elif json.loads(answer.content)['ok'] is False:
            print('Error into slack response: ' + json.loads(answer.content)['error'])
            return False
        else:
            return True

    def find_files(self):
        slack_answer = requests.post(
            self.slack_url + '/api/files.list',
            {
                'token': self.token,
                'channel': self.channel_id,
                'ts_to': int(time.time())
            })
        return slack_answer

    def del_files(self, file_id):
        slack_answer = requests.post(
            self.slack_url + '/api/files.delete',
            {
                'token': self.token,
                'file': file_id
            })
        return slack_answer
