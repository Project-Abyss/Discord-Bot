import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('HIHIHIHI')

    @commands.command(brief="Any message to owo")
    async def ppp(self, ctx):
        await ctx.send('Pong~~~')

async def setup(bot):
    await bot.add_cog(Example(bot))

