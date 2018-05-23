from time import gmtime, strftime
import discord
import os


def msg_parser(message):  # for parsing the message content and writing it in a log file
    time_recv = strftime('|%Y-%m-%d %H:%M:%S|', gmtime())
    msg = [time_recv, message.channel, message.author, message.content]
    formatted_msg = ('{}~{}~| {}: {} '.format(*msg))
    return formatted_msg + "\n"
