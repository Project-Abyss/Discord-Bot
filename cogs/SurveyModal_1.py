import discord
from discord.ext import commands

class template_1(discord.ui.Modal, title ='Meeting Announcement'):
    meeting_time = discord.ui.TextInput(label = 'Time')
    meeting_channel = discord.ui.TextInput(label = 'Channel')
    content = discord.ui.TextInput(label='Content', style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        # content
        content_str = str(self.content)
        content_split = content_str.split("\n")
        result = []
        for i in range(len(content_split)):
            content_split_2 = content_split[i].split('    ')
            for j in range(len(content_split_2)):
                if j == 0:
                    content_split_new = str(content_split_2[0])
                    content_split_2[j] =  '❖ ' + content_split_new +'\n'
                    result.append(content_split_2[j])
                else:
                    content_split_new = str(content_split_2[j])
                    content_split_2[j] = '    ⟡ ' + content_split_new + '\n'
                    result.append(content_split_2[j])
        final_result = "".join(result)
        # meeting channel
        guild = interaction.guild
        for channel in guild.channels:
            if str(self.meeting_channel) == channel.name:
                final_channel_id = channel.id   
        await interaction.response.send_message(f' **【Meeting Announcement】**\n> _Time_: {self.meeting_time}\n\
                                                > _Channel_: <#{final_channel_id}>\
                                                \n-----------------------------\n{final_result}', ephemeral=False)

class Modal_1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_1(bot))
