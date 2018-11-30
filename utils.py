from time import gmtime, strftime
from googleapiclient.discovery import build
from token_babo import my_api_key
from token_babo import my_cse_id
import configparser
import shlex
from discord import Embed
from discord import Colour
from pathlib import Path


class Utils:
    def __init__(self, msg):
        self.channel = msg.channel
        self.author = msg.author
        self.content = msg.content
        self.msg = msg

    def msg_parser(self):
        time_recv = strftime('|%Y-%m-%d %H:%M:%S|', gmtime())
        msg = [time_recv, self.channel, self.author, self.content]
        formatted_msg = ('{}~{}~| {}: {} '.format(*msg))
        return formatted_msg

    @staticmethod
    def cmd_parser(content):
        from main import client
        no_head = content.replace(client.get_prefix(), "")
        no_head_split = no_head.split(" ")
        invoke = no_head_split[0]
        raw_args = no_head.replace(invoke, "", 1)
        args = shlex.split(raw_args)
        return CmdContainer(invoke, args, content)

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']

    def q_google(search):
        results = Utils.google_search(search, my_api_key, my_cse_id, num=1)
        for result in results:
            return result['link']

    def get_config(setting, option, msg):
        path = str(msg.guild.id)+'/config.ini'
        file = Path(path)
        config = configparser.RawConfigParser()
        if not file.exists():
            config_file = open(file, "w")
            config.add_section("Settings")
            config.set("Settings", "prefix", "!")
            config.write(config_file)
            config_file.close()
            return config.get(setting, "prefix")
        else:
            config.read(path)
            return config.get(setting, "prefix")

    def embed_templ(title, description=None, field1=None, field2=None, author=None, image_author=None):
        embed = Embed(
            title=title,
            description=description,
            colour=Colour.magenta()
        )
        embed.add_field(name=field1, value=field2, inline=True)
        embed.set_author(name=author, icon_url=image_author)
        return embed


class CmdContainer:
    def __init__(self, invoke, args, msg):
        self.invoke = invoke
        self.args = args
        self.message = msg
