import discord
from discord.ext import commands

class template_3(discord.ui.Modal, title='Announcement'):
    content = discord.ui.TextInput(label='Content', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f' **【Announcement】**\
                                                \n------------------------------------------------------------\
                                                \n{self.content}', ephemeral=False)

class Modal_3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_3(bot))