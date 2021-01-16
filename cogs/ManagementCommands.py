from discord.ext import commands

class ManagementCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_member_join(self, ctx):
        await ctx.send(f'Welcome to the degenerate encampment {self.bot.user}')

    @commands.Cog.listener
    async def on_member_leave(self, ctx):
        await ctx.send(f'Cheers {self.bot.user}, ')

    @commands.command
    async def ban(self):
        pass

    

def setup(bot):
    bot.add_cog(ManagementCommands(bot))