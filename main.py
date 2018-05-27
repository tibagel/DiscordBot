import discord
import token_babo
from utils import Utils
from Commands import *
import asyncio


class MyClient(discord.Client):
    commands = dict()
    commands["ping"] = PingCommand()
    commands["clear"] = Clear()

    async def on_ready(self):
        print('|logged in as {} .  The discord version is {}|'.format(self.user, discord.__version__))

    async def on_message(self, msg):
        content = msg.content
        print(Utils.msg_parser(msg))
        with open('text_log.txt', 'a') as file:
            file.write(Utils.msg_parser(msg) + '\n')
            file.close()
            if content == '$babo':
                await msg.channel.send(Utils.q_google('dindon'))

        parser = Utils(msg)
        if "!" in content:
            cmd = parser.cmd_parser()
            if cmd.invoke in content:
                loop = client.loop
                client.loop.create_task(self.commands[cmd.invoke].action(msg=msg, args=cmd.args))

        else:
            parser.msg_parser()


client = MyClient()
