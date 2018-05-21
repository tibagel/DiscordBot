from time import gmtime, strftime
import discord
import os

def msg_parser(message):            # for parsing the message content and writing it in a log file
    time_recv = strftime('|%Y-%m-%d %H:%M:%S|',gmtime())
    msg = [time_recv,message.channel,message.author,message.content]
    print('{}~{}~| {}: {} \n'.format(*msg))
    file = open('discord_channel.log','a+')
    file.write('{}~{}~| {}: {} \n'.format(*msg))
    file.close()

#def cmd_parser(message):
#    splitted_content = message.content.split()
#    split_word = list(splitted_content[0])
#    if split_word[0] == '$':
#        return True

#def test_func(message):
#    file = open('discord_channel.log','a+')
#    file.write(str(message))
#    file.close()
