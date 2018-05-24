from main import client
from pathlib import Path


@client.command(pass_context=True)
async def logs(ctx):
    message = ctx.message
    channel = message.channel
    file_path = Path(message.server.id + "/" + channel.name + "/text_logs.txt")
    label = "tiens! " + message.author.mention + "Les logs"
    await client.send_file(channel, file_path)
    await client.say(label)
