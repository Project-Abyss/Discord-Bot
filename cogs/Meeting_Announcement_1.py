import discord
from discord.ext import commands

class template_1(discord.ui.Modal, title ='Meeting Announcement'):
    meeting_time = discord.ui.TextInput(label = 'Time', placeholder='Nov. 14th, 2022(Mon.) 00:00~23:59')
    meeting_channel = discord.ui.TextInput(label = 'Channel', placeholder='請輸入頻道全名')
    content = discord.ui.TextInput(label='Content', placeholder='主要內容與附屬內容間隔「四個空格」', style = discord.TextStyle.paragraph)
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
        # time
        time = str(self.meeting_time)
        re_time = []
        time_split = time.split(" ")
        for i in range(len(time_split)-1):
            normal = time_split[i]
            re_time.append(normal)
        for j in range(len(time_split)):
            italic = time_split[-1]
            italic_edit = "_"+ str(italic)+"_"
        re_time.append(italic_edit)
        final_time = " ".join(str(i) for i in re_time) 

        await interaction.response.send_message(f' **【Meeting Announcement】**\n> _Time_: {final_time}\n\
                                                > _Channel_: <#{final_channel_id}>\
                                                \n-----------------------------\n{final_result}', ephemeral=False)

class Modal_1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_1(bot))
