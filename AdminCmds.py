import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import time
import json

class AdminCmds:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Cog AdminCmds is working!")

    @commands.command(pass_context = True)
    async def mute(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    role = discord.utils.get(member.server.roles, name='Muted')
                    user = member
                    if role in user.roles:
                        embed = discord.Embed(title="Error!", description="Hey **{0}** that user is already muted!".format(ctx.message.author), timestamp=ctx.message.timestamp, color=0x0d00f9)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        mutemsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(mutemsg)
                    else:
                        if ctx.message.author.server_permissions.kick_members:
                            role = discord.utils.get(member.server.roles, name='Muted')
                            await self.bot.add_roles(member, role)
                            embed=discord.Embed(title="User muted!", description="**{0}** Was muted by: **{1}**!".format(member, ctx.message.author), timestamp=ctx.message.timestamp, color=0x0d00f9)
                            embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            mutemsg = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                        else:
                            embed=discord.Embed(title="Access Denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), timestamp=ctx.message.timestamp, color=0x0d00f9)
                            embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                            embed.set_footer(
                            text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name),
                            icon_url=ctx.message.author.avatar_url)
                            mutemsgnoperm = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(mutemsgnoperm)

    @commands.command(pass_context=True)
    async def unmute(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    role = discord.utils.get(member.server.roles, name='Muted')
                    user = member
                    if not role in user.roles:
                        embed = discord.Embed(title="Error!", description="Hey **{0}** that user is not muted!".format(ctx.message.author), timestamp=ctx.message.timestamp, color=0x0d00f9)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        mutemsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(mutemsg)
                    else:
                        if ctx.message.author.server_permissions.kick_members:
                            role = discord.utils.get(member.server.roles, name='Muted')
                            await self.bot.remove_roles(member, role)
                            embed = discord.Embed(title="User unmuted!", description="**{0}** Was unmuted by: **{1}**!".format(member, ctx.message.author), color=0x0d00f9, timestamp=ctx.message.timestamp)
                            embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            unmutemsg = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                        else:
                            embed = discord.Embed(title="Access denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), color=0x0d00f9, timestamp=ctx.message.timestamp)
                            embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                            unmutenoperm = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(unmutenoperm)

    @commands.command(pass_context=True)
    async def kick(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.kick_members:
                        await self.bot.kick(member)
                        embed = discord.Embed(title="User has been kicked!", description="**{0}** was kicked from the server by **{1}**!".format(member, ctx.message.author), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        kickmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                    else:
                        embed=discord.Embed(title="Access denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), timestamp=ctx.message.timestamp, color=0x0d00f9)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        kicknoperm = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(kicknoperm)

    @commands.command(pass_context=True)
    async def ban(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.ban_members:
                        await self.bot.ban(member)
                        embed = discord.Embed(title="User has been banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        banmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                    else:
                        embed=discord.Embed(title="Access denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), timestamp=ctx.message.timestamp, color=0x0d00f9)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        bannoperm = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(bannoperm)

    @commands.command(pass_context=True)
    async def clear(self, ctx, number):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.manage_messages:
                        mgs = []  # Empty list to put all the messages in the log
                        number = int(number)  # Converting the amount of messages to delete to an integer
                        async for x in self.bot.logs_from(ctx.message.channel, limit=number):
                            mgs.append(x)
                        await self.bot.delete_messages(mgs)
                        embed = discord.Embed(title="Chat cleared!", description="**{0}** Has cleared {1} messages!".format(ctx.message.author, number), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        clearmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(clearmsg)
                    else:
                        embed = discord.Embed(title="Access denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        clearnoperm = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(clearnoperm)

    @commands.command(pass_context=True)
    async def say(self, ctx, *args):
        if ctx.message.author.id == "231821149015769089":
            mesg = ' '.join(args)
            await asyncio.sleep(0.1)
            await self.bot.delete_message(ctx.message)
            await self.bot.say(mesg)
        else:
            return

    @commands.command(pass_context = True)
    async def tempmute(self, ctx, member: discord.Member, duration: int):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.kick_members:
                        role = discord.utils.get(member.server.roles, name='Muted')
                        embed=discord.Embed(title="User muted!", description="**{0}** Was muted by: **{1}** for {} seconds!".format(member, ctx.message.author, duration), timestamp=ctx.message.timestamp, color=0x0d00f9)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        await self.bot.say(embed=embed)
                        await asyncio.sleep(duration)
                        await self.bot.remove_roles(member, role)
                        embed = discord.Embed(title="User unmuted!", description="**{0}** Has been unmuted after **{1}**!".format(member, duration), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        await self.bot.say(embed=embed)
                    else:
                        embed = discord.Embed(title="Access denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811 ".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def fban(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.ban_members:
                        embed = discord.Embed(title="User Has Been Banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0x0d00f9)
                        embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRequested by: ' + ctx.message.author.name)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        banmsg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                    else:
                        embed=discord.Embed(title="Access Denied!", description="{} You dont have the premmision to use this command :confused:".format(ctx.message.author.mention), color=0x0d00f9)
                        bannoperm = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(bannoperm)

 #ERRORS---ERRORS---ERRORS---ERRORS---ERRORS---ERRORS---ERRORS---ERRORS---ERRORS---ERRORS


    @kick.error
    async def kick_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo kick <mention>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        kicker = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(kicker)
                        return

    @ban.error
    async def ban_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo ban <mention>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        baner = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(baner)
                        return

    @fban.error
    async def fban_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo fban <mention>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        baner = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(baner)
                        return

    @mute.error
    async def mute_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo mute <mention>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter1 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(muter1)
                        return
                    if isinstance(error, commands.errors.CommandInvokeError):
                        embed = discord.Embed(title="ERROR:", description='You need to create a role called "Muted" to use this command or the bot doesent have the premission!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter3 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(muter3)
                        return
                    if isinstance(error, discord.errors.Forbidden):
                        embed = discord.Embed(title="ERROR:", description='I dont have the premission to do that!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter2 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(muter2)
                        return

    @unmute.error
    async def unmute_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo unmute <mention>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        unmuteer = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(unmuteer)
                        return
                    if isinstance(error, discord.errors.Forbidden):
                        embed = discord.Embed(title="ERROR:", description='I dont have the premission to do that!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        unmuteer2 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(unmuteer2)
                        return
                    if isinstance(error, commands.errors.CommandInvokeError):
                        embed = discord.Embed(title="ERROR:", description='You need to create a role called "Muted" to use this command or the bot doesent have the premission!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        unmuteer3 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(unmuteer3)
                        return

    @clear.error
    async def clear_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo clear <2-100>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        clearer = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(clearer)
                        return

    @tempmute.error
    async def tempmute_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="USAGE:", description="@Aivo tempmute <mention> <seconds>", color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer( text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter1 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(muter1)
                        return
                    if isinstance(error, commands.errors.CommandInvokeError):
                        embed = discord.Embed(title="ERROR:", description='You need to create a role called "Muted" to use this command or the bot doesent have the premission!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter3 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(muter3)
                        return
                    if isinstance(error, discord.errors.Forbidden):
                        embed = discord.Embed(title="ERROR:", description='I dont have the premission to do that!', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        muter2 = await self.bot.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(muter2)
                        return

def setup(bot):
    bot.add_cog(AdminCmds(bot))
