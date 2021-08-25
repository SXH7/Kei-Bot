import discord
from discord.ext import commands
import praw
import random
#import anilist


reddit = praw.Reddit(client_id = "tpThwIQjP1tYhA",
                     client_secret = "iiz8VruzO5y2XRksqClXxQxC6hXCIQ",
                     username = "shashwat_senpai",
                     password = "shashwwat@reddit",
                     user_agent = "Kei Bot")

defaultUserUrl = 'https://anilist.co/user/'

class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("The Fun Cog is Ready")

    @commands.command()
    async def reddit(self, ctx, sub: str = ""):
        subreddit = reddit.subreddit(sub)
        hot = subreddit.hot(limit = 100)
        allsub = []
        for submissions in hot:
            allsub.append(submissions)

        post = random.choice(allsub)
        name = post.title
        url = post.url

        em = discord.Embed(title = name)
        em.set_image(url = url)
        if post.over_18:
            await ctx.send("https://imgur.com/a/5HKgTzU")
        else:
            await ctx.send(embed = em)



"""    @commands.group(name='anilist', invoke_without_command=True)
    async def anilist(self, ctx):
        await ctx.channel.send('The anilist commands available are: **user**, **anime**, **manga**.')
        
    @anilist.command(name='user')
    async def user_subcommand(self, ctx, *, username):
        await ctx.channel.send(defaultUserUrl+username)

    @anilist.command(name='anime')
    async def anime_subcommand(self, ctx):
        await ctx.channel.send('anime subcommand')"""


def setup(client):
    client.add_cog(FunCommands(client))
