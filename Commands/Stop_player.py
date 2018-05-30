from Commands.commands import Commands
from Voice_utils import Voice_Player


class stop_player(Commands):
    async def action(self, msg, args):
        Voice_Player.voice_disconnect(self)

