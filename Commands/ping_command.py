from Commands.commands import Commands
from discord import Embed
from discord import Colour


class PingCommand(Commands):
    def __init__(self):
        super()
        self.msg = None

    async def action(self, msg, args, client):
        self.msg = msg
        from main import client
        latency_ms = int(client.latency * 1000)
        description = ":ping_pong: **{0}** ms".format(latency_ms)
        embed = Embed(
            description=description,
            colour=Colour.magenta()
        )
        await msg.channel.send(embed=embed)
        self.done()

    @staticmethod
    async def help(msg):
        await msg.channel.send("Ping c'est pas compliqué")

    async def executed(self):
        print("Faut que j'arrête de coder de la marde")
        return self.state
