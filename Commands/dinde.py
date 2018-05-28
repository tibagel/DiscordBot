from ctypes.util import find_library
from discord import opus
from Commands.commands import Commands
import discord
from Voice_utils import Voice_Player
import time

client = discord.Client()
lib = find_library('opus')
opus.load_opus(lib)

class dinde(Commands):
    async def action(self, msg, args):
        vp = Voice_Player(msg)
        await vp.join_voice()
        await vp.audio_play()
        time.sleep(1)
        await vp.voice_disconnect()
