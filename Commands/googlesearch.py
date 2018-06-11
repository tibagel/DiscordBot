from Commands.commands import Commands
from utils import Utils


class Gsearch(Commands):
    async def action(self, msg, args, client):
        output = ''
        for word in args:
            output += word + ' '
        url = Utils.q_google(output)
        await msg.channel.send('This is your URL: {}'.format(url))