import discord
from discord.ext import commands
from datetime import datetime
import asyncio

numbersIcon =("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")

class PollResult:
    def __init__(self, optionDescription, optionPollResult):
        self.optionDescription = optionDescription
        self.optionPollResult = optionPollResult
    def __repr__(self) -> str:
        return self.optionDescription + ", " + str(self.optionPollResult)

class Poll_Function(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polls = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll_Function cog loaded.')

    @commands.command(name='SingleAnswer', brief="\n單票制投票\n【範例：SingleAnswer 投票標題 截止日期 截止時刻 選項】")
    async def SingleAnswer(self, ctx, descriptionMessage: str, dateLimit: str, timeLimit: str, *options):
        if len(options) > 10:
            await ctx.channel.send("The maximum of options are 10!")
        else:
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", color=ctx.author.color, timestamp=datetime.today())
            emb.set_footer(text=f"Poll by {ctx.author.name}")
            fields = [("OPTIONS", "\n".join([f"{numbersIcon[idx]} {option}" for idx, option in enumerate(options)]), False)]
            for name, value, inline in fields:
                emb.add_field(name=name, value=value, inline=inline)

            msg = await ctx.channel.send(embed=emb)

            for numberEmoji in numbersIcon[:len(options)]:
                await msg.add_reaction(numberEmoji)

            self.polls.append((msg.channel.id, msg.id))

            dateLimit = datetime.strptime(dateLimit, "%Y-%m-%d")
            timeLimit = datetime.strptime(timeLimit, "%H:%M:%S")
            todayDateAndTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            todayDateAndTime = str(todayDateAndTime).split()
            todayDate = datetime.strptime(todayDateAndTime[0], "%Y-%m-%d")
            todayTime = datetime.strptime(todayDateAndTime[1], "%H:%M:%S")
            dateDelta = dateLimit - todayDate
            timedelta = timeLimit - todayTime
            timeUntilTheEndOfThePoll = (dateDelta.days*24*60*60) + (timedelta.seconds)
            if timeUntilTheEndOfThePoll > 0:
                await asyncio.sleep(timeUntilTheEndOfThePoll)
            else:
                await ctx.channel.send("You can not poll in past!")

            newmsg = await ctx.fetch_message(msg.id)
            reactionResult = []
            index = 0
            for reactNum in newmsg.reactions:
                choices = [choice async for choice in reactNum.users()]
                choices = len(choices)
                optionTitle = str(options[index])
                reactionResult.append(PollResult(optionTitle, choices))
                if index != len(options):
                    index += 1
            reactionResult.sort(key=lambda x: x.optionPollResult, reverse=True)

            singlePollResult = []
            for item in reactionResult: 
                if item.optionPollResult == reactionResult[0].optionPollResult:
                    singlePollResult.append(item.optionDescription)
            singlePollResult = " ".join(str(i) for i in singlePollResult)
            
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", description=f"最高票數：{singlePollResult}", color=ctx.author.color, timestamp=datetime.today())
            await newmsg.edit(embed=emb)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id in (poll[1] for poll in self.polls):
            channel = await self.bot.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            for reaction in message.reactions:
                users = [user async for user in reaction.users()]
                if(not payload.member.bot and payload.member in users and reaction.emoji != payload.emoji.name):
                    await message.remove_reaction(reaction.emoji, payload.member)

    @commands.command(name='MultiAnswer', brief="\n多票制投票\n【範例：MultiAnswer 投票標題 截止日期 截止時刻 選項】")
    async def MultiAnswer(self, ctx, descriptionMessage: str, dateLimit: str, timeLimit: str, *options):
        if len(options) > 10:
            await ctx.channel.send("The maximum of options are 10!")
        else:
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", color=ctx.author.color, timestamp=datetime.today())
            emb.set_footer(text=f"Poll by {ctx.author.name}")
            fields = [("OPTIONS", "\n".join([f"{numbersIcon[idx]} {option}" for idx, option in enumerate(options)]), False)]
            for name, value, inline in fields:
                emb.add_field(name=name, value=value, inline=inline)

            msg = await ctx.channel.send(embed=emb)

            for numberEmoji in numbersIcon[:len(options)]:
                await msg.add_reaction(numberEmoji)

            dateLimit = datetime.strptime(dateLimit, "%Y-%m-%d")
            timeLimit = datetime.strptime(timeLimit, "%H:%M:%S")
            todayDateAndTime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            todayDateAndTime = str(todayDateAndTime).split()
            todayDate = datetime.strptime(todayDateAndTime[0], "%Y-%m-%d")
            todayTime = datetime.strptime(todayDateAndTime[1], "%H:%M:%S")
            dateDelta = dateLimit - todayDate
            timedelta = timeLimit - todayTime
            timeUntilTheEndOfThePoll = (dateDelta.days*24*60*60) + (timedelta.seconds)
            if timeUntilTheEndOfThePoll > 0:
                await asyncio.sleep(timeUntilTheEndOfThePoll)
            else:
                await ctx.channel.send("You can not poll in past!")

            newmsg = await ctx.fetch_message(msg.id)
            reactionResult = []
            index = 0
            for reactNum in newmsg.reactions:
                choices = [choice async for choice in reactNum.users()]
                choices = len(choices) - 1
                optionTitle = str(options[index])
                reactionResult.append(PollResult(optionTitle, choices))
                if index != len(options):
                    index += 1
            reactionResult.sort(key=lambda x: x.optionPollResult, reverse=True)

            await ctx.channel.send(f"> **POLL: {descriptionMessage}**\n> 票數排行榜\n> -----------\n")
            pollResultRanking = 0
            for pollResultRanking in range(len(options)):
                await ctx.channel.send(f"> ❖ 第 {pollResultRanking+1} 名｜" 
                                       + "**" + str(reactionResult[pollResultRanking].optionDescription) + "**｜" 
                                       + str(reactionResult[pollResultRanking].optionPollResult) + " 票\n")

async def setup(bot):
    await bot.add_cog(Poll_Function(bot))
