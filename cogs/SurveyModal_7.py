import discord
from discord.ext import commands

# 模板七
class template_7(discord.ui.Modal, title='FaceBook 貼文發表'):
    #大框框
    post_time = discord.ui.TextInput(label = 'Time')
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f' **【Facebook 貼文發表】**\n．Time: {self.post_time}', ephemeral=False)

# 繼承 commands.Cog 的類別
class Modal_7(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_7(bot))