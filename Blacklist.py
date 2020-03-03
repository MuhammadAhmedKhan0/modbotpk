import discord
from discord.ext import commands
import asyncio
import json

class Blacklist:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Cog Blacklist is working!")

    @commands.group(invoke_without_command=True)
    async def blacklist(ctx):
        await bot.say("Blakclist")

    @blacklist.command(pass_context=True)
    async def add(self, ctx, id):
        if ctx.message.author.bot:
            return
        else:
            if ctx.message.author.id == "231821149015769089":
                with open("blacklist.json", "r") as f:
                    user = json.load(f)

                user[id] = 0
                embed = discord.Embed(title="Blacklist Update",
                                      description="Bot owner **{0}** has **blacklisted** a user with the id **{1}**!".format(
                                          ctx.message.author, id), color=0x0d00f9)
                embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRequested by: ' + ctx.message.author.name)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                chenable = await self.bot.say(embed=embed)
                with open("blacklist.json", "w") as f:
                    json.dump(user, f)

                user = await self.bot.get_user_info(user_id=id)
                embed = discord.Embed(title="Blacklist Update",
                                      description="You have been blacklisted, That means that the bot will ignore you!", color=0x0d00f9)
                await self.bot.send_message(user, embed=embed)

            else:
                await self.bot.say("You cant do that!")

    @blacklist.command(pass_context=True)
    async def remove(self, ctx, id):
        if ctx.message.author.bot:
            return
        else:
            if ctx.message.author.id == "231821149015769089":
                with open("blacklist.json", "r") as f:
                    user = json.load(f)

                del user[id]
                embed = discord.Embed(title="Blacklist Update",
                                      description="Bot owner **{0}** has **removed** a user with the id **{1}** from the **blacklist**!".format(
                                          ctx.message.author, id), color=0x0d00f9)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                chenable = await self.bot.say(embed=embed)
                with open("blacklist.json", "w") as f:
                    json.dump(user, f)

                user = await self.bot.get_user_info(user_id=id)
                embed = discord.Embed(title="Blacklist Update",
                                      description="You have been removed from blacklist!", color=0x0d00f9)
                await self.bot.send_message(user, embed=embed)

            else:
                await self.bot.say("You cant do that!")


def setup(bot):
    bot.add_cog(Blacklist(bot))
