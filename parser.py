from time import gmtime, strftime
import discord
import os

def msg_parser(message):            # for parsing the message content and writing it in a log file
    time_recv = strftime('|%Y-%m-%d %H:%M:%S|',gmtime())
    msg = [message.author,message.content,time_recv,message.channel]
    print(str(msg[2])+'~'+str(msg[3])+'~| '+str(msg[0])+': '+str(msg[1]))
    file = open('discord_channel.log','a+')
    file.write(str(msg[2])+'~'+str(msg[3])+'~| '+str(msg[0])+': '+str(msg[1])+'\n')
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
