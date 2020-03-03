import discord
from discord.ext import commands
import asyncio
import re
import json

class AdBlock:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Cog AdBlock is ready!")

    @commands.command(pass_context=True)
    async def enablelinks(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open("LinksS.json", "r") as f:
                            channels = json.load(f)

                        channel = ctx.message.channel
                        if str(ctx.message.channel.id) in channels:
                            embed = discord.Embed(title="AdBlock Error", description="**{0}** Links are already **enabled** in this channel".format(ctx.message.author), color=0x0d00f9)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            linkenable = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(linkenable)
                            return
                        else:
                            channels[channel.id] = 0
                            embed=discord.Embed(title="AdBlock Update", description="Administrator **{0}** Has **enabled** links in this channel!".format(ctx.message.author), color=0x0d00f9)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            linkdisable = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            with open("LinksS.json", "w") as f:
                                json.dump(channels, f)
                    else:
                        await self.bot.say("You cant do that")

    @commands.command(pass_context=True)
    async def disablelinks(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open("LinksS.json", "r") as f:
                            channels = json.load(f)
                            channel = ctx.message.channel
                            if not str(ctx.message.channel.id) in channels:
                                embed = discord.Embed(title="AdBlock Error", description="**{0}** Links are already **disabled** in this channel".format(ctx.message.author), color=0x0d00f9)
                                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                                linkdisable = await self.bot.say(embed=embed)
                                await asyncio.sleep(1)
                                await self.bot.delete_message(ctx.message)
                                await asyncio.sleep(10)
                                await self.bot.delete_message(linkdisable)
                                return
                            else:
                                del channels[channel.id]

                                embed = discord.Embed(title="AdBlock Update", description="Administrator **{0}** Has **disabled** links in this channel!".format(ctx.message.author), color=0x0d00f9)
                                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                                chenable = await self.bot.say(embed=embed)
                                await asyncio.sleep(1)
                                await self.bot.delete_message(ctx.message)
                                with open("LinksS.json", "w") as f:
                                    json.dump(channels, f)

                    else:
                        await self.bot.say("You cant do that!")

    @commands.command(pass_context=True)
    async def enableinvites(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open("InvitesS.json", "r") as f:
                            channels = json.load(f)

                        channel = ctx.message.channel
                        if str(ctx.message.channel.id) in channels:
                            embed = discord.Embed(title="AdBlock Error", description="**{0}** Invites are already **enabled** in this channel".format(ctx.message.author), color=0x0d00f9)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            linkenable = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(linkenable)
                            return
                        else:
                            channels[channel.id] = 0
                            embed=discord.Embed(title="AdBlock Update", description="Administrator **{0}** Has **enabled** invites in this channel!".format(ctx.message.author), color=0x0d00f9)
                            embed.set_thumbnail(url=ctx.message.author.avatar_url)
                            linkdisable = await self.bot.say(embed=embed)
                            await asyncio.sleep(1)
                            await self.bot.delete_message(ctx.message)
                            with open("InvitesS.json", "w") as f:
                                json.dump(channels, f)
                    else:
                        await self.bot.say("You cant do that")

    @commands.command(pass_context=True)
    async def disableinvites(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open("InvitesS.json", "r") as f:
                            channels = json.load(f)
                            channel = ctx.message.channel
                            if not str(ctx.message.channel.id) in channels:
                                embed = discord.Embed(title="AdBlock Error", description="**{0}** Invites are already **disabled** in this channel".format(ctx.message.author), color=0x0d00f9)
                                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                                invitedisable = await self.bot.say(embed=embed)
                                await asyncio.sleep(1)
                                await self.bot.delete_message(ctx.message)
                                await asyncio.sleep(10)
                                await self.bot.delete_message(invitedisable)
                                return
                            else:
                                del channels[channel.id]

                                embed = discord.Embed(title="AdBlock Update", description="Administrator **{0}** Has **disabled** links in this channel!".format(ctx.message.author), color=0x0d00f9)
                                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                                chenable = await self.bot.say(embed=embed)
                                await asyncio.sleep(1)
                                await self.bot.delete_message(ctx.message)
                                with open("InvitesS.json", "w") as f:
                                    json.dump(channels, f)
                    else:
                        await self.bot.say("You cant do that!")





    async def on_message(self, message):
        if message.author.server_permissions.manage_messages:
            return
        else:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
            invite = re.findall('discord?.gg/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
            invites = re.findall('http[s]?://discord?.gg/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
            discio = re.findall('http[s]?://discord?.io/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content.lower())
            if invite or invites or discio:
                with open("InvitesS.json", "r") as f:
                    channels = json.load(f)
                    if str(message.channel.id) in channels:
                        return
                    else:
                        await self.bot.delete_message(message)
                        embed = discord.Embed(title="AdBlock Invites",
                                              description="**{0}** Sorry but you cant send invites in this channel".format(
                                                  message.author), color=0x0d00f9)
                        embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMessage deleted - ' + message.author.name)
                        embed.set_thumbnail(url=message.author.avatar_url)
                        invitedisable = await self.bot.send_message(message.channel, embed=embed)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(invitedisable)
            else:
                if urls:
                    with open("LinksS.json", "r") as f:
                        channels = json.load(f)
                        if str(message.channel.id) in channels:
                            return
                        else:
                            await self.bot.delete_message(message)
                            embed = discord.Embed(title="AdBlock Links",
                                                  description="**{0}** Sorry but you cant send links in this channel".format(
                                                      message.author), color=0x0d00f9)
                            embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMessage deleted - ' + message.author.name)
                            embed.set_thumbnail(url=message.author.avatar_url)
                            invitedisable = await self.bot.send_message(message.channel, embed=embed)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(invitedisable)
                else:
                    return
                return

    async def on_message_edit(self, before, after):
        if after.author.server_permissions.manage_messages:
            return
        else:
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', after.content.lower())
            invite = re.findall('discord?.gg/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', after.content.lower())
            invites = re.findall('http[s]?://discord?.gg/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', after.content.lower())
            discio = re.findall('http[s]?://discord?.io/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', after.content.lower())
            if invite or invites or discio:
                with open("InvitesS.json", "r") as f:
                    channels = json.load(f)
                    if str(after.channel.id) in channels:
                        return
                    else:
                        await self.bot.delete_message(after)
                        embed = discord.Embed(title="AdBlock Invites",
                                              description="**{0}** Sorry but you cant send invites in this channel".format(
                                                  after.author), color=0x0d00f9)
                        embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMessage deleted - ' + after.author.name)
                        embed.set_thumbnail(url=after.author.avatar_url)
                        invitedisable = await self.bot.send_message(after.channel, embed=embed)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(invitedisable)
            else:
                if urls:
                    with open("LinksS.json", "r") as f:
                        channels = json.load(f)
                        if str(after.channel.id) in channels:
                            return
                        else:
                            await self.bot.delete_message(after)
                            embed = discord.Embed(title="AdBlock Links",
                                                  description="**{0}** Sorry but you cant send links in this channel".format(
                                                      after.author), color=0x0d00f9)
                            embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMessage deleted - ' + after.author.name)
                            embed.set_thumbnail(url=after.author.avatar_url)
                            invitedisable = await self.bot.send_message(after.channel, embed=embed)
                            await asyncio.sleep(10)
                            await self.bot.delete_message(invitedisable)
                else:
                    return
                return
      #  await self.bot.send_message(after.channel, "test sucessefull")



def setup(bot):
    bot.add_cog(AdBlock(bot))
