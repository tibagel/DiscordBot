import discord
import logging
from discord.ext import commands
import configparser
from msg_parser import msg_parser
from pathlib import Path
import os
import re
import requests
import Commands

global config_checked
config_checked = False


def check_dirs(server, channels):
    server_dir = Path(server)
    if not server_dir.exists():  # Checking if the log directory exists for this server
        os.makedirs(server_dir)
        print("Folder:", server_dir, "created")
    else:
        print("Dir exists")

    for channel in channels:
        path = server + "/" + channel.name + "/"
        channel_dir = Path(path)
        # Checking if a log directory exists for each text channels, creating it if not
        if not channel_dir.exists() and str(channel.type) == 'text':
            os.makedirs(channel_dir)
            os.makedirs(Path(path+"Images"))  # Creating sub folder Images in the text channel's folder
            os.makedirs(Path(path+"Files"))  # Subfolder Files
            print("Created ", channel.name, "directory at:", path)

    config_file_path = Path(server+"/config_file.ini")
    if not config_file_path.exists():
        config_file = open(server+"/config_file.ini", "w")
        config_file.close()

    global config_checked
    config_checked = True

def write_to_log(message):
    global config_checked
    if not config_checked:
        check_dirs(message.server.id, client.get_all_channels())

    attachments = message.attachments
    if attachments:  # If the message contains something
        image_regex = re.compile("(http(s)?):(\\/\\/[a-z0-9A-Z\\+%&\\?\\.\\/_-]+)(\\.(jp(e)?g)|(tif(f)?)|gif|bmp|png|ico)")
        attachment = attachments[0]
        attachment_url = attachment["url"]
        attachment_filename = attachment["filename"]

        server = message.server.id
        channel_name = message.channel.name
        request = requests.get(attachment_url).content
        global path
        path = ""
        if image_regex.match(attachment_url):  # The attachment is an image
            path = server + "/" + channel_name + "/Images/" + attachment_filename
        else:  # Setting the path accordingly
            path = server + "/" + channel_name + "/Files/" + attachment_filename

        with open(path, "wb") as file:
            file.write(request)

    else:
        text_log_path = Path(message.server.id + "/" + message.channel.name + "/text_logs.txt")
        text_log_file = open(text_log_path, "a+")
        print(msg_parser(message))
        text_log_file.write(msg_parser(message))


config = configparser.RawConfigParser()
config.read('config.ini')
prefix = config.get('Settings', 'prefix')
client = commands.Bot(command_prefix=prefix)


@client.event
<<<<<<< HEAD
async def on_message(message):
    msg_parser(message)
    await client.process_commands(message)


@client.event
=======
>>>>>>> master
async def on_ready():
    await client.change_presence(game=discord.Game(name='Avec ma graine'))
    print('discord version: {}\nLogged in as: {}'.format(discord.__version__,client.user.name))
    print("------------------------------------")


@client.event
async def on_message(message):
    if not config_checked:
        server = message.server.id
        channels = client.get_all_channels()
        check_dirs(server, channels)

    content = message.content
    author = message.author
    if not author.bot and content.startswith("$"):  # If the author is not a bot
        await client.process_commands(message)
        await client.delete_message(message)
    else:
        write_to_log(message)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)
