import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '!!')
status = cycle(['!!help', 'Hello there!',])

@client.event
async def on_ready():
    change_status.start()
    print("Ready")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('!!help'))

@tasks.loop(seconds = 5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}') 

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('ODAwMjI4OTYwOTk4Nzg1MDU1.YAPFSw.ROvAjQeqGZDxTqiDFjUlgWxoB4c')
