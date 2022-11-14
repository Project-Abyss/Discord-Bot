import discord, os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>',intents = discord.Intents.all())

for guild in bot.guilds:
    for text_ch in guild.text_channels:
        pass
        # print(text_ch.id)
        
@bot.event
async def on_ready():
    print('Online.')
    # channel = bot.get_channel(int(LOBBY_CHANNEL))    
    # await channel.send("早安您好，小機器人上線啦", delete_after=10)

@bot.command()
async def ping(ctx):
	await ctx.send(f'{round(bot.latency*1000)}(ms)')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message[0] == '>':
        return
    if message.author == bot.user:
        return
    
# Close the bot
@bot.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await ctx.message.delete()
    await bot.close()

@bot.event
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            
async def main(): 
    await load()
    await bot.start(TOKEN)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
