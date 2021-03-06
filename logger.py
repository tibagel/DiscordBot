from pathlib import Path
import os
import configparser
import re
import requests
from utils import Utils
from Commands.Audio import youtube_play
from Commands.Audio.voice_utils import VoicePlayer
import asyncio
from discord import *


class Logger:
    global txt_triggers
    txt_triggers = {}

    @staticmethod
    def check_dirs(server, channels):
        server_dir = Path(str(server))
        if not server_dir.exists():  # Checking if the log directory exists for this server
            os.makedirs(server_dir)
            print("Folder:", server_dir, "created")

        for channel in channels:
            path = str(server) + "/" + channel.name + "/"
            chan_dir = Path(path)
            # Checking if a log directory exists for each text channels, creating it if not
            if not chan_dir.exists():
                os.makedirs(chan_dir)
                os.makedirs(Path(path + "Images"))  # Creating sub folder Images in the text channel's folder
                os.makedirs(Path(path + "Files"))  # Subfolder Files
                print("Created ", channel.name, "directory at:", path)

        # Initializing the basic triggers.ini or loading it
        config_file_path = Path(str(server) + "/triggers.ini")
        if not config_file_path.exists():
            conf_file = open(config_file_path, "w")
            trigger_conf = configparser.ConfigParser()
            trigger_conf.add_section("text_triggers")
            trigger_conf.add_section("sound_triggers")
            trigger_conf.set("text_triggers", "soer", "matin")
            trigger_conf.write(conf_file)
            conf_file.close()
        else:
            trigger_conf = configparser.ConfigParser()
            trigger_conf.read(str(server) + "/triggers.ini")
            for key, val in trigger_conf.items("text_triggers"):
                txt_triggers[key] = val

        global config_checked
        config_checked = True

    @staticmethod
    def write_to_log(msg):
        atts = msg.attachments
        embeds = msg.embeds
        request = None
        svr = str(msg.guild.id)
        chan_name = msg.channel.name
        global path
        path = ""
        if atts:  # If the message contains something
            image_regex = re.compile(
                "(http(s)?):(//[a-z0-9A-Z+%&?./_-]+)(\\.(jp(e)?g)|(tif(f)?)|gif|bmp|png|ico)")
            for att in atts:
                if att.height and image_regex.match(att.url):
                    request = requests.get(att.url).content
                    path = svr + "/" + chan_name + "/Images/" + att.filename
                else:  # Setting the path accordingly
                    request = requests.get(att.url).content
                    path = svr + "/" + chan_name + "/Files/" + att.filename

                with open(path, "wb") as file:
                    file.write(request)

        elif not embeds == Embed.Empty:
            print("ouin")
            text_log_path = str(msg.guild.id) + "/" + chan_name + "/text_logs.txt"
            text_log_file = open(text_log_path, "a+")
            text_log_file.write(Utils.msg_parser(msg) + "\n")

    @asyncio.coroutine
    async def check_for_triggers(self, msg):
        content = msg.content
        for key in txt_triggers:
            if key in content:  # If the message contains a Trigger word
                if txt_triggers[key].startswith("http"):  # If the trigger key starts with http it means it's an audio trigger
                    await youtube_play.Play().play(vp=VoicePlayer(msg), url=txt_triggers[key])
                else:  # Else it's a plain text trigger
                    await msg.channel.send(txt_triggers[key])


    @staticmethod
    def get_triggers():
        return txt_triggers
