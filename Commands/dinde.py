from ctypes.util import find_library
from discord import opus
from Commands.commands import Commands
import discord
from Voice_utils import Voice_Player

client = discord.Client()
lib = find_library('opus')
discord.opus.load_opus


class dinde(Commands):
    async def action(self, msg, args):
        vp = Voice_Player(msg)
        await vp.join_voice()
        await vp.file_play('Recording.m4a')

