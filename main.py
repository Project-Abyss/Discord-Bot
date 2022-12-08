import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from cogs.greetings import Greetings
from cogs.example import Example
from cogs.drawlottery import DrawLottery


load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.load_extension('cogs.greetings')
    await bot.load_extension('cogs.example')
    await bot.load_extension('cogs.drawlottery')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
            
@bot.command(name='q', aliases=['quit', 'close', 'exit', 'bye'])
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

"""
@bot.command(name='member')
async def member(ctx):
    #await ctx.send(f'{bot.users}')
    for i in range(len(bot.users)):
        if bot.users[i].bot != True:
            await ctx.send(f'{bot.users[i]}')
            print(bot.users[i].mention)

@bot.command(name='g')
async def g(ctx):
    guilds = [guild async for guild in bot.fetch_guilds(limit=150)]
    print(guilds)

@bot.command(name='channel')
async def channel(ctx):
    voice_channel_list = ctx.guild.voice_channels
    await ctx.send(f'{voice_channel_list}')

    for voice_channels in voice_channel_list:
        print('voice_channels:', voice_channels)
        for member in voice_channels.members:
            print('- MEMBER:', member)
"""


bot.run(TOKEN)
