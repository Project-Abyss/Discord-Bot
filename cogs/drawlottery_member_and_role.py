import discord
import random
from discord.ext import commands


class draw_member_and_role(discord.ui.Modal, title ='Draw Member & Role'):
    amount = discord.ui.TextInput(label='Number of people', placeholder='2')
    somebody = discord.ui.TextInput(label='Tag users & roles', placeholder='role1,user1,user2,role2,role3', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        input_somebody_split = str(self.somebody).split(",")

        all_members_list = []
        for sb in input_somebody_split:
            try:
                user_name = discord.utils.get(guild.members, name=sb)
                print(user_name)
                if user_name.mention not in all_members_list:
                    all_members_list.append(user_name.mention)
            except:
                role_id = discord.utils.get(guild.roles, name=sb).id
                role_members = discord.utils.get(guild.roles, id=role_id).members
                for m in role_members:
                    if m.mention not in all_members_list:
                        all_members_list.append(m.mention)

        result = random.sample(all_members_list, k=eval(str(self.amount)))
        await interaction.response.send_message(f' **【Draw Member & Role】**\n \
            > _Candidates_: {all_members_list}\n \
            > _Result_: <#{result}>', ephemeral=False)


class Modal_draw_member_and_role(commands.Cog, draw_member_and_role):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_draw_member_and_role(bot))
