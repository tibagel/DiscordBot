from Commands import commands
from Commands.ping_command import PingCommand
from Commands.clear import Clear
from Commands.change_game import ChangeGame
from Commands.googlesearch import Gsearch
from Commands.get_logs import GetLogs
from Commands.trigger_commands import TriggerCommands
from Commands.cmd_git import CmdGit
from Commands.prefix import Prefix
from Commands.Audio.pause_player import PausePlayer
from Commands.Audio.pure_soiree import PureSoiree
from Commands.Audio.resume_player import ResumePlayer
from Commands.Audio.stop_player import StopPlayer
from Commands.Audio.youtube_play import Play
from Commands.Audio.voice_utils import VoicePlayer
from Commands.Audio.dinde import Dinde
from main import client
import token_babo
client.run(token_babo.token)
