import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import datetime
import inspect
import keep_alive

def get_prefix(bot, message):
    if not message.server:
        return commands.when_mentioned_or("at!")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.server.id) not in prefixes:
        return commands.when_mentioned_or("at!")(bot, message)

    prefix = prefixes[str(message.server.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

bot= commands.Bot(command_prefix=get_prefix)

async def get_uptime():
    await bot.wait_until_ready()
    global seconds
    seconds = 0
    global minutes
    minutes = 0
    global hours
    hours = 0
    global days
    days = 0
    global weeks
    weeks = 0
    while not bot.is_closed:
        await asyncio.sleep(1)
        seconds += 1
        if seconds==60:
            minutes += 1
            seconds = 0
            if minutes==60:
                hours += 1
                minutes = 0
                if hours==24:
                    days += 1
                    hours = 0
                    if days==7:
                        weeks += 1
                        days = 0


async def status_task():
    while True:
        #await bot.change_presence(game=discord.Game(name= "BOT IS UPDATING...", type=3))
        await bot.change_presence(game=discord.Game(name= "{} Servers".format(str(len(bot.servers))),  type=3))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name= "Type a!help for help", type=3))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name= "{} Members".format(str(len(list(bot.get_all_members())))), type=3))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name= "Version 2.7",type=1))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    #bot.loop.create_task(status_task())
    bot.loop.create_task(get_uptime())
    print ("Bot is ready!")
    print ("Running on : " + bot.user.name)
    print ("Using ID : " + bot.user.id)
    print("Invite Link:\nhttps://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8\n".format(bot.user.id))
    print('Servers connected to:')
    #for server in bot.servers:
     #    print(server.name)
    print("Cogs:")

#bot.load_extension("AdBlock")
#bot.load_extension("Memes")
#bot.load_extension("Fun")
#bot.load_extension("ChatFilter")
#bot.load_extension("AdminCmds")
#bot.load_extension("Economy")
#bot.load_extension("Misc")
#bot.load_extension("Blacklist")



"""bot.remove_command('help')
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(description="Bot Created by: Minlor#0005", color=0x0d00f9)
    #embed = discord.Embed(description="Bot is currently updating for more info please visit the support server: https://discord.gg/ujAx2xK", color=0x0d00f9)
    #embed.set_author(name="Bot is updating..", icon_url=bot.user.avatar_url)
    embed.set_author(name="List Of Commands:", icon_url=bot.user.avatar_url)
    embed.add_field(name="Administration", value="setprefix, enablechatfilter, disablechatfilter, disableinvites, enableinvites, disablelinks, enablelinks", inline=False)
    embed.add_field(name="Moderation", value="ban, kick, mute ,unmute, tempmute(disabled), clear", inline=False)
    embed.add_field(name="Economy", value="level, xp, bal, balance, daily", inline=False)
    embed.add_field(name="Fun", value="meme, iq, howgay, slap, kiss, hug", inline=False)
    embed.add_field(name="Miscellaneous", value="meme, iq, howgay, slap, hug, kiss", inline=False)
    embed.add_field(name="Miscellaneous", value="avatar, ping, serverinfo, uptime, invite, inviteme, support", inline=False)
    embed.add_field(name="BETA/TEST", value="NONE!", inline=False)
    embed.set_footer(text='Version 2.5 BETA TEST!ㅤㅤㅤ   ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ          Requested by: ' + ctx.message.author.name)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    helpmsg = await bot.say(embed=embed)
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)"""

#HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND
bot.remove_command("help")
@bot.group(invoke_without_command=True, aliases=["cmds", "commands", "helpme", "cmd"])
async def help(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                await asyncio.sleep(0.5)
                await bot.delete_message(ctx.message)

@help.command(pass_context=True)
async def fun(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                #embed = discord.Embed(description="Bot is currently updating for more info please visit the support server: https://discord.gg/ujAx2xK", color=0x0d00f9)
                #embed.set_author(name="Bot is updating..", icon_url=bot.user.avatar_url)
                embed = discord.Embed(title=":smiley: Fun commands:", description="meme, iq, howgay, slap, kiss, hug, rps, 8ball", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                embed.set_author(name="Aivo | Fun", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                embed.set_footer(text="{} | Aivo is running on version 2.6".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=embed)

@help.command(pass_context=True)
async def config(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                embed = discord.Embed(title=":gear: Config commands:", description="setprefix, enablechatfilter, disablechatfilter, disableinvites, enableinvites, disablelinks, enablelinks", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                embed.set_author(name="Aivo | Config", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                embed.set_footer(text="{} | Aivo is running on version 2.6".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=embed)

@help.command(pass_context=True)
async def moderation(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                embed = discord.Embed(title=":hammer: Moderation commands:", description="ban, kick, mute, unmute, tempmute, clear", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                embed.set_author(name="Aivo | Moderation", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                embed.set_footer(text="{} | Aivo is running on version 2.6".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=embed)

@help.command(pass_context=True)
async def economy(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                embed = discord.Embed(title=":bank: Economy commands: - Currently disabled", description="daily, xp, level, balance", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                embed.set_author(name="Aivo | Economy", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                embed.set_footer(text="{} | Aivo is running on version 2.6".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=embed)

@help.command(pass_context=True)
async def misc(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                embed = discord.Embed(title=":paperclips: Miscellaneous commands:", description="avatar, ping, serverinfo, uptime", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                embed.set_author(name="Aivo | Miscellaneous", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                embed.set_footer(text="{} | Aivo is running on version 2.6".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await bot.send_message(ctx.message.channel, embed=embed)
#HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND---HELP COMMAND

@bot.command(pass_context=True)
async def uptime(ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                msg = "{0} weeks, {1} days, {2} hours, {3} minutes and {4} seconds".format(weeks, days, hours, minutes, seconds)
                embed = discord.Embed(title="Bot Uptime", description=msg, color=0x0d00f9)
                uptimemsg = await bot.say(embed=embed)
                await asyncio.sleep(1)
                await bot.delete_message(ctx.message)
                await asyncio.sleep(10)
                await bot.delete_message(uptimemsg)

@commands.cooldown(3, 30, commands.BucketType.user)
@bot.command(pass_context=True)
async def setprefix(ctx, *, pre):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '231821149015769089':
                    with open ("prefixes.json", "r") as f:
                        prefixes = json.load(f)

                    server = ctx.message.server
                    prefixes[server.id] = pre
                    await bot.say("New prefix is {}".format(pre))
                    with open("prefixes.json", "w") as f:
                        json.dump(prefixes, f)

                else:
                    await bot.say("You cant do that!")

@bot.command(name='eval', pass_context=True)
async def eval_(ctx, *, command):
    if ctx.message.author.id == "231821149015769089":
        res = eval(command)
        if inspect.isawaitable(res):
            await bot.say(await res)
        else:
            await bot.say(res)
    else:
        return

#ERROR--------------------------------------------------

          #          embed = discord.Embed(description="You can use this command again in {0}".format(error.retry_after), color=0x0d00f9)
           # embed.set_author(name="Cooldown", icon_url=ctx.message.author.avatar_url)
            #await self.bot.send_message(ctx.message.channel, embed=embed)

@setprefix.error
async def setprefix_error(error, ctx):
    if ctx.message.author.bot:
        return
    else:
        with open("blacklist.json", "r") as f:
            user = json.load(f)
            if str(ctx.message.author.id) in user:
                return
            else:
                if isinstance(error, commands.errors.MissingRequiredArgument):
                    e = discord.Embed(title="USAGE:", description="@Aivo setprefix <prefix>", color=0x0d00f9)
                    setpreferror = await bot.send_message(ctx.message.channel, embed=e)
                    await asyncio.sleep(1)
                    await bot.delete_message(ctx.message)
                    await asyncio.sleep(5)
                    await bot.delete_message(setpreferror)
                    return
                if isinstance(error, commands.errors.CommandOnCooldown):
                  embed = discord.Embed(description="**{0}** You can use this command 3 times every 30 seconds. You can use this command again in **{1:.2f}**".format(ctx.message.author, error.retry_after), color=0x0d00f9)
                  embed.set_author(name="Daily", icon_url=ctx.message.author.avatar_url)
                  await bot.send_message(ctx.message.channel, embed=embed)

@help.error
async def help_error(error, ctx):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    embed=discord.Embed(description=":small_blue_diamond: [**Support Server**](https://discord.gg/KJnnsTW) :small_blue_diamond: :small_orange_diamond: [**Invite Link**](https://discordapp.com/oauth2/authorize?client_id=549693186918973442&scope=bot&permission=8) :small_orange_diamond:", timestamp=ctx.message.timestamp, color=0x0d00f9, icon_url=bot.user.avatar_url)
                    embed.set_author(name="Aivo | Help", icon_url="https://cdn.discordapp.com/avatars/549693186918973442/107af8fbb7be1c52be471beb71328ef7.webp?size=1024")
                    embed.add_field(name=":hammer: **Moderation**", value="`a!help moderation`", inline=True)
                    embed.add_field(name=":gear: **Config**", value="`a!help config`", inline=True)
                    embed.add_field(name=":smiley: **Fun**", value="`a!help fun`", inline=True)
                    embed.add_field(name=":bank: **Economy**", value="`a!help economy`", inline=True)
                    embed.add_field(name=":paperclips: **Miscellaneous**", value="`a!help misc`", inline=True)
                    embed.set_footer(text="{} | Aivo is running on version 2.7".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                    await bot.send_message(ctx.message.channel, embed=embed)
                    return

@bot.command(pass_context=True, name='reload', hidden=True, aliases=["r"])
async def reload(ctx, *, cog: str):
    if ctx.message.author.id == "231821149015769089":
        """Reloads a module."""
        try:
            cog = "{0}".format(cog)
            bot.unload_extension(cog)
            bot.load_extension(cog)
            await bot.say("Reloaded!")
        except Exception as e:
            await bot.say('Error!')
            await bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            print("Cog : {0} Reloaded.".format(cog))
    else:
        return

#start the server
keep_alive.keep_alive()

bot.run("TOKEN")
