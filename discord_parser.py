from time import gmtime, strftime
from googleapiclient.discovery import build
from token_babo import my_api_key
from token_babo import my_cse_id

class Utils():

    def __init__(self, msg):
        self.channel = msg.channel
        self.author = msg.author
        self.content = msg.content

    def msg_parser(self):
        time_recv = strftime('|%Y-%m-%d %H:%M:%S|', gmtime())
        msg = [time_recv, self.channel, self.author, self.content]
        formatted_msg = ('{}~{}~| {}: {} '.format(*msg))
        return formatted_msg

    def cmd_parser(self):
        content = self.content
        no_head = content.replace("!", "")
        no_head_split = no_head.split(" ")
        invoke = no_head_split[0]
        raw_args = no_head.replace(invoke, "", 1)
        if '"' in raw_args:
            splitted = raw_args.split('"')
        else:
            splitted = raw_args.split(" ")
        del splitted[0]
        print(splitted)

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']

    def q_google(search):
        results = Utils.google_search(search, my_api_key, my_cse_id, num=1)
        for result in results:
            return result['link']
