from Commands import commands
from Commands.ping_command import PingCommand
from Commands.clear import Clear
from Commands.change_game import ChangeGame
from Commands.googlesearch import Gsearch
from Commands.dinde import dinde
from Commands.get_logs import GetLogs
from Commands.trigger_commands import TriggerCommands
from Commands.youtube_play import play
from Commands.Stop_player import stop_player
from Commands.pure_soiree import PureSoiree
from Commands.cmd_git import CmdGit
from Commands.prefix import Prefix
from main import client
import token_babo
client.run(token_babo.token)