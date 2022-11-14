import discord
from discord.ext import commands

class template_5(discord.ui.Modal, title ='對內課程公告'):
    course_time = discord.ui.TextInput(label = '時間', placeholder='2022/11/16 18:30 ~ 20:30')
    course_location = discoimport discord
from discord.ext import commands

class template_4(discord.ui.Modal, title ='對外課程公告'):
    course_time = discord.ui.TextInput(label = '時間', placeholder='2022/11/16 18:30 ~ 20:30')
    course_location = discord.ui.TextInput(label = '地點')
    course_title = discord.ui.TextInput(label = '課程名稱')
    course_lecturer = discord.ui.TextInput(label = '課程講師', placeholder='請填寫帳號全名')
    course_slides_note = discord.ui.TextInput(label = '簡報筆記', placeholder='s <url>\nn <url>',style = discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        slide_and_note =str(self.course_slides_note)
        result = []
        n = 0
        s = 0
        slide_split = slide_and_note.split("\n")
        for i in range(len(slide_split)):
            slide_split_2 = slide_split[i].split(' ')
            for j in range(len(slide_split_2)):
                if slide_split_2[0] == 's' and slide_split_2[1] != "":
                    slide_split_new = str(slide_split_2[1])
                    slide_split_2[j] =  '     ．簡報 －' + slide_split_new +'\n'
                    result.append(slide_split_2[j])
                    s = s + 1
                elif slide_split_2[0] == 'n' and slide_split_2[1] != "":
                    slide_split_new = str(slide_split_2[1])
                    slide_split_2[j] = '     ．筆記 －' + slide_split_new + '\n'
                    result.append(slide_split_2[j])
                    n = n + 1

        if s == 0:
            slide_split_new = str(slide_split_2[1])
            slide_split_2[j] =  '     ．簡報 － <待補>\n'
            result.append(slide_split_2[j])
        if n == 0:
            slide_split_new = str(slide_split_2[1])
            slide_split_2[j] =  '     ．筆記 － <待補>\n'
            result.append(slide_split_2[j])                    
        final_result = "".join(result)

        guild = interaction.guild
        for member in guild.members:
            if str(self.course_lecturer) == member.name:
                final_member_id = member.id
        await interaction.response.send_message(f' **【對外課程公告】**\n> 時間: {self.course_time}\
                                                \n> 地點: {self.course_location}\
                                                \n------------------------------------------------------------\
                                                \n．課程名稱: {self.course_title}\
                                                \n．課程講師: <@{final_member_id}>\
                                                \n．課程教材:\
                                                \n{final_result}', ephemeral=False)

class Modal_4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Modal_4(bot))rd.ui.TextInput(label = '地點')
    course_title = discord.ui.TextInput(label = '課程名稱')
    course_lecturer = discord.ui.TextInput(label = '課程講師', placeholder='請填寫帳號全名')
    course_teachingMaterial = discord.ui.TextInput(label = '課程教材')
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        for member in guild.members:
            if str(self.course_lecturer) == member.name:
                final_member_id = member.id  
        await interaction.response.send_message(f' **【對內課程公告】**\n> 時間: {self.course_time}\
                                                \n> 地點: {self.course_location}\
                                                \n------------------------------------------------------------\
                                                \n．課程名稱: {self.course_title}\
                                                \n．課程講師: <@{final_member_id}>\
                                                \n．課程教材:\
                                                \n\t．{self.course_teachingMaterial}\
                                                \n(如有要請假的請留言回覆告知)', ephemeral=False)
        member = await interaction.original_response()
        mem_data = str(member)
        result = []
        id_split = mem_data.split("=")
        for i in range(len(id_split)):
            id_split_2 = id_split[i].split(' ')
            for j in range(len(id_split_2)):
                if id_split_2[j] == 'channel':
                    # print (id_split_2[0])
                    result.append(id_split_2[0])
        self.final_result = str("".join(result))

class who_is_the_lucky_guy(discord.ui.Modal, title ='This 15 Speech'):
    fifteen_speech = discord.ui.TextInput(label = '幸運兒', placeholder='請填寫帳號全名')
    async def on_submit(self, interaction: discord.Interaction):  
        guild = interaction.guild
        for member in guild.members:
            if str(self.fifteen_speech) == member.name:
                self.final_member_id = member.id
        await interaction.response.send_message(f'> This 15 Speech: <@{self.final_member_id}>', ephemeral=False, delete_after=5)

class Modal_5(commands.Cog, template_5, who_is_the_lucky_guy):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "This 15 Speech" in message.content:
            self.channel_id = template_5.final_result
            self.lucky_guy = who_is_the_lucky_guy.final_member_id

            guild =self.bot.guild
            for member in guild.members:
                if str(self.lucky_guy) == member.name:
                    self.final_member = member.id

            message_id = self.channel_id
            await message.create_thread(name = "【對內課程公告】", auto_archive_duration=60, slowmode_delay=None, reason=None)
            thread = message.channel.get_thread(message_id)
            await thread.send(f"> This 15 Speech: <@{self.final_member}>")    
async def setup(bot):
    await bot.add_cog(Modal_5(bot))
