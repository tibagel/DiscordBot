from main import client
import discord


@client.command()
async def changegame(*args):
    game = ''
    for word in args:
        game += word + ' '
    await client.change_presence(game=discord.Game(name=game))
