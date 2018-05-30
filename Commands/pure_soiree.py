from Commands.commands import Commands
from Voice_utils import Voice_Player
from discord import opus
import discord
from ctypes.util import find_library

client = discord.Client()
lib = find_library('opus')
opus.load_opus


class PureSoiree(Commands):
    async def action(self, msg, args):
        vp = Voice_Player(msg)
        await vp.join_voice()
        await vp.file_play('pure_soire.mp3')
        await msg.channel.send('Je sens que ce matin va être une pure soiré!')
