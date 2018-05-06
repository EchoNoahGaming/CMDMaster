import discord
from discord.ext import commands
import random
import asyncio

description = '''CMDMaster [Version 1.0.0]
2018 Echolandia Studios.'''
bot = commands.Bot(command_prefix='>', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="CMDMaster [Version 1.0.0]"))

@bot.command()
async def echo(content='ECHO is on.'):
    """Displays messages."""
    await bot.say(content)
        
@bot.command()
async def ver():
    """Displays the CMDMaster version."""
    await bot.say("CMDMaster [Version 1.0.0]")
    
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
	
bot.run('NDQyNjgwMjI3NjE3OTY0MDMy.DdCVqA.01DYrfOPx5a3d3UYR7TW0qtmx6g')
