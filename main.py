import discord
import token_babo
from utils import Utils


class MyClient(discord.Client):

    async def on_ready(self):
        print('|logged in as {} .  The discord version is {}|'.format(self.user,discord.__version__))

    async def on_message(self, message):
        print(Utils.msg_parser(message))
        with open('text_log.txt','a') as file:
            file.write(Utils.msg_parser(message)+ '\n')
            file.close()
            if message.content == '$babo':
                await message.channel.send(Utils.q_google('dindon'))

        parser = Utils(message)
        if "!" in message.content:
            parser.cmd_parser()


client = MyClient()
client.run(token_babo.token)
