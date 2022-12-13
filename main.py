import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from cogs.greetings import Greetings
from cogs.drawlottery import DrawLottery


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.load_extension('cogs.greetings')
    await bot.load_extension('cogs.menu')
    await bot.load_extension('cogs.drawlottery')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
            
@bot.command(name='q', aliases=['quit', 'close', 'exit', 'bye'])
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

"""
@bot.command(name='channel')
async def channel(ctx):
    voice_channel_list = ctx.guild.voice_channels
    await ctx.send(f'{voice_channel_list}')		
    # e.g. [<VoiceChannel id=1028862292495970319 name='開會區' rtc_region=None position=0 bitrate=64000 video_quality_mode=<VideoQualityMode.auto: 1> user_limit=0 category_id=1028862292495970317>]

    for voice_channels in voice_channel_list:
        await ctx.send(f'CHANNEL: {voice_channels}')		# e.g. voice_channels: 開會區
        for member in voice_channels.members:
            await ctx.send(f'MEMBER: {member}')
"""

bot.run(TOKEN)
