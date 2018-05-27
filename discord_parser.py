from time import gmtime, strftime


class Discord_parser():

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
        raw_args = no_head.replace(invoke, "", 1)!s
        if '"' in raw_args:
            splitted = raw_args.split('"')
        else:
            splitted = raw_args.split(" ")
        del splitted[0]
        print(splitted)
