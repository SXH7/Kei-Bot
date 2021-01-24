import discord
from discord.ext import commands
from discord import Member

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("The misc cog is ready")

    @commands.command()
    async def pfp(self, ctx, member: Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title= member.display_name+"'s pfp")
        embed.set_image(url= member.avatar_url)

        await ctx.send(embed= embed)

def setup(client):
    client.add_cog(misc(client))
