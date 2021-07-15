import discord
from discord.ext import commands
from discord import Member
from discord.ext import tasks
from discord.utils import get

triggers = ['sx', 'darby', 'deku', 'harsh', 'sakamoto', 'vanshika', 'weedboii',
            'diven', 'keshav', 'dazai', 'diablo', 'fak', 'remon', 'ishan', 'shlok']
responses = ['https://tenor.com/view/smiley-3d-vibe-check-creepy-gif-15669762', 'Hawas ka pujaari',
             'They call me P-R-O-P-H-E-T I count up all the thots I see!', 'gareeb bas naam se',
             'Pervertization', 'nub', 'did you mean priya?',
             "Diven? Who's that bitch <:holup:783200762007650304>",
             'https://tenor.com/view/family-vindiesel-fastandfurious-gif-5179042',
             "Let's commit double suicide.",
             "Here's Little Known Fact About Me: There's nothing To know about me",
             'https://imgur.com/a/ZU4Mqrc', 'https://tenor.com/view/eksundar-baccha-gif-21878483',
             'https://tenor.com/view/mdlr-gif-19578119', 'https://c.tenor.com/yPKQXLN9KwEAAAAM/futa-futanari.gif']

#role_alias = ['water', "waifu wars"]
#role_ID = ['WaterPing', 'WaifuWars']

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

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            msg = message
            for trig in triggers:
                if trig == message.content.lower():
                    index_t = triggers.index(trig)
                    response = responses[index_t]
                    await message.channel.send(response)

    @commands.command()
    async def togglewater(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name= "WaterPing")
        if role not in ctx.author.roles:
            await ctx.author.add_roles(role)
            await ctx.channel.send("The WaterPing role was given to you!")
        else:
            await ctx.author.remove_roles(role)
            await ctx.channel.send("The WaterPing role was taken from you.")

    '''@commands.command()
    async def toggle(self, ctx, rolename):
        if rolename not in role_alias:
            ctx.channel.send("That role does not exist! Use the command `k!rolelist` to get the list of available roles")
        else:
            role_index = role_ID.index(rolename)
            role =role_ID(role_index)
            print(role)'''





def setup(client):
    client.add_cog(misc(client))
