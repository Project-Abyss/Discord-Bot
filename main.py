import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from cogs.greetings import Greetings
from cogs.example import Example

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.load_extension('cogs.greetings')
    await bot.load_extension('cogs.example')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
            
@bot.command(name='quit')
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

bot.run(TOKEN)
