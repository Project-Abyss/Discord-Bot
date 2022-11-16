import discord
from discord.ext import commands

class template_5(discord.ui.Modal, title ='對內課程公告'):
    course_time = discord.ui.TextInput(label = '時間', placeholder='2022/11/16 18:30 ~ 20:30')
    course_location = discord.ui.TextInput(label = '地點')
    course_title = discord.ui.TextInput(label = '課程名稱')
    course_lecturer = discord.ui.TextInput(label = '課程講師', placeholder='請填寫帳號全名')
    course_teachingMaterial = discord.ui.TextInput(label = '課程教材')
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        for member in guild.members:
            if str(self.course_lecturer) == member.name:
                final_member_id = member.id  
        await interaction.response.send_message(f' **【對內課程公告】**\n> 時間: {self.course_time}\
                                                \n> 地點: {self.course_location}\
                                                \n------------------------------------------------------------\
                                                \n．課程名稱: {self.course_title}\
                                                \n．課程講師: <@{final_member_id}>\
                                                \n．課程教材:\
                                                \n\t．{self.course_teachingMaterial}\
                                                \n(如有要請假的請留言回覆告知)', ephemeral=False)

class who_is_the_lucky_guy(discord.ui.Modal, title ='This 15 Speech'):
    fifteen_speech = discord.ui.TextInput(label = '幸運兒', placeholder='請填寫帳號全名')
    async def on_submit(self, interaction: discord.Interaction):  
        guild = interaction.guild
        for member in guild.members:
            if str(self.fifteen_speech) == member.name:
                self.final_member_id = member.id
        await interaction.response.send_message(f'> This 15 Speech: <@{self.final_member_id}>', ephemeral=False)

class Modal_5(commands.Cog, template_5):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_5(bot))
