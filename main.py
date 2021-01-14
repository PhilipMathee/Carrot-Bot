import discord
from discord.ext import commands
import json
import os



with open("./config.json") as f:
    configData = json.load(f)

token = configData["Token"]
bot = commands.Bot(command_prefix = '>')




extensions = ['cogs.Extras']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run(token)
