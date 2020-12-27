import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("The Example Cog is Ready")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason = reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount):
        amount = int(amount)+1
        await ctx.channel.purge(limit= amount)



def setup(client):
    client.add_cog(Example(client))

