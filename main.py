import discord
import token_babo
from discord_parser import Discord_parser

class MyClient(discord.Client):

    async def on_ready(self):
        print('logged in as {} .  The discord version is {}'.format(self.user,discord.__version__))

    async def on_message(self, message):
        print(Discord_parser.msg_parser(message))

client = MyClient()
client.run(token_babo.token)
