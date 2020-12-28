import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = 'k!', intents = intents)

@client.event
async def on_ready():
    print("The bot is ready.")

@client.command()
async def load(ctx, extention):
    client.load_extension()

client.run('TOKEN')
