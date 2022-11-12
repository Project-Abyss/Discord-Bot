import discord
from discord.ext import commands

class template_5(discord.ui.Modal, title ='對內課程公告'):
    course_time = discord.ui.TextInput(label = '時間')
    course_location = discord.ui.TextInput(label = '地點')
    course_title = discord.ui.TextInput(label = '課程名稱')
    course_lecturer = discord.ui.TextInput(label = '課程講師')
    course_teachingMaterial = discord.ui.TextInput(label = '課程教材')
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        for member in guild.members:
            if str(self.course_lecturer) == member.name:
                print(member.id, member.name)
                final_member_id = member.id   
        await interaction.response.send_message(f' **【對內課程公告】**\n> 時間: {self.course_time}\
                                                \n> 地點: {self.course_location}\
                                                \n------------------------------------------------------------\
                                                \n．課程名稱: {self.course_title}\
                                                \n．課程講師: <@{final_member_id}>\
                                                \n．課程教材:\
                                                \n\t．{self.course_teachingMaterial}\
                                                \n(如有要請假的請留言回覆告知)', ephemeral=False)

# 繼承 commands.Cog 的類別
class Modal_5(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == commands.user:
            if "Yes" in message.content:
                message_id = message.id
                thread = message.channel.get_thread(message_id)
                await message.message.delete()
                await thread.send("請輸入名字",  delete_after=60)

async def setup(bot):
    await bot.add_cog(Modal_5(bot))