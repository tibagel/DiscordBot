from Commands.commands import Commands
from discord import Embed
from discord import Colour


class PingCommand(Commands):
    async def action(self, msg, args):
        from main import client
        latency_ms = int(client.latency * 1000)
        description = ":ping_pong: **{0}** ms".format(latency_ms)
        embed = Embed(
            description=description,
            colour=Colour.magenta()
        )
        await msg.channel.send(embed=embed)

    async def help(self, msg):
        return ""
