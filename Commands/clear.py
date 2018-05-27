from Commands.commands import Commands


class Clear(Commands):
    async def action(self, msg, args):
        channel = msg.channel
        messages = []
        async for message in channel.history(limit=int(args[0])):
            messages.append(message)
        await channel.delete_messages(messages)
        await msg.channel.send("**" + str(len(messages)) + "** messages were deleted.")