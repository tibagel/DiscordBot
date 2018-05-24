from main import client
from main import text_triggers


@client.command(pass_context=True)
async def trigger(ctx,*args):
    args_list = list(args)
    if args_list[0] == "add":
        del args_list[0]
        message_remain = str(args_list).split('"')
        key = message_remain[0]
        value = message_remain[1]
        print(message_remain)
        for word in args_list:
            value += word
        text_triggers[key] = value


