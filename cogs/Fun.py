import discord
from discord.ext import commands, tasks
#from discord.utils import get
import praw
import random
from PIL import Image, ImageDraw, ImageFont
#import anilist


reddit = praw.Reddit()

defaultUserUrl = 'https://anilist.co/user/'

class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("The Fun Cog is Ready")

    @commands.command()
    async def reddit(self, ctx, sub: str = ""):
        '''if(sub == "hentai" or sub == "porn" or sub == "fiftyfifty" or sub == "Hentai" or sub == "Porn"):
            await ctx.send(file=discord.File('bonk.png'))'''
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
    @commands.command()
    async def shrex(self, ctx, *,user=None):
        if(user != None):
            if(ctx.message.mentions):

                user = user.replace("<", "")
                user = user.replace(">", "")
                user = user.replace("@", "")
                user = user.replace("!", "")

                username = str(ctx.guild.get_member(int(user)))
                length = len(username)
                username = username[:length-5]

                img = Image.open('C:/Users/shash/PycharmProjects/Kei-Bot/cogs/resources/shrex.jpg')
                draw = ImageDraw.Draw(img)
                author = ctx.author.name
                author = author.lower()
                font = ImageFont.truetype('C:/Users/shash/PycharmProjects/Kei-Bot/cogs/resources/comic.ttf', 14)
                draw.text((20, 194), username, (255, 255, 255), font=font, stroke_width=1, stroke_fill='#000000')
                draw.text((33, 207), author, (255, 255, 255), font=font, stroke_width=1, stroke_fill='#000000')
                img.save('img.png')
                file = discord.File('img.png')
                await ctx.channel.send(file=file)

            else:
                img = Image.open('C:/Users/shash/PycharmProjects/Kei-Bot/cogs/resources/shrex.jpg')
                draw = ImageDraw.Draw(img)
                author = ctx.author.name
                author = author.lower()
                font = ImageFont.truetype('C:/Users/shash/PycharmProjects/Kei-Bot/cogs/resources/comic.ttf', 14)
                draw.text((20, 194), user, (255, 255, 255), font=font, stroke_width=1, stroke_fill='#000000')
                draw.text((33, 207), author, (255, 255, 255), font=font, stroke_width=1, stroke_fill='#000000')
                img.save('img.png')
                file = discord.File('img.png')
                await ctx.channel.send(file=file)
        if(user==None):
            await ctx.channel.send("You must pass something with the command.")



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
