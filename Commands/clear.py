from main import client


@client.command(pass_context=True)
async def clear(ctx,amount=2):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say(str(len(messages))+" messages were deleted.")

