import discord
from discord.ext import commands
import asyncio
import random
import aiohttp
import json

class Misc:
    def __init__(self, bot):
        self.bot = bot
                            
    async def on_ready(self):
        print("Cog Misc is working!")
          
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    t = await self.bot.say('Pong!, Is this even working?')
                    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
                    await self.bot.edit_message(t, new_content=':ping_pong: **Pong!** Took: {}ms'.format(int(ms)))
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(10)
                    await self.bot.delete_message(t)
        
    @commands.command(pass_context=True)
    async def avatar(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    avatar = member.avatar_url
                    embed = discord.Embed(description="Avatar of **{}**".format(member), color=0x0d00f9)
                    embed.set_image(url=avatar)
                    avmsg = await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)

                       #member.avatar_url

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    server = ctx.message.server
                    roles = [x.name for x in server.role_hierarchy]
                    role_length = len(roles)

                    if role_length > 50:
                        roles = roles[:50]
                        roles.append('>>>> [50/%s] Roles'%len(roles))

                    roles = ', '.join(roles);
                    channelz = len(server.channels);
                    time = str(server.created_at); time = time.split(' '); time= time[0];
                    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = 0x0d00f9);
                    join.set_thumbnail(url = server.icon_url);
                    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
                    join.add_field(name = '__ID__', value = str(server.id))
                    join.add_field(name = '__Member Count__', value = str(server.member_count));
                    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
                    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
                    join.set_footer(text ='Created: %s'%time);

                    return await self.bot.say(embed = join);

    @commands.command(pass_context=True, aliases=["dict", "urbandict", "definition", "dictionary"])
    async def urban(self, ctx, *, search_terms : str):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    """Urban Dictionary search"""
                    search_terms = search_terms.split(" ")
                    search_terms = "+".join(search_terms)
                    search = "http://api.urbandictionary.com/v0/define?term=" + search_terms
                    try:
                        async with aiohttp.get(search) as r:
                            result = await r.json()
                            if result["list"] != []:
                                definition = result['list'][0]['definition']
                                example = result['list'][0]['example']
                                embed = discord.Embed(title="UrbanDict:", description="**Definition:** " + definition + "\n\n" + "**Example:** " + example , color=0x0d00f9, timestamp=ctx.message.timestamp)
                                embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                                msg = await self.bot.say(embed=embed)
                                await asyncio.sleep(1)
                                await self.bot.delete_message(ctx.message)
                            else:
                                await self.bot.say("Your search terms gave no results.")
                    except:
                        await self.bot.say("Error.")

    @commands.command(pass_context=True)
    async def lmgtfy(self, ctx, *text):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    """Creates a lmgtfy link"""
                    if text == ():
                        embed = discord.Embed(title="Usage:", description='@aivo lmgtfy <text>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)
                        return
                    text = "+".join(text)
                    await self.bot.say("http://lmgtfy.com/?q=" + text)

#ERRORS ------------------------------------------------------------------

    @avatar.error
    async def avatar_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        avatar = ctx.message.author.avatar_url
                        embed = discord.Embed(description="Avatar of **{}**".format(ctx.message.author), color=0x0d00f9)
                        embed.set_image(url=avatar)
                        aver = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        return
                    if isinstance(error, commands.errors.BadArgument):
                        e = discord.Embed(title="USAGE:", description="@Aivo avatar <mention>", color=0x0d00f9)
                        aver = await self.bot.send_message(ctx.message.channel, embed=e)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(aver)
                        return

    @urban.error
    async def urban_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if isinstance(error, commands.errors.MissingRequiredArgument):
                        embed = discord.Embed(title="Usage:", description='@aivo urban <text>', color=0x0d00f9, timestamp=ctx.message.timestamp)
                        embed.set_footer(text="{} | If you find any bugs please contact Minlor#6811".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                        msg = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(5)
                        await self.bot.delete_message(msg)

def setup(bot):
    bot.add_cog(Misc(bot))
