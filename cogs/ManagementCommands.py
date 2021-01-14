from discord.ext import commands

class ManagementCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_member_join(self, ctx, client):
        pass