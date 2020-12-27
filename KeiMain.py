import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'k!', intents = intents)

@client.event
async def on_ready():
    print("The bot is ready")

client.run('NzkyNjExOTU3MDM0OTc1MjMy.X-gPaA.GPVTjMgw-jXmr2i8Tbf2RSozWiY')
