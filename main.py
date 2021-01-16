import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '>')

@bot.event
async def on_ready():
    print('Carrot is ready to chop.') #will print in console if bot launches successfully



'''
Load extensions
'''
extensions = ['cogs.Extras']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(os.getenv('TOKEN'))
