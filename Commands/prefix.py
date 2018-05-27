from Commands.commands import Commands
import configparser

class Prefix(Commands):
    async def action(self, msg, args):
        config = configparser.RawConfigParser()
        config.read('config.ini')
        prefix = ''
        for word in args:
            prefix += word
        config.set('Settings', "prefix", prefix)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        with open('config.ini', 'r'):
            prefix = config.get('Settings', 'prefix')
