import discord
from discord.ext import commands
from discord import Member
from discord.ext import tasks
from discord.utils import get

triggers = ['sx', 'darby', 'deku', 'harsh', 'sakamoto', 'vanshika', 'weedboii',
            'diven', 'keshav', 'dazai', 'diablo', 'fak', 'remon', 'ishan', 'shlok', 'bisim']
responses = ['https://tenor.com/view/smiley-3d-vibe-check-creepy-gif-15669762',
             'https://media.discordapp.net/attachments/648031568756998158/859925392709517332/image0.gif',
             'They call me P-R-O-P-H-E-T I count up all the thots I see!', 'gareeb bas naam se',
             'Pervertization', 'nub', 'did you mean priya?',
             "Diven? Who's that bitch <:holup:783200762007650304>",
             'https://tenor.com/view/family-vindiesel-fastandfurious-gif-5179042',
             "Let's commit double suicide.",
             "Here's Little Known Fact About Me: There's nothing To know about me",
             'https://imgur.com/a/ZU4Mqrc', 'https://tenor.com/view/eksundar-baccha-gif-21878483',
             'https://tenor.com/view/mdlr-gif-19578119', 'https://c.tenor.com/yPKQXLN9KwEAAAAM/futa-futanari.gif',
             'https://tenor.com/view/ice-eating-ok-and-gif-19666657']

roles = {
    "Water":"WaterPing",
    "Valorant":"Valorant",
    "Genshin":"Genshin Impact",
    "Krunker":"Krunker",
    "Skribbl":"Skribbl",
    "Brawlhalla":"Brawlhalla"
         }


def getAllRoles(roles):
    rolelist = list(roles.keys())
    length = len(rolelist)-1
    roles = ""
    for x in rolelist:
        if(rolelist.index(x) != length):
            roles = roles+'**'+x+'**'+", "
        else:
            roles = roles+"**"+x+"**"+"."

    return roles



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


    @commands.command()
    async def toggle(self, ctx, rolename=None):
        if(rolename != None):
            rolename = rolename.lower()
            rolename = rolename.capitalize()
            if(rolename != "List"):
                if(rolename in roles.keys()):
                    rolen = roles[rolename]
                    role = discord.utils.get(ctx.guild.roles, name=rolen)
                    if(role not in ctx.author.roles):
                        await ctx.author.add_roles(role)
                        await ctx.channel.send(f"The {rolename} role was given to you <:keiyay:879679090100154410>")
                    else:
                        await ctx.author.remove_roles(role)
                        await ctx.channel.send(f"The {rolename} role was taken from you <a:keihayaku:879679192390828052>")
                else:
                    await ctx.channel.send(f'The role {rolename} does not exist. Check the list of avilable roles by using "k!toggle list"')
            else:
                await ctx.send(f"This is the list of all the avilable roles: {getAllRoles(roles)}")
        else:
            await ctx.channel.send('Check the list of all avilable roles by using `k!toggle list`.')







def setup(client):
    client.add_cog(misc(client))
