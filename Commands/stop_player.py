from Commands.commands import Commands



class StopPlayer(Commands):
    async def action(self, msg, args, client):
        for cli in client.voice_clients:
            cli.stop()
            await msg.channel.send('Stopped the shit')
