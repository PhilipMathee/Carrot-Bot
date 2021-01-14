from discord.ext import commands
import random
import datetime
import pytz

class Extras(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #commands
    @commands.Cog.listener()
    async def on_ready(self):
        print('Carrot is ready to chop.')


    #events (checks client latency)
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
            random_line = random.choice(lines)
            await ctx.send(random_line)

    #PRINTS A RANDOM PHRASE IN RESPONSE TO 8BALL
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(bot):
    bot.add_cog(Extras(bot))