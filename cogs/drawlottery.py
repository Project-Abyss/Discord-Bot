import discord
import random
from discord.ext import commands


class DrawLottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._list_member = bot.users
        self._amount_member = len(bot.users)
        self._list_channel = bot.guilds

    @commands.Cog.listener()
    async def on_ready(self):
        print('DrawLottery cog loaded.')

    @commands.command(name='MembersInfo')
    async def members_info(self, ctx):
        real_member_count = 0
        real_member_list = []

        for i in range(self._amount_member):
            if self._list_member[i].bot != True:
                real_member_count += 1
                real_member_list.append(self._list_member[i].mention)
                #await ctx.send(f'{self._list_member[i]}')              # e.g. bessyhuang#0424

        self._amount_member = real_member_count
        self._list_member = real_member_list

        await ctx.send(f'There are {self._amount_member} members in this channel ~')
        await ctx.send(f'Members: {self._list_member}')

    @commands.command(name='依據成員抽籤', aliases=['抽'], brief="\t頻道內的所有人都逃不掉！\n\t\t\t\t【 範例：!抽 2 】")
    async def draw_lottery_member(self, ctx, amount: int):
        for channel in self._list_channel:
            await ctx.send(f'Draw {amount} lots on {channel.name} channel.')
        
        real_member_namelist = []
        for i in range(len(self._list_member)):
            real_member_namelist.append(str(self._list_member[i]))

        result = random.sample(real_member_namelist, k=amount)
        await ctx.send(f'公佈中籤名單：{result}')
        #await ctx.send(f'==> {discord.utils.get(guild.roles, name="RD")}')

    @commands.command(name='依據身份抽籤')
    async def getuser(self, ctx):
        user = discord.utils.find(lambda m: str(m) == 'bessyhuang#0424', ctx.message.guild.members)
        await ctx.send(f'{user}')

async def setup(bot):
    await bot.add_cog(DrawLottery(bot))
