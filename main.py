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
    commands['play'] = play()
    commands['stop'] = stop_player()
    commands['pure'] = PureSoiree()
    commands['git'] = CmdGit()


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
        parser = Utils(msg)
        print(parser.msg_parser())

        if prefix in content and not msg.author.bot:
            global help_content
            help_content = ""
            if prefix + "help" in content:
                help_content = content.replace("help ", "")
                cmd = parser.cmd_parser(help_content)
            elif prefix + "stop" in content:
                for cli in client.voice_clients:
                    cli.voice_disconnect()
            else:
                cmd = parser.cmd_parser(msg.content)

            try:
                if cmd.invoke in content and help_content == "":
                    await self.commands[cmd.invoke].action(msg=msg, args=cmd.args)
                    await self.commands[cmd.invoke].executed()
                else:
                    await self.commands[cmd.invoke].help(msg=msg)
            except KeyError as e:
                print('{} 404: Command not found '.format(e))
        elif not msg.author.bot:
            logger.write_to_log(msg=msg)
            await logger.check_for_triggers(msg)

    def get_prefix(self):
        return prefix


client = MyClient()