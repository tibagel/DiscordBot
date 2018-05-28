import discord


class Voice_Player:
    def __init__(self, msg):
        self.channel = msg.channel
        self.author = msg.author
        self.content = msg.content
        self.msg = msg
        self.vc = None

    async def join_voice(self):
        try:
            author = self.author
            self.vc = await discord.VoiceChannel.connect(author.voice.channel)
        except Exception as e:
            print(e)
        return self.vc

    async def voice_disconnect(self):
        await self.vc.disconnect()
