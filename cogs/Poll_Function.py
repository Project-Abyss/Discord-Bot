import discord
from discord.ext import commands
import datetime
import asyncio

numbersIcon =("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")
class Poll_Function(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polls = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll_Function cog loaded.')

    @commands.command(name='單票制投票', brief="\tparameter: (Poll_Title) (Time_Limit) (Options)！\n\t\t\t\t\t *Time_Limit Unit is Minutes ")
    async def SingleAnswer(self, ctx, descriptionMessage: str, timeLimit: int, *options):
        if len(options) > 10:
            await ctx.channel.send("The maximum of options are 10!")
        else:
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", color=ctx.author.color, timestamp=datetime.datetime.today())
            emb.set_footer(text=f"Poll by {ctx.author.name}")
            fields = [("OPTIONS", "\n".join([f"{numbersIcon[idx]} {option}" for idx, option in enumerate(options)]), False)]
            for name, value, inline in fields:
                emb.add_field(name=name, value=value, inline=inline)

            msg = await ctx.channel.send(embed=emb)

            for numberEmoji in numbersIcon[:len(options)]:
                await msg.add_reaction(numberEmoji)

            self.polls.append((msg.channel.id, msg.id))

            timeLimit *= 60
            await asyncio.sleep(timeLimit)

            newmsg = await ctx.fetch_message(msg.id)
            reactionResult = []
            for reactNum in newmsg.reactions:
                choices = [choice async for choice in reactNum.users()]
                choices = len(choices)
                reactionResult.append(choices)

            resultIndex = [indx for indx, item in enumerate(reactionResult) if item == max(reactionResult)]
            result = []
            for indx in resultIndex:
                result.append(options[indx])
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", description=f"Result: {result}", color=ctx.author.color, timestamp=datetime.datetime.today())
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

    @commands.command(name='多票制投票', brief="\tparameter: (Poll_Title) (Time_Limit) (Options)！\n\t\t\t\t\t *Time_Limit Unit is Minutes ")
    async def MutiAnswer(self, ctx, descriptionMessage: str, timeLimit: int, *options):
        if len(options) > 10:
            await ctx.channel.send("The maximum of options are 10!")
        else:
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", color=ctx.author.color, timestamp=datetime.datetime.today())
            emb.set_footer(text=f"Poll by {ctx.author.name}")
            fields = [("OPTIONS", "\n".join([f"{numbersIcon[idx]} {option}" for idx, option in enumerate(options)]), False)]
            for name, value, inline in fields:
                emb.add_field(name=name, value=value, inline=inline)

            msg = await ctx.channel.send(embed=emb)

            for numberEmoji in numbersIcon[:len(options)]:
                await msg.add_reaction(numberEmoji)

            timeLimit *= 60
            await asyncio.sleep(timeLimit)

            newmsg = await ctx.fetch_message(msg.id)
            reactionResult = []
            for reactNum in newmsg.reactions:
                choices = [choice async for choice in reactNum.users()]
                choices = len(choices)
                reactionResult.append(choices)

            resultIndex = [indx for indx, item in enumerate(reactionResult) if item == max(reactionResult)]
            result = []
            for indx in resultIndex:
                result.append(options[indx])
            emb = discord.Embed(title=f" POLL: {descriptionMessage}", description=f"Result: {result}", color=ctx.author.color, timestamp=datetime.datetime.today())
            await newmsg.edit(embed=emb)

async def setup(bot):
    await bot.add_cog(Poll_Function(bot))
