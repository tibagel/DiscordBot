from Commands.commands import Commands
from discord import File


class GetLogs(Commands):
    async def action(self, msg, args):
        channel = msg.channel
        file_path = str(msg.guild.id) + "/" + channel.name + "/text_logs.txt"
        label = "tiens! " + msg.author.mention + "Les logs"
        await channel.send(file=File(fp=file_path))
        await channel.send(label)
