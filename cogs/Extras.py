from discord.ext import commands
import random
import datetime
import pytz
import inspirobot

'''
This is a Cog with 'Extra' functions for the bot.
Which includes random features that do not fit under a specific category.
'''

class Extras(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #prints client latency
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}ms')


    #PRINTS TIME IN SPECIFIED TIME ZONE
    @commands.command()
    async def time(self, ctx, *, timezone):
        try:
            t_timezone = datetime.datetime.now(tz=pytz.timezone(timezone))
            index = timezone.find('/')
            city = timezone[index+1::]
            time = t_timezone.strftime("%a %H:%M")
            await ctx.send(f"""{city}: {t_timezone.strftime("%a %H:%M")}""")
        except:
            await ctx.send('Invalid Timezone.')


    #PRINTS A RANDOM PROVERB FROM PROVERBS.TXT
    @commands.command(aliases=['proverb', 'proverbs'])
    async def _proverb(self, ctx):
        with open('TextDocuments/proverbs.txt', 'r') as f:
            lines = f.readlines()
            await ctx.send(random.choice(lines))

    #PRINTS A RANDOM PHRASE IN RESPONSE TO 8BALL
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        with open("TextDocuments/8ball.txt", 'r') as f:
            lines = f.readlines()
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(lines)}')

    @commands.command(aliases=['inspire'])
    async def _inspire(self, ctx):
        quote = inspirobot.generate()
        await ctx.send(quote.url)

'''
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return

        msg = ctx.content

        greet = ['yoo', 'yo', 'hey', 'hi', 'sup', 'hello'
        , 'yoo', 'yooo', 'heyy', 'heyyy', 'ello', 'o/', 'heya']
        if any(word in msg.lower() for word in greet):
            await ctx.channel.send("yo gamer")
'''
def setup(bot):
    bot.add_cog(Extras(bot))
