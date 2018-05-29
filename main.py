import discord
from utils import Utils
from Commands import *
import configparser
from logger import Logger


class MyClient(discord.Client):
    commands = dict()
    commands["ping"] = PingCommand()
    commands["clear"] = Clear()
    commands['changeGame'] = ChangeGame()
    commands['search'] = Gsearch()
    commands['getlogs'] = GetLogs()
    commands['trigger'] = TriggerCommands()
    commands['prefix'] = Prefix()
    commands['dinde'] = dinde()


    global config_checked
    config_checked = False
    config = configparser.RawConfigParser()
    config.read('config.ini')
    global prefix
    prefix = ""
    text_triggers = {}

    async def on_ready(self):
        print('|logged in as {} .  The discord version is {}|'.format(self.user, discord.__version__))
        await client.change_presence(game=discord.Game(name="vec ma graine"))

    async def on_message(self, msg):
        logger = Logger()
        Logger.check_dirs(logger, msg.guild.id, msg.guild.text_channels)
        global prefix
        prefix = Utils.get_config('Settings', prefix, msg)
        content = msg.content
        print(Utils.msg_parser(msg))
        parser = Utils(msg)
        client.get_user()

        if prefix in content and not msg.author.bot:
            cmd = parser.cmd_parser()
            if cmd.invoke in content:
                await self.commands[cmd.invoke].action(msg=msg, args=cmd.args)
        elif not msg.author.bot:
            logger.write_to_log(msg=msg)
            await logger.check_for_triggers(msg)

    def get_prefix(self):
        return prefix

client = MyClient()
