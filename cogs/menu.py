import discord
from discord.ext import commands
from discord.ui import Button, View

from .Meeting_Announcement_1 import template_1
from .Meeting_Announcement_2 import template_2
from .Announcement import template_3
from .Foreign_courses import template_4
from .Internal_courses import *
from .Resource_storage import template_6
from .Facebook_post import template_7
from .drawlottery_member_and_role import draw_member_and_role
from .PollFunction_Menu import PollMenu

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Draw Member & Role", emoji="😱", description="依據指定成員或身份組抽籤"),
            discord.SelectOption(label="Meeting Announcement 1",emoji="1️⃣",description="時間、頻道、備註"),
            discord.SelectOption(label="Meeting Announcement 2",emoji="2️⃣",description="時間、頻道、成員、備註"),
            discord.SelectOption(label="Announcement",emoji="3️⃣",description="備註"),
            discord.SelectOption(label="對外課程公告",emoji="4️⃣",description="時間、地點、課程名稱、課程講師、課程教材"),
            discord.SelectOption(label="對內課程公告",emoji="5️⃣",description="時間、地點、課程名稱、課程講師、課程教材、15 speech 講者"),
            discord.SelectOption(label="遺忘書目",emoji="6️⃣",description="難度、URL、概述、領域"),
            discord.SelectOption(label="FaceBook 貼文發表",emoji="7️⃣",description="時間")
            discord.SelectOption(label="Make a Poll",emoji="8️⃣",description="建立多票制或單票制投票活動")
        ]
        super().__init__(placeholder="Choose an announcement template.",max_values=1,min_values=1,options=options)
    # callback
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
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
        elif self.values[0] == "Draw Member & Role":
            await interaction.response.send_modal(draw_member_and_role())
        elif self.values[0] == "Make a Poll":
            await interaction.response.send_modal(PollMenu())


class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # default delete time
        self.sec = 60

    @commands.Cog.listener()
    async def on_ready(self):
        print('Menu cog loaded.')

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("Select announcement",view=SelectView(), delete_after=int(self.sec))
        await ctx.message.delete()

    @commands.command()
    async def time(self, ctx, msg):
        await ctx.message.delete()
        self.sec = msg

    @commands.Cog.listener()
    async def on_message(self, message):
        if "【Facebook 貼文發表】" in message.content:
            await message.create_thread(name = "【Facebook 貼文發表】", auto_archive_duration=60, slowmode_delay=None, reason=None)

        if "【對內課程公告】" in message.content:
            button = Button(label = " 有 ",style=discord.ButtonStyle.green)
            async def button_callback(interaction):
                await interaction.response.send_modal(who_is_the_lucky_guy())
            button.callback = button_callback
            view = View()
            view.add_item(button)
            await message.channel.send("這週有 15 Speech 的人嗎？", view=view, delete_after=int(self.sec))

async def setup(bot):
    await bot.add_cog(Menu(bot))
