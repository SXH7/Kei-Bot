import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont

file = open('TOKEN.txt', 'r')
data = file.read()
print(data)

file2 = open('bannedword.txt', 'r')
bannedWords = file2.read().split()
print(bannedWords)

status = cycle(["discord.gg/bb8bTCr", "weedboii face reveal go brrr", "'bie' hai saale 'bye' nahi", "piyush harami", "pro editor in the houes, Deku#7015"])

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'k!', intents = intents)



# READY INDICATOR
@client.event
async def on_ready():
    change_game.start()
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
    await client.get_channel(682540092992389228).send(f"Everybody welcome the newest member of {member.guild.name}, {member.mention}. You can get your roles from {self_roles.mention}."
                                                      f" Read the rules here {rules.mention}. Enjoy yourself, contact the mods or admins if you have any issues.")

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

client.run(data)

