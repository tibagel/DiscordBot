import discord
import token_babo
from utils import Utils
from Commands import *
import asyncio
import configparser
from logger import Logger


class MyClient(discord.Client):
    commands = dict()
    commands["ping"] = PingCommand()
    commands["clear"] = Clear()
    commands['changeGame'] = ChangeGame()
    commands['Gsearch'] = Gsearch()

    global config_checked
    config_checked = False
    config = configparser.RawConfigParser()
    config.read('config.ini')
    global prefix
    prefix = Utils.get_config('Settings','prefix')
    text_triggers = {}


    async def on_ready(self):
        print('|logged in as {} .  The discord version is {}|'.format(self.user, discord.__version__))
        await client.change_presence(game=discord.Game(name="vec ma graine"))

    async def on_message(self, msg):
        logger = Logger()
        logger.check_dirs(msg.guild.id, msg.guild.text_channels)
        content = msg.content
        print(Utils.msg_parser(msg))
        with open('text_log.txt', 'a') as file:
            file.write(Utils.msg_parser(msg) + '\n')
            file.close()
            if content == '$babo':
                await msg.channel.send(Utils.q_google('dindon'))

        parser = Utils(msg)
        if prefix in content and not msg.author.bot:
            cmd = parser.cmd_parser()
            if cmd.invoke in content:
                await self.commands[cmd.invoke].action(msg=msg, args=cmd.args)
        else:
            logger.write_to_log(message=msg)
            await logger.check_for_triggers(msg)


client = MyClient()
