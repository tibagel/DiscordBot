from Commands import commands
from Commands.ping_command import PingCommand
from Commands.clear import Clear
from Commands.change_game import ChangeGame
from Commands.googlesearch import Gsearch
from Commands.Voicetest import Join_Voices
from Commands.get_logs import GetLogs
from Commands.trigger_commands import TriggerCommands
from Commands.prefix import Prefix
from main import client
import token_babo
client.run(token_babo.token)
