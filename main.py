import discord
import logging
import discord_token
from parser import msg_parser
from discord.ext import commands




client = commands.Bot(command_prefix='$')
#token = open('token.txt','r')
#tok = token.read()

@client.event
async def on_message(message):
    msg_parser(message)
    await client.process_commands(message)
#    print(message.attachments)
#    test_func(message)
#    if cmd_parser(message) == True:
#       await client.send_message(message.channel, 'Hola senior'+' '+message.author.mention+' ! '+'eres el hombre !!')

@client.command()
async def ping():
    await client.say('Pong!')         

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command()
async def git():
    await client.say("https://github.com/tibagel/DiscordBot")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Avec ma graine'))
    print('discord version:',discord.__version__)
    print("Logged in as")
    print(client.user.name)
    print("----------------")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


client.run(discord_token.token_babo)