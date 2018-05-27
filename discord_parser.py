from time import gmtime, strftime

class Discord_parser():

    def msg_parser(message):
        time_recv = strftime('|%Y-%m-%d %H:%M:%S|', gmtime())
        msg = [time_recv, message.channel, message.author, message.content]
        formatted_msg = ('{}~{}~| {}: {} '.format(*msg))
        return formatted_msg + "\n"
