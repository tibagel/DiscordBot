from ctypes.util import find_library
from discord import opus
from Commands.commands import Commands
import discord
from voice_utils import VoicePlayer

client = discord.Client()
lib = find_library('opus')
discord.opus.load_opus


class Dinde(Commands):
    async def action(self, msg, args, client):
        vp = VoicePlayer(msg)
        await vp.join_voice()
        await vp.file_play('Turkey.mp3')
