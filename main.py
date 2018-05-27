import discord
import token_babo
from discord_parser import Utils


class MyClient(discord.Client):

    async def on_ready(self):
        print('|logged in as {} .  The discord version is {}|'.format(self.user,discord.__version__))

    async def on_message(self, message):
        print(Utils.msg_parser(message))
        try:
            with open('text_log.txt','a') as file:
                file.write(Utils.msg_parser(message)+ '\n')
                file.close()
            if message.content == '$babo':
                await message.channel.send(Utils.q_google('dindon'))
        except Exception as e:
            print(e)


client = MyClient()
client.run(token_babo.token)
