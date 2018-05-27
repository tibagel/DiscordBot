from Commands.commands import Commands
from logger import Logger
import configparser
from discord import Embed
from discord import Colour
from pathlib import Path


class TriggerCommands(Commands):
    async def action(self, msg, args):
        args_list = list(args)
        param1 = args_list[0]
        triggers = ""
        config_file_path = Path(str(msg.guild.id) + "/triggers.ini")
        trigger_config = configparser.ConfigParser()
        trigger_config.read(config_file_path)
        text_triggers = Logger.get_triggers(Logger)

        if param1 == "add" and args_list[2]:
            key = args_list[1]
            value = args_list[2]
            text_triggers[key] = value
            await msg.channel.send("Trigger :**" + key + "** Added")
            trigger_config.set("text_triggers", key, value)
            with open(config_file_path, "w") as config_file:
                trigger_config.write(config_file)

        elif param1 == "del":
            key = args_list[1]
            if key in text_triggers:
                del text_triggers[key]
                trigger_config.remove_option("text_triggers", key)
                with open(config_file_path, "w") as config_file:
                    trigger_config.write(config_file)
                await msg.channel.send("Trigger **" + key + "** deleted")
            else:
                await msg.channel.send("This triggers doesn't exist")

        elif param1 == "list":
            embedded_message = Embed(
                title="Voici la liste des triggers",
                colour=Colour.dark_gold()
            )
            embedded_message.set_author(name="Gaspé",
                                        icon_url="https://www.beautifulworld.com/wp-content/uploads/2016/10/perce-rock-quebec-canada.jpg")

            for key in text_triggers:
                triggers += key + ": " + text_triggers[key] + "\n"

            embedded_message.add_field(name="so", value=triggers, inline=True)
            embedded_message.set_footer(text="Asteur décrisses")
            await msg.channel.send(embed=embedded_message)
