import discord
from discord.ext import commands
import requests
import random

class gif(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("GIF Cog is ready")

    @commands.command()
    async def gif(self, ctx, *, query):
        rand = random.randint(0, 19)
        term = 'anime '+query
        search = "https://api.tenor.com/v1/search?q=" + term +"&key=NVTZ7ZVRG92Y&limit=20&media_filter=basic"
        random_request = requests.get(search)
        if random_request.status_code == 200:
            try:
                json_random = random_request.json()['results']
                gif = json_random[rand]
                gif = gif.get("media")
                gif = gif[0]
                gif = gif.get("gif")
                gif = gif.get("url")
                random_embed = discord.Embed(colour=discord.Colour.blue())

                random_embed.set_image(url=gif)
                await ctx.channel.send(embed=random_embed)
            except:
                await ctx.channel.send("{} Sorry, but I hasn't found any gif!".format(ctx.author.mention))

    @commands.command()
    async def hug(self, ctx, *, string=None):
        rand = random.randint(0, 19)
        search = "https://api.tenor.com/v1/search?q=animehug&key=NVTZ7ZVRG92Y&limit=20&media_filter=basic"
        random_request = requests.get(search)
        if random_request.status_code == 200:
            try:
                json_random = random_request.json()['results']
                gif = json_random[rand]
                gif = gif.get("media")
                gif = gif[0]
                gif = gif.get("gif")
                gif = gif.get("url")
                random_embed = discord.Embed(title = "Hug", colour=discord.Colour.blue())
                random_embed.add_field(name= ctx.author.mention+"just hugged "+string)


                random_embed.set_image(url=gif)
                await ctx.channel.send(embed=random_embed)
            except:
                await ctx.channel.send("{} Sorry, but I hasn't found any gif!".format(ctx.author.mention))




def setup(client):
    client.add_cog(gif(client))

