import discord
from discord.ext import commands
import json
import os


'''
Load token from .json file
'''
with open("./config.json", "r") as f: 
    configData = json.load(f)

token = configData["Token"]
bot = commands.Bot(command_prefix = '>')



@commands.Cog.listener()
async def on_ready(self):
    print('Carrot is ready to chop.') #will print in console if bot launches properly



'''
Load extensions
'''
extensions = ['cogs.Extras']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(token)
