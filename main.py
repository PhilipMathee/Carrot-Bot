import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix = '>') #bot prefix
token = config.TOKEN #loads token from config file

@bot.event
async def on_ready():
    print('Carrot is ready to chop.') #will print in console if bot launches successfully

extensions = ['cogs.Extras'] # list of cogs to load

if __name__ == '__main__': #loading extensions
    for ext in extensions:
        bot.load_extension(ext)

bot.run(token)
