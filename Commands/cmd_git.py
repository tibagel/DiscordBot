from Commands.commands import Commands


class CmdGit(Commands):
    async def action(self, msg, args, client):
        await msg.channel.send('https://github.com/tibagel/DiscordBot')
