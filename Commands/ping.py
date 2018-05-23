from main import client
import discord_token

@client.command()
async def ping():
    await client.say('Pong!')

