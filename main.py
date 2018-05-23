import discord
import logging
from discord.ext import commands
import configparser
from msg_parser import msg_parser
import Commands

config = configparser.RawConfigParser()
config.read('config.ini')
prefix = config.get('Settings', 'prefix')
client = commands.Bot(command_prefix=prefix)


@client.event
async def on_message(message):
    msg_parser(message)
    await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Avec ma graine'))
    print('discord version:', discord.__version__)
    print("Logged in as")
    print(client.user.name)
    print("----------------")


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)
