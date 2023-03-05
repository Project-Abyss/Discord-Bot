import discord
from discord.ext import commands

class Poll_Function(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll_Function cog loaded.')

    @commands.command()
    async def SingleAnswer(self, ctx, pollTitle, descriptionMessage):
        emb = discord.Embed(title=f"{pollTitle}", description=f"{descriptionMessage}")
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(":o:")
        await msg.add_reaction(":x:")

    # @commands.command()
    # async def MutiAnswer(self, ctx, pollTitle, descriptionMessage)


async def setup(bot):
    await bot.add_cog(Poll_Function(bot))

