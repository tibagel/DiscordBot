from pathlib import Path
import os
import configparser
import re
import requests
from utils import Utils
import asyncio


class Logger:
    global text_triggers
    text_triggers = {}

    def check_dirs(self, server, channels):
        server_dir = Path(str(server))
        if not server_dir.exists():  # Checking if the log directory exists for this server
            os.makedirs(server_dir)
            print("Folder:", server_dir, "created")

        for channel in channels:
            path = str(server) + "/" + channel.name + "/"
            channel_dir = Path(path)
            # Checking if a log directory exists for each text channels, creating it if not
            if not channel_dir.exists():
                os.makedirs(channel_dir)
                os.makedirs(Path(path + "Images"))  # Creating sub folder Images in the text channel's folder
                os.makedirs(Path(path + "Files"))  # Subfolder Files
                print("Created ", channel.name, "directory at:", path)

        # Initializing the basic triggers.ini or loading it
        config_file_path = Path(str(server) + "/triggers.ini")
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


        global config_checked
        config_checked = True

    def write_to_log(self, message):
        from main import client
        self.check_dirs(message.guild, client.get_all_channels())

        attachments = message.attachments
        if attachments:  # If the message contains something
            image_regex = re.compile(
                "(http(s)?):(\\/\\/[a-z0-9A-Z\\+%&\\?\\.\\/_-]+)(\\.(jp(e)?g)|(tif(f)?)|gif|bmp|png|ico)")
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
            text_log_path = Path(str(message.guild.id) + "/" + message.channel.name + "/text_logs.txt")
            text_log_file = open(text_log_path, "a+")
            text_log_file.write(Utils.msg_parser(message)+"\n")

    @asyncio.coroutine
    async def check_for_triggers(self, message):
        content = message.content
        for key in text_triggers:
            if key in content:
                await message.channel.send(text_triggers[key])
