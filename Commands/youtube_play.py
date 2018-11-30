from Commands.commands import Commands
from utils import Utils
from Voice_utils import Voice_Player
from ctypes.util import find_library
import discord
from discord import opus
client = discord.Client()
lib = find_library('opus')
opus.load_opus


class Play(Commands):
    def __init__(self):
        super()

    async def action(self, msg, args, client):
        output = ''
        for word in args:
            output += word + ' '
            url = Utils.q_google('youtube.com:' + output)
        await self.play(Voice_Player(msg), msg.channel, url)

    async def play(self, vp, channel, url):
        await vp.join_voice()
        await vp.url_play(url)
        await channel.send('Now playing: '+url)
