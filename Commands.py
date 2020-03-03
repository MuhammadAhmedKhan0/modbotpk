import discord
from discord.ext import commands
import asyncio
import random

class Commands:
    def __init__(self, bot):
        self.bot = bot
                            
    async def on_ready(self):
        print("Cog Commands is working!")

    @help.command()
    async def fun(self, ctx):
        await self.bot.say("test working")

def setup(bot):
    bot.add_cog(Commands(bot))
