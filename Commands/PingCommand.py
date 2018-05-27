from Commands import commands


class PingCommand(commands.Commands):

    def __init__(self):
        self.ouin =""

    async def action(self, msg):
        await msg.channel.send("pong")

    async def help(self, msg):
        return ""
