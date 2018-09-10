from Commands.commands import Commands



class PausePlayer(Commands):
    async def action(self, msg, args, client):
        for cli in client.voice_clients:
            cli.pause()
            await msg.channel.send('Paused the shit')
