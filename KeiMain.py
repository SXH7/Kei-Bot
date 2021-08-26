import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time
import random

file = open('TOKEN.txt', 'r')
data = file.read()

file2 = open('bannedword.txt', 'r')
bannedWords = file2.read().split()

status = cycle(["discord.gg/bb8bTCr", "weedboii face reveal go brrr", "'bie' hai saale 'bye' nahi", "darby harami", "pro editor in the houes, Deku#7015"])

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'k!', intents = intents)

night_time = ["04 PM", "05 PM", "06 PM", "07 PM", "08 PM", "09 PM", "10 PM", "11 PM", "12 AM", "01 AM", "02 AM"]

water_images = ['https://imgur.com/zh6HuZd',
                'https://imgur.com/QdLWeFA',
                'https://imgur.com/zYycm6n',
                'https://imgur.com/FpehOvj',
                'https://imgur.com/z7mViLc',
                'https://imgur.com/a/8wrl5pc',
                'https://imgur.com/qWzAqyb',
                'https://imgur.com/IDk36ZB',
                'https://imgur.com/Xx5ZOPd']

# READY INDICATOR
@client.event
async def on_ready():
    change_game.start()
    water_reminder.start()
    print("The bot is ready.")



#COD LOAD/UNLOAD COMMANDS
@client.command()
async def load(ctx, extention):
    if (ctx.message.author.id == 394378558308352001):
        client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    if (ctx.message.author.id == 394378558308352001):
        client.unload_extension(f'cogs.{extention}')

@client.command()
async def reload(ctx, extention):
    if (ctx.message.author.id == 394378558308352001):
        client.unload_extension(f'cogs.{extention}')
        client.load_extension(f'cogs.{extention}')


#BOT PRESENCE LOOPS
@tasks.loop(hours= 1)
async def change_game():
    await client.change_presence(activity=discord.Game(next(status)))


#welcome command

@client.event
async def on_member_join(member):
    self_roles = client.get_channel(711422716875636807)
    rules = client.get_channel(688009156179132431)
    intro = client.get_channel(692049221431590982)
    await client.get_channel(682540092992389228).send(f"Everybody welcome the newest member of {member.guild.name}, {member.mention}. You can get your roles from {self_roles.mention}."
                                                      f" Read the rules here {rules.mention}, introduce yourself in {intro.mention}. Enjoy yourself, contact the mods or admins if you have any issues.")

    img = Image.open("background.png")
    draw = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("KGALittleSpark.ttf", 90)
    font2 = ImageFont.truetype("RowanMaskide.ttf", 90)

    textvar = member.name
    draw.text((100, 50), "Welcome to the server!", (0, 0, 0), font=font2, stroke_width=3, stroke_fill="#ffffff")
    draw.text((100, 185), textvar, (0, 0, 0), font=font1, stroke_width=3, stroke_fill="#ffffff")
    img.save('img.png')
    file=discord.File('img.png')
    await client.get_channel(688005133602259056).send(f"Welcome to the server {member.mention}. Have a great time here!")
    await client.get_channel(688005133602259056).send(file= file)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    for each in bannedWords:
        if(message.content == each):
            await message.delete()

    await client.process_commands(message)

@tasks.loop(hours=1.0)
async def water_reminder():
    picture = random.randint(0, 8)
    timegmt = time.strftime("%I %p", time.gmtime())
    if(timegmt in night_time):
        print(timegmt)
    else:
        await client.get_channel(682540092992389228).send("<@&849874571829313537> Go drink water <:water:855361454235320360>\n "+water_images[picture])
#<@&849874571829313537>
client.run(data)
