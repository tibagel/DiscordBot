from Commands.commands import Commands
import discord


class ChangeGame(Commands):
    async def action(self, msg, args, client):
        game = ''
        for word in args:
            game += word + ' '
        from main import client
        await client.change_presence(game=discord.Game(name=game))
