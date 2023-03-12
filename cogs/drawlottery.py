import discord
import random
from discord.ext import commands
from discord.utils import get


class DrawLottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._list_member = bot.users
        self._amount_member = len(bot.users)
        self._list_channel = bot.guilds

    @commands.Cog.listener()
    async def on_ready(self):
        print('DrawLottery cog loaded.')

    @commands.command(name='MembersInfo', aliases=['info'], brief="\n")
    async def members_info(self, ctx):
        real_member_count = 0
        real_member_list = []

        for i in range(self._amount_member):
            if self._list_member[i].bot != True:
                real_member_count += 1
                real_member_list.append(self._list_member[i].mention)
                #await ctx.send(f'{self._list_member[i]}')              		# e.g. bessyhuang#0424

        self._amount_member = real_member_count
        self._list_member = real_member_list

        await ctx.send(f'There are {self._amount_member} members in this channel ~')
        await ctx.send(f'Members: {self._list_member}')

    @commands.command(name='依據指定成員抽籤', aliases=['member'], brief="\n\t被點到的人都逃不掉！\n\t【 範例：!member_v2 2 成員1 成員2 成員3 】\n")
    async def draw_specific_lottery_member(self, ctx, amount: int, *users):
        all_members_list = []
        for user in users:
            user_id = user.replace('<@', '').replace('>', '')
            user_name = discord.utils.get(ctx.guild.members, id=eval(user_id))
            if user_name not in all_members_list:
                all_members_list.append(user_name.mention)
        
        await ctx.send(f'參與抽籤的成員：{all_members_list}')

        result = random.sample(all_members_list, k=amount)
        await ctx.send(f'公佈中籤名單：{result}')

    @commands.command(name='依據身份組抽籤', aliases=['role'], brief="\n\t選擇多個身份組後，再抽簽！\n\t【 範例：!role 2 身份組1 身份組2 身份組3 】\n")
    async def draw_lottery_role(self, ctx, amount: int, *roles):
        all_members_list = []
        for role in roles:
            role_id = role.replace('<@&', '').replace('>', '')
            role_name = discord.utils.get(ctx.guild.roles, id=eval(role_id))
            role_members = discord.utils.get(ctx.guild.roles, id=eval(role_id)).members
            for m in role_members:
                if m not in all_members_list:
                    all_members_list.append(m.mention)
        
        await ctx.send(f'參與抽籤的成員：{all_members_list}')

        result = random.sample(all_members_list, k=amount)
        await ctx.send(f'公佈中籤名單：{result}')

    @commands.command(name='依據指定成員或身份組抽籤', aliases=['mix'], brief="\n\t選擇多個指定成員或身份組後，再抽簽！\n\t【 範例：!mix 2 身份組1 成員1 成員2 身份組2 身份組3 成員3 】\n")
    async def draw_lottery_member_and_role(self, ctx, amount: int, *somebody):
        all_members_list = []
        for sb in somebody:
            if "<@&" in sb:
                role_id = sb.replace('<@&', '').replace('>', '')
                role_name = discord.utils.get(ctx.guild.roles, id=eval(role_id))
                role_members = discord.utils.get(ctx.guild.roles, id=eval(role_id)).members
                for m in role_members:
                    if m.mention not in all_members_list:
                        all_members_list.append(m.mention)
            elif "<@" in sb:
                user_id = sb.replace('<@', '').replace('>', '')
                user_name = discord.utils.get(ctx.guild.members, id=eval(user_id))
                if user_name.mention not in all_members_list:
                    all_members_list.append(user_name.mention)

        await ctx.send(f'參與抽籤的成員：{all_members_list}')
        
        result = random.sample(all_members_list, k=amount)
        await ctx.send(f'公佈中籤名單：{result}')

async def setup(bot):
    await bot.add_cog(DrawLottery(bot))
