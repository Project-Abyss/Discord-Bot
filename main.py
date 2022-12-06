import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def menu_templates():
    initial_extensions = ['cogs.Announcement', 'cogs.Facebook_post', 'cogs.Foreign_courses', 'cogs.Internal_courses', 'cogs.Meeting_Announcement_1', 'cogs.Meeting_Announcement_2', 'cogs.Resource_storage', 'cogs.menu']
    for extension in initial_extensions:
        await bot.load_extension(extension)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
            
@bot.command(name='quit')
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

bot.run(TOKEN)
