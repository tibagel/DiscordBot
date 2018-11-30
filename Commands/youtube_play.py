from Commands.commands import Commands
from utils import Utils
from voice_utils import VoicePlayer
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
        await self.play(VoicePlayer(msg), msg.channel, url)

    @staticmethod
    async def play(vp, channel, url):
        await vp.join_voice()
        await vp.url_play(url)
        await channel.send('Now playing: '+url)
