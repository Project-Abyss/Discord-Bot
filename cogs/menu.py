import discord
from discord.ext import commands
from .SurveyModal_1 import template_1
from .SurveyModal_2 import template_2
from .SurveyModal_3 import template_3
from .SurveyModal_4 import template_4
from .SurveyModal_5 import *
from .SurveyModal_6 import template_6
from .SurveyModal_7 import template_7

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Meeting Announcement 1",emoji="1️⃣",description="時間、頻道、備註"),
            discord.SelectOption(label="Meeting Announcement 2",emoji="2️⃣",description="時間、頻道、成員、備註"),
            discord.SelectOption(label="Announcement",emoji="3️⃣",description="備註"),
            discord.SelectOption(label="對外課程公告",emoji="4️⃣",description="時間、地點、課程名稱、課程講師、課程教材"),
            discord.SelectOption(label="對內課程公告",emoji="5️⃣",description="時間、地點、課程名稱、課程講師、課程教材、15 speech 講者"),
            discord.SelectOption(label="遺忘書目",emoji="6️⃣",description="難度、URL、概述、領域"),
            discord.SelectOption(label="FaceBook 貼文發表",emoji="7️⃣",description="時間")       
            ]
        super().__init__(placeholder="Choose an announcement template.",max_values=1,min_values=1,options=options)
        
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        # print(guild.id)
        ## update this
        if self.values[0] == "Meeting Announcement 1":
            await interaction.response.send_modal(template_1())
        elif self.values[0] == "Meeting Announcement 2":
            await interaction.response.send_modal(template_2())
        elif self.values[0] == "Announcement":
            await interaction.response.send_modal(template_3())
        elif self.values[0] == "對外課程公告":
            await interaction.response.send_modal(template_4())
        elif self.values[0] == "對內課程公告":
            await interaction.response.send_modal(template_5())
        elif self.values[0] == "遺忘書目":
            await interaction.response.send_modal(template_6())
        elif self.values[0] == "FaceBook 貼文發表":
            await interaction.response.send_modal(template_7()) 

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Menu cog loaded.')

    @commands.command()
    async def menu(self, ctx):
        await ctx.message.delete()
        await ctx.send("Select announcement",view=SelectView(), delete_after=10)
    

    @commands.Cog.listener()
    async def on_message(self, message):
        if "【Facebook 貼文發表】" in message.content:
            await message.create_thread(name = "【Facebook 貼文發表】", auto_archive_duration=60, slowmode_delay=None, reason=None)
        if "【對內課程公告】" in message.content:
            message_id = message.id
            await message.create_thread(name = "【對內課程公告】", auto_archive_duration=60, slowmode_delay=None, reason=None)
            thread = message.channel.get_thread(message_id)
            await thread.send("這周有 This 15 Speech 嗎？ \n(Yes or No)",  delete_after=60)
                    
async def setup(bot):
    await bot.add_cog(Menu(bot))
