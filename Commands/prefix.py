from Commands.commands import Commands
import configparser


class Prefix(Commands):
    async def action(self, msg, args, client):
        config = configparser.RawConfigParser()
        config.read(str(msg.guild.id)+'/config.ini')
        prefix = ''
        for word in args:
            prefix += word
        config.set('Settings', "prefix", prefix)
        with open(str(msg.guild.id)+'/config.ini', 'w') as configfile:
            config.write(configfile)
