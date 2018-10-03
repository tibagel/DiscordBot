import discord
import youtube_dl
import asyncio
import os

__author__ = 'Alex Bergeron'

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

    def voice_disconnect(self):
        asyncio.run_coroutine_threadsafe(self.vc.disconnect(), self.vc.loop)

    async def file_play(self, file):
        vc = self.vc
        vc.play(discord.FFmpegPCMAudio(file), after=lambda e: self.voice_disconnect())

    async def url_play(self,url):
        try:
            os.remove('yt.m4a')
        except Exception as e:
            pass
        try:
            vc = self.vc
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
                vc.play(discord.FFmpegPCMAudio('yt.m4a'), after=lambda e: self.voice_disconnect())
        except Exception as e:
            print(e)
            self.voice_disconnect()