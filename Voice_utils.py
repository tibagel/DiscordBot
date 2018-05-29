import discord

class Voice_Player:

	def __init__(self,msg):
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

	async def voice_disconnect(self):
		if self.vc is not None:
			await self.vc.disconnect()

	async def file_play(self,file):
		if self.vc is not None:
			self.vc.play(discord.FFmpegPCMAudio(file))


	async def url_play(self, url):
		if self.vc is not None:
			ydl_opts = {
				'outtmpl': 'yt.m4a',
				'format': 'bestaudio/best',
				'postprocessors': [{
					'key': 'FFmpegExtractAudio',
					'preferredcodec': 'm4a',
				}],
			}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
				self.vc.play(discord.FFmpegPCMAudio('yt.m4a'), after=lambda self: asyncio.run_coroutine_threadsafe(self.vc.disconnect()))
			if not self.vc.is_playing():
				os.remove('yt.m4a')
