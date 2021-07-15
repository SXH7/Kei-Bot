import discord
from discord.ext import commands

class musicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music commands are ready.')

    @commands.command(pass_context = True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
    
    @commands.command(pass_context = True)
    async def play(self, ctx, url):
        guild = ctx.message.guild
        voice_client = guild.voice_client
        player = await voice_client.create_ytdl_player(url)
        player.start()





def setup(client):
    client.add_cog(musicCommands(client))

