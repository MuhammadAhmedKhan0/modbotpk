import discord
from discord.ext import commands
import asyncio
import praw
import random
import json


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

class Memes:
    def __init__(self, bot):
        self.bot = bot
                            
    async def on_ready(self):
        print("Cog Memes is ready!")

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    memes_submissions = reddit.subreddit('memes').hot()
                    post_to_pick = random.randint(1, 30)
                    for i in range(0, post_to_pick):
                        submission = next(x for x in memes_submissions if not x.stickied)

                    embed = discord.Embed(description="Hope ya like the meme **{}**".format(ctx.message.author), color=0x0d00f9)
                    embed.set_image(url=submission.url)
                    await self.bot.say(embed=embed)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)
        
        
        #await self.bot.say(submission.url)

    @meme.error
    async def meme_error(self, error, ctx):
        if ctx.message.author.bot:
            return
        else:
            with open("blacklist.json", "r") as f:
                user = json.load(f)
                if str(ctx.message.author.id) in user:
                    return
                else:
                    e = discord.Embed(description="You can use the meme command every 5 seconds right now you need to wait {0:.2f} to use the command again".format(error.retry_after), color=0x0d00f9)
                    memeerror = await self.bot.send_message(ctx.message.channel, embed=e)
                    await asyncio.sleep(1)
                    await self.bot.delete_message(ctx.message)
                    await asyncio.sleep(5)
                    await self.bot.delete_message(memeerror)
        

def setup(bot):
    bot.add_cog(Memes(bot))
