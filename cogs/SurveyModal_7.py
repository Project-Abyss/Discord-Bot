import discord
from discord.ext import commands

class template_7(discord.ui.Modal, title='FaceBook 貼文發表'):
    post_time = discord.ui.TextInput(label = 'Time')
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f' **【Facebook 貼文發表】**\n．Time: {self.post_time}', ephemeral=False)

class Modal_7(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_7(bot))