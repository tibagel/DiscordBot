from time import gmtime, strftime
import discord

def msg_parser(message):
    time_recv = strftime('|%Y-%m-%d %H:%M:%S|',gmtime())
    msg = [message.author,message.content,time_recv,message.channel]
    print(str(msg[2])+'~'+str(msg[3])+'~| '+str(msg[0])+': '+str(msg[1]))

def cmd_parser(message):
    splitted_content = message.content.split()
    split_word = list(splitted_content[0])
    if split_word[0] == '$':
        return True

def test_func(message):
    splitted_content = message.content.split()
    for each_splitted_content in splitted_content:
        print(list(each_splitted_content))