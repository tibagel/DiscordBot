from ctypes.util import find_library
from discord import opus
from Commands.commands import Commands
import discord
from VoicePlayer import Voice_Player
import time

client = discord.Client()
lib = find_library('opus')
discord.opus.load_opus


class Join_Voices(Commands):
    async def action(self, msg, args):
        vp = Voice_Player(msg)
        await vp.join_voice()
        time.sleep(5)
        await vp.voice_disconnect()
