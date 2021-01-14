from discord.ext import commands
import random
import datetime
import pytz

'''
This is a Cog with 'Extra' functions for the bot.
Which includes random features that do not fit under a specific category.
'''

class Extras(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #prints client latency
    @commands.command()
    async def jackass(self, ctx):
        await ctx.send(f'no u {round(self.bot.latency * 1000)}ms')


    #PRINTS TIME IN SPECIFIED TIME ZONE
    @commands.command()
    async def time(self, ctx, *, userTZ):
        try:
            t_timezone = datetime.datetime.now(tz=pytz.timezone(userTZ))
            index = userTZ.find('/')
            city = userTZ[index+1::]
            await ctx.send(f"""{city}: {t_timezone.strftime("%a %H:%M")}""")
        except Exception as e:
            await ctx.send('Invalid Timezone')


    #PRINTS A RANDOM PROVERB FROM PROVERBS.TXT
    @commands.command(aliases=['proverb', 'proverbs'])
    async def _proverb(self, ctx):
        with open('proverbs.txt', 'r') as f:
            lines = f.readlines()
            await ctx.send(random.choice(lines))

    #PRINTS A RANDOM PHRASE IN RESPONSE TO 8BALL
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        with open("8ball.txt", as 'r') as f:
            lines = f.readlines()
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(lines)}')


def setup(bot):
    bot.add_cog(Extras(bot))
