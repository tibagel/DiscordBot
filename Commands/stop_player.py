from Commands.commands import Commands
from Voice_utils import Voice_Player
import discord


class StopPlayer(Commands):
    async def action(self, msg, args, client):
        for cli in client.voice_clients:
            await cli.disconnect()
            await msg.channel.send('Stopped the shit')
