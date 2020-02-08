from Commands.commands import Commands


class ResumePlayer(Commands):
    async def action(self, msg, args, client):
        for cli in client.voice_clients:
            cli.resume()
            await msg.channel.send('Resumed the shit')
