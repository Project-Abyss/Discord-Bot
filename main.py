import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from function.greetings import Greetings
from function.Poll_Function import Poll_Function


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.load_extension('function.greetings')
    await bot.load_extension('function.menu')
    await bot.load_extension('function.drawlottery')
    await bot.load_extension('function.Poll_Function')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
            
@bot.command(name='q', aliases=['quit', 'close', 'exit', 'bye'])
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

bot.run(TOKEN)
