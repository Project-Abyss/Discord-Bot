import discord
from discord.ext import commands

class PollMenu(discord.ui.Modal, title ='VOTE'):
    multiOrSingle = discord.ui.TextInput(label='Multiple Vote or Single Vote', placeholder='Multi or Sing')
    pollTitle = discord.ui.TextInput(label='Poll Title', placeholder='Which color do you like?')
    timeLimit = discord.ui.TextInput(label='The End Date', placeholder='2222-02-22 22:22:22')
    optionDescription = discord.ui.TextInput(label='Option Title', placeholder='Blue Red Green......')

    async def on_submit(self, interaction: discord.Interaction):
        optionGroup = str(self.optionDescription).split(" ")
        optionGroup = " ".join(str(i) for i in optionGroup)
        if str(self.multiOrSingle) == 'Multi':
            await interaction.response.send_message(f'SYNTAX: !MultiAnswer {self.pollTitle} {self.timeLimit} {optionGroup}')
        elif str(self.multiOrSingle) == 'Sing':
            await interaction.response.send_message(f'SYNTAX: !SingleAnswer {self.pollTitle} {self.timeLimit} {optionGroup}')
        else:
            await interaction.response.send_message("Please Choose \"Multi\" or \"Sing\" !")

class PollMenuModel(commands.Cog, PollMenu):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(PollMenuModel(bot))
