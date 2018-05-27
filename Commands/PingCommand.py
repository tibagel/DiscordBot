from Commands.commands import Commands


class PingCommand(Commands):

    def __init__(self):
        self.ouin =""

    async def action(self, msg, args):
        await msg.channel.send("pong")

    async def help(self, msg):
        return ""
