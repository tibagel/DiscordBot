from ctypes.util import find_library
from Commands.commands import Commands
import discord
from Commands.Audio.voice_utils import VoicePlayer
from discord import opus

client = discord.Client()
lib = find_library('opus')
opus.load_opus(lib)


class Dinde(Commands):
    async def action(self, msg, args, client):
        vp = VoicePlayer(msg)
        await vp.join_voice()
        await vp.file_play('Turkey.m4a')
