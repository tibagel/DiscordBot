from Commands import commands
from Commands.ping_command import PingCommand
from Commands.clear import Clear
from Commands.change_game import ChangeGame
from main import client
import token_babo
client.run(token_babo.token)