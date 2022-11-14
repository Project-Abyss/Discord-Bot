import discord
from discord.ext import commands

class template_6(discord.ui.Modal, title='遺忘書目'):
    resource_name = discord.ui.TextInput(label = '網站名稱／檔案名稱')
    level = discord.ui.TextInput(label = '難度 (鬼 > 英雄 > 冒險者 > 初心者 > 村民)', placeholder='e.g. 村民 ~ 英雄')
    url = discord.ui.TextInput(label = 'URL')
    content = discord.ui.TextInput(label='概述網站內容', style=discord.TextStyle.paragraph)
    field = discord.ui.TextInput(label = '領域', placeholder='e.g. #Python #Git')
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f' **{self.resource_name}**\
                                                \n難度：{self.level}\
                                                \n@{self.url}\n\
                                                \n{self.content}\n\
                                                \n#{self.field}', ephemeral=False)

class Modal_6(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_6(bot))
