import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime
import asyncio
import time
import random

class Economy:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Cog Economy is working!")

    async def on_message(self, message):
        with open("userdata.json", "r") as f:
            users = json.load(f)

            if message.author.bot:
                return
            if message.channel.is_private:
                return
            if message.server.id == "264445053596991498":
                return
            else:
                await self.update_data(users, message.author)
                number = random.randint(5, 15)
                await self.add_experience(users, message.author, number)
                await self.lvl_up(users, message.author, message.channel)

            with open("userdata.json", "w") as f:
                json.dump(users, f)

    async def update_data(self, users, user):
        if not user.id + "-" in users:
            users[user.id + "-"] = {}
            users[user.id + "-"]["Xp"] = 0
            users[user.id + "-"]["Coins"] = 0
            users[user.id + "-"]["lvl"] = 1
            users[user.id + "-"]["last_message"] = 0


    async def add_experience(self, users, user, exp):
        if time.time() - users[user.id + "-"]["last_message"] > 60:
            users[user.id + "-"]["Xp"] += exp
            users[user.id + "-"]["last_message"] = time.time()
        else:
            return

    async def lvl_up(self, users, user, channel):
        experience = users[user.id + "-"]["Xp"]
        lvl_start = users[user.id + "-"]["lvl"]
        lvl_end = int(experience ** (1 / 4))


        if lvl_start < lvl_end:
             embed = discord.Embed(description=":tada: **{0}** Is now level **{1}** :tada:".format(user.mention, lvl_end), color=0x0d00f9)
             embed.set_author(name="Level Up!", icon_url=user.avatar_url)
             await self.bot.send_message(channel, embed=embed)
             users[user.id + "-"]["lvl"] = lvl_end

    @commands.command(pass_context=True)
    async def level(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    with open("userdata.json", "r") as f:
                        data = json.load(f)
                        author = ctx.message.author
                        lvl = data[author.id + "-"]["lvl"]
                        author = ctx.message.author.mention
                        embed = discord.Embed(description="**{0}** Is level **{1}**".format(author, lvl), color=0x0d00f9)
                        embed.set_author(name="Level", icon_url=ctx.message.author.avatar_url)
                        lvlupmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(lvlupmsg)

    @commands.command(pass_context=True, aliases=["Xp", "XP"])
    async def xp(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    with open("userdata.json", "r") as f:
                        data = json.load(f)
                        author = ctx.message.author
                        Xp = data[author.id + "-"]["Xp"]
                        author = ctx.message.author.mention
                        embed = discord.Embed(description="**{0}** Has **{1}** XP".format(author, Xp), color=0x0d00f9)
                        embed.set_author(name="XP", icon_url=ctx.message.author.avatar_url)
                        xpmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(xpmsg)

    @commands.command(pass_context=True, aliases=["bal", "Balance"])
    async def balance(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    with open("userdata.json", "r") as f:
                        data = json.load(f)
                    author = ctx.message.author
                    Coins = data[author.id + "-"]["Coins"]
                    author = ctx.message.author.mention
                    embed = discord.Embed(description="**{0}** Has **{1}** coins".format(author, Coins), color=0x0d00f9)
                    embed.set_author(name="Balance", icon_url=ctx.message.author.avatar_url)
                    balmsg = await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(10)
                    await self.bot.delete_message(balmsg)

#TEST-TEST-TEST-TEST

    

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def daily(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    with open("userdata.json", "r") as f:
                        data = json.load(f)

                    author = ctx.message.author
                    data[author.id + "-"]["Coins"] += 50
                    with open("userdata.json", "w") as f:
                        json.dump(data, f)
                    embed = discord.Embed(description="**{}** Has claimed their daily reward of **50** coins".format(ctx.message.author), color=0x0d00f9)
                    embed.set_author(name="Daily", icon_url=ctx.message.author.avatar_url)
                    dailymsg = await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(10)
                    await self.bot.delete_message(dailymsg)

    @daily.error
    async def daily_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.CommandOnCooldown):
                        embed = discord.Embed(description="**{0}** You can use this command again in **{1:.2f}**".format(ctx.message.author, error.retry_after), color=0x0d00f9)
                        embed.set_author(name="Daily", icon_url=ctx.message.author.avatar_url)
                        dailymsger = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(dailymsger)

def setup(bot):
    bot.add_cog(Economy(bot))
