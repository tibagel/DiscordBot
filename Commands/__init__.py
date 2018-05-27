from Commands import commands
from Commands.ping_command import PingCommand
from Commands.clear import Clear
from Commands.change_game import ChangeGame
from Commands.googlesearch import Gsearch
from Commands.Voicetest import Voices
from Commands.get_logs import GetLogs
from main import client
import token_babo
client.run(token_babo.token)
