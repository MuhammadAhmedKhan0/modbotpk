import discord
from discord.ext import commands
import asyncio
import datetime
from enum import Enum
from random import choice, randint, sample
import random
import json

class RPS(Enum):
    rock = "\N{MOYAI}"
    paper = "\N{PAGE FACING UP}"
    scissors = "\N{BLACK SCISSORS}"


class RPSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPS.rock
        elif argument == "paper":
            self.choice = RPS.paper
        elif argument == "scissors":
            self.choice = RPS.scissors
        else:
            return

class Fun:
    def __init__(self, bot):
        self.bot = bot
                            
    async def on_ready(self):
        print("Cog Fun is working!")

    @commands.command(pass_context=True)
    async def iq(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    number = random.randint(1,250)
                    e = discord.Embed(title="IQ", description="Calculating iq...", color=0x0d00f9)
                    e1 = await self.bot.say(embed=e)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(3)
                    e2 = discord.Embed(title="IQ", description=":bulb: {} Your iq is {} :bulb: ".format(member.mention, number), color=0x0d00f9)
                    await self.bot.edit_message(e1, embed=e2)

    @commands.command(pass_context=True)
    async def howgay(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    number = random.randint(1,100)
                    e = discord.Embed(title="Howgay", description="Calculating", color=0x0d00f9)
                    e1 = await self.bot.say(embed=e)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(3)
                    e2 = discord.Embed(title="Howgay", description=":gay_pride_flag: {} You are {}% gay :gay_pride_flag:".format(member.mention, number), color=0x0d00f9)
                    await self.bot.edit_message(e1, embed=e2)

    @commands.command(pass_context=True)
    async def slap(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    gifs = ["https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993", "https://media1.tenor.com/images/f9f121a46229ea904209a07cae362b3e/tenor.gif?itemid=7859254", "https://media.tenor.com/images/47a6be1fbc1c40c3a55c0e2c8b725603/tenor.gif", "https://media.tenor.com/images/47a6be1fbc1c40c3a55c0e2c8b725603/tenor.gif", "https://media0.giphy.com/media/j2h2sB2WkbH6U/giphy.gif?cid=790b76115d38412f6d744a4777a4fdb9&rid=giphy.gif"]
                    embed = discord.Embed(description="{} Just slapped {}".format(ctx.message.author.mention, member.mention), color=0x0d00f9)
                    embed.set_image(url=random.choice(gifs))
                    embed.set_footer(text='Why did you do this' + ctx.message.author.name)
                    await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    gifs = ["https://media0.giphy.com/media/od5H3PmEG5EVq/giphy.gif?cid=790b76115d38402d674936794d046da7&rid=giphy.gif", "https://media0.giphy.com/media/wnsgren9NtITS/giphy.gif?cid=790b76115d38403e7a58424241d17832&rid=giphy.gif", "https://media3.giphy.com/media/JglVCaB0axZ4Y/giphy.gif?cid=790b76115d38402d674936794d046da7&rid=giphy.gif", "https://media3.giphy.com/media/HaC1WdpkL3W00/giphy.gif?cid=790b76115d38402d674936794d046da7&rid=giphy.gif", "https://media0.giphy.com/media/DjczAlIcyK1Co/giphy.gif?cid=790b76115d38410949634b3536764555&rid=giphy.gif"]
                    embed = discord.Embed(description=":blue_heart: {} Just hugged {} :blue_heart:".format(ctx.message.author.mention, member.mention), color=0x0d00f9)
                    embed.set_image(url=random.choice(gifs))
                    embed.set_footer(text='You`re so sweet ' + ctx.message.author.name)
                    await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)


    @commands.command(pass_context=True)
    async def kiss(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    gifs = ["https://media.tenor.com/images/26aaa1494b424854824019523c7ba631/tenor.gif", "https://media.tenor.com/images/dd777838018ab9e97c45ba34596bb8de/tenor.gif", "https://media.tenor.com/images/07b5bea3e050f380c6742500c1f1f7db/tenor.gif", "https://media.tenor.com/images/4b75a7e318cb515156bb7bfe5b3bbe6f/tenor.gif", "https://media.tenor.com/images/1f9175e76488ebf226de305279151752/tenor.gif", "https://media.tenor.com/images/48963a8342fecf77d8eabfd2ab2e75c1/tenor.gif"]
                    embed = discord.Embed(description=":blue_heart: {} Just kissed {} :blue_heart:".format(ctx.message.author.mention, member.mention), color=0x0d00f9)
                    embed.set_image(url=random.choice(gifs))
                    embed.set_footer(text='You`re so sweet ' + ctx.message.author.name)
                    await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def rps(self, ctx, your_choice: RPSParser):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    """Play rock paper scissors"""
                    player_choice = your_choice.choice
                    tb_choice = choice((RPS.rock, RPS.paper, RPS.scissors))
                    cond = {
                            (RPS.rock,     RPS.paper): False,
                            (RPS.rock,     RPS.scissors): True,
                            (RPS.paper,    RPS.rock): True,
                            (RPS.paper,    RPS.scissors): False,
                            (RPS.scissors, RPS.rock): False,
                            (RPS.scissors, RPS.paper): True
                           }

                    if tb_choice == player_choice:
                        outcome = None  # Tie
                    else:
                        outcome = cond[(player_choice, tb_choice)]

                        if outcome is True:
                            await self.bot.say("{0} You win {1}!".format(tb_choice.value, ctx.message.author.mention))
                        elif outcome is False:
                            await self.bot.say("{0} You lose {1}!".format(tb_choice.value, ctx.message.author.mention))
                        else:
                            await self.bot.say("{0} We're square {1}!".format(tb_choice.value, ctx.message.author.mention))

    @commands.command(pass_context=True, aliases=["8ball"])
    async def ask(self, ctx, *, question=None):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    """Ask a question"""
                    question = question.lower()

                    if question.startswith("should"):
                        responses = ("Yes", "No", "Definitely", "Sure", "Of course", "Maybe",
                                     "Probably" "Definitely not", "No way", "Please don't",
                                     "Go ahead!", "I mean, if you want to, sure", "Sure, but be careful",
                                     "That's probably not a good idea")
                    elif question.startswith("where"):
                        fast_food_chains = ("McDonald's", "Wendy's", "Burger King", "A&W", "KFC", "Taco Bell")
                        responses = ("Just over there", "In your closet", "Probably hiding from you",
                                     "At the nearest {}".format(choice(fast_food_chains)),
                                     "Right behind you", "At the store", "Just a few blocks away",
                                     "Nowhere near here")
                    elif question.startswith("when"):
                        time_units = ("years", "months", "days", "hours", "minutes", "seconds")
                        responses = ("In a few hours", "Sometime this month", "When pigs fly",
                                     "Not anythime soon, that's for sure", "By the end of the week",
                                     "Let's hope that never happens", "I am genuinely unsure",
                                     "Soon", "No idea, but be sure to tell me when it does",
                                     "In a dog's age", "I don't know, but hopefully it's in my lifetime",
                                     "In {0} {1}".format(randint(1, 101), choice(time_units)))
                    else:
                        responses = ("Yes", "No", "Definitely", "Sure", "Of course", "Maybe",
                                     "Probably", "Most likely", "Definitely not", "No way",
                                     "I hope not", "Better be", "I don't think so")

                        if question is None:
                            await self.bot.say("You forgot to ask a question")
                        else:
                            await self.bot.say(choice(responses))
        """elif question.startswith("who"):
            html = await self.bot.fetch(ctx.session, "https://www.randomlists.com/random-celebrities?a", timeout=15,
                               return_type='text')
            soup = BeautifulSoup(html, "html.parser")
            tags = soup.find_all(class_="crux")
            celebrities = []
            for tag in tags:
                celebrities.append(tag.text)
            responses = celebrities
        elif question.startswith(("what movie should", "what film should")):
            html = await self.bot.fetch(ctx.session, "https://www.randomlists.com/random-movies?a", timeout=15,
                               return_type='text')
            soup = BeautifulSoup(html, "html.parser")
            tags = soup.find_all(class_="support")
            movies = []
            for tag in tags:
                movies.append(tag.text)
            responses = movies
        elif question.startswith(("what game should", "what video game should", "what videogame should")):
            html = await self.bot.fetch(ctx.session, "https://www.randomlists.com/random-video-games?a", timeout=15,
                               return_type='text')
            soup = BeautifulSoup(html, "html.parser")
            tags = soup.find_all(class_="support")
            games = []
            for tag in tags:
                games.append(tag.text)
            responses = games
        else:
            responses = ("Yes", "No", "Definitely", "Sure", "Of course", "Maybe",
                         "Probably", "Most likely", "Definitely not", "No way",
                         "I hope not", "Better be", "I don't think so")

        if question is None:
            await self.bot.say("You forgot to ask a question")
        else:
            await self.bot.say(choice(responses))"""
         
#ERRORS ------------------------------------------------------------------

    @ask.error
    async def ask_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.CommandInvokeError):
                        embed = discord.Embed(title="Usage:", description='@aivo 8ball <question>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return

    @slap.error
    async def slap_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo slap <@member>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return

    @kiss.error
    async def kiss_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo kiss <@member>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return


    @hug.error
    async def hug_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo hug <@member>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return

    @iq.error
    async def iq_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        number = random.randint(1, 250)
                        e = discord.Embed(title="IQ", description="Calculating iq...", color=0x0d00f9)
                        e1 = await self.bot.say(embed=e)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(3)
                        e2 = discord.Embed(title="IQ", description=":bulb: {} Your iq is {} :bulb: ".format(ctx.message.author.mention, number), color=0x0d00f9)
                        await self.bot.edit_message(e1, embed=e2)
                        return
                    if isinstance(error, commands.errors.BadArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo iq <@member>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return
        

    @howgay.error
    async def howgay_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        number = random.randint(1, 100)
                        number = random.randint(1, 100)
                        e = discord.Embed(title="Howgay", description="Calculating", color=0x0d00f9)
                        e1 = await self.bot.say(embed=e)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(3)
                        e2 = discord.Embed(title="Howgay", description=":gay_pride_flag: {} You are {}% gay :gay_pride_flag:".format(ctx.message.author.mention, number), color=0x0d00f9)
                        await self.bot.edit_message(e1, embed=e2)
                        return
                    if isinstance(error, commands.errors.BadArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo howgay <@member>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return


    @rps.error
    async def rps_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo rps <rock, paper or scissors>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer( text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return
                    if isinstance(error, commands.errors.CommandOnCooldown):
                        embed = discord.Embed(title="Error:", description='You can use this command every 3 seconds, You need to wait {} more seconds to use this command'.format(error.retry_after), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        memeerror = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(memeerror)
                        return

def setup(bot):
    bot.add_cog(Fun(bot))
