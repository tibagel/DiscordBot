import discord
import logging
from discord.ext import commands
import configparser
from msg_parser import msg_parser
import Commands

config = configparser.RawConfigParser()
config.read('config.ini')
prefix = config.get('Settings','prefix')
client = commands.Bot(command_prefix=prefix)


@client.event
async def on_message(message):
    msg_parser(message)
    await client.process_commands(message)

<<<<<<< Updated upstream
=======
@client.command()
async def ping():
    await client.say('Pong!')

@client.command(pass_context=True)
async def clear(ctx,amount=2):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say(str(len(messages))+" messages were deleted.",delete_after=float(3))

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command()
async def git():
    embed = discord.Embed(
        title = 'GitHub Tibagel',
        description = 'Bad code and shit',
        colour = discord.Colour.magenta()
        )
    embed.set_footer(text='penchez vous tous')
    embed.set_image(url='https://i.imgur.com/hBYEPoB.png')
    embed.set_author(name='Le Dindon',icon_url='https://i.imgur.com/jGZ3fX1.png')
    embed.add_field(name='Le hub du petit matin', value='https://github.com/tibagel/DiscordBot',inline=True)
    await client.say(embed=embed)
        


>>>>>>> Stashed changes
'''
@client.command()
async def prefix(*args):
    prex = ''
    for word in args:
        prex += word
    config.set('Settings','prefix',prex)
    with open('config.ini','w') as configfile:
        config.write(configfile)
    with open('config.ini','r') as configfile:
        prex = config.get('Settings','prefix')
'''    


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Avec ma graine'))
    print('discord version: {}\nLogged in as: {}'.format(discord.__version__,client.user.name))
    print("------------------------------------")


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)
