import discord
from discord.ext import commands
import asyncio
import json

class ChatFilter:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Cog ChatFilter is working!")

    @commands.command(pass_context=True)
    async def disablechatfilter(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open ("chatfilterservers.json", "r") as f:
                            servers = json.load(f)

                        server = ctx.message.server
                        servers[server.id] = 0
                        with open("chatfilterservers.json", "w") as f:
                            json.dump(servers, f)
                        embed=discord.Embed(title="Chatfilter Update", description="Administrator **{0}** Has **disabled** the chat filter!".format(ctx.message.author), color=0x0d00f9)
                        embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRequested by: ' + ctx.message.author.name)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        chdisable = await self.bot.say(embed=embed)
                        await asyncio.sleep(1)
                        await self.bot.delete_message(ctx.message)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(chdisable)

                    else:
                        await self.bot.say("You cant do that!")

    @commands.command(pass_context=True)
    async def enablechatfilter(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    if ctx.message.author.server_permissions.administrator:
                        with open ("chatfilterservers.json", "r") as f:
                            servers = json.load(f)
                            server = ctx.message.server
                            del servers[server.id]

                        with open("chatfilterservers.json", "w") as f:
                            json.dump(servers, f)
                        embed=discord.Embed(title="Chatfilter Update", description="Administrator **{0}** Has **enabled** the chat filter!".format(ctx.message.author), color=0x0d00f9)
                        embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤRequested by: ' + ctx.message.author.name)
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)
                        chenable = await self.bot.say(embed=embed)
                        await asyncio.sleep(10)
                        await self.bot.delete_message(chenable)

                    else:
                        await self.bot.say("You cant do that!")

    async def on_message(self, message):
        contents = message.content.split(" ") #contents is a list type
        for word in contents:
            #God will hate me for all these bad words which i will type rn :/
            chat_filter = ["PICKA", "KURAC", "JEBEM", "JEBE", "SESI", "SEX", "SEKS", "FUCK", "PUSSY", "DICK", "PENIS", "FUCKER", "FAK", "JEBI", "SUCK", "FUCKING", "COCK", "ASSHOLE", "SHIT", "MOTHERFUCKER", "SUCK", "ASS"]
            if word.upper() in chat_filter:
                bypass_list = ["549693186918973442", "418583960461770754", "328070105638502400", "539139919008890880", "257170205883629580"]
                if not message.author.id in bypass_list:
                  if message.server.id == "264445053596991498":
                    return
                  with open ("chatfilterservers.json", "r") as f:
                      servers = json.load(f)
                      if str(message.server.id) in servers:
                          return
                      else:
                          try:
                              await asyncio.sleep(0.1)
                              await self.bot.delete_message(message)
                              author = message.author.mention
                              embed = discord.Embed(title="ChatFiler",
                                     description="**Hey!** {} Stop swearing!".format(author),
                                     color=0x0d00f9)
                              embed.set_footer(text='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMessage deleted')
                              embed.set_thumbnail(url=message.author.avatar_url)
                              ch = await self.bot.send_message(message.channel, embed=embed)
                              await asyncio.sleep(5)
                              await self.bot.delete_message(ch)
                          except discord.errors.NotFound:
                              return


def setup(bot):
    bot.add_cog(ChatFilter(bot))
