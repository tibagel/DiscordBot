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
import asyncio

global config_checked
config_checked = False
config = configparser.RawConfigParser()
config.read('config.ini')
prefix = config.get('Settings', 'prefix')
client = commands.Bot(command_prefix=prefix)
text_triggers = {}


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

    # Initializing the basic triggers.ini or loading it
    config_file_path = Path(server+"/triggers.ini")
    if not config_file_path.exists():
        config_file = open(config_file_path, "w")
        trigger_config = configparser.ConfigParser()
        trigger_config.add_section("text_triggers")
        trigger_config.add_section("sound_triggers")
        trigger_config.set("text_triggers", "soer", "matin")
        trigger_config.write(config_file)
        config_file.close()
    else:
        trigger_config = configparser.ConfigParser()
        trigger_config.read(config_file_path)
        for key, val in trigger_config.items("text_triggers"):
            text_triggers[key] = val

        print(text_triggers)

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

    else:  # If it's text, it goes in a text file, duh
        text_log_path = Path(message.server.id + "/" + message.channel.name + "/text_logs.txt")
        text_log_file = open(text_log_path, "a+")
        print(msg_parser(message))
        text_log_file.write(msg_parser(message))


@asyncio.coroutine
async def check_for_triggers(message):
    content = message.content
    for key in text_triggers:
        if key in content:
            await client.send_message(message.channel, text_triggers[key])


@client.event
async def on_message(message):
    msg_parser(message)
    await client.process_commands(message)


@client.event
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
    if not author.bot and content.startswith(prefix):  # If the author is not a bot(Neo is that you? )
        await client.process_commands(message)
    elif not author.bot:
        write_to_log(message)
        await check_for_triggers(message)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)
