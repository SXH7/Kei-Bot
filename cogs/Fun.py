import discord
from discord.ext import commands
import praw
import random

reddit = praw.Reddit(client_id = "tpThwIQjP1tYhA",
                     client_secret = "iiz8VruzO5y2XRksqClXxQxC6hXCIQ",
                     username = "shashwat_senpai",
                     password = "shashwwat@reddit",
                     user_agent = "Kei Bot")



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

        await ctx.send(embed = em)

def setup(client):
    client.add_cog(FunCommands(client))
