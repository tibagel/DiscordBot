from main import client
from main import text_triggers
from pathlib import Path
import configparser


@client.command(pass_context=True)
async def trigger(ctx, *args):
    args_list = list(args)
    if args_list[0] == "add":
        del args_list[0]
        key = args_list[0]
        value = args_list[1]
        text_triggers[key] = value
        config_file_path = Path(ctx.message.server.id + "/triggers.ini")
        trigger_config = configparser.ConfigParser()
        trigger_config.read(config_file_path)
        trigger_config.set("text_triggers", key, value)
        with open(config_file_path, "w") as config_file:
            trigger_config.write(config_file)

