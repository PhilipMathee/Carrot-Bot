import discord
from discord.ext import commands
import random
import datetime
import pytz
import config

TOKEN = config.token

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    print('Karrot is ready to chop.')

@client.command()
async def time(ctx, *, userTZ):
    try:
        t_timezone = datetime.datetime.now(tz=pytz.timezone(userTZ))
        index = userTZ.find('/')
        city = userTZ[index+1::]
        await ctx.send(f"""{city}: {t_timezone.strftime("%a %H:%M")}""")
    except Exception as e:
        await ctx.send('Invalid Timezone')

@client.command()
async def jackass(ctx):
    await ctx.send(f'no u {round(client.latency * 1000)}ms')

@client.command(aliases=['proverb', 'proverbs'])
async def _proverb(ctx):
    with open('proverbs.txt', 'r') as f:
        lines = f.readlines()
        random_line = random.choice(lines)
        await ctx.send(random_line)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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


client.run(TOKEN)
