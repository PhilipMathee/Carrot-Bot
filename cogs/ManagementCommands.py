import discord
from discord.ext import commands

class ManagementCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    '''
    clearing messages
    '''
    @commands.command()
    async def clear(self, ctx, amount=5):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await ctx.channel.purge(limit=amount)
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use clear command.")

    '''
    muting
    '''
    @commands.command()
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).mute_members):
            await member.ban(reason=reason)
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use mute command.")

    '''
    kicking
    '''
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *,  reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
            await member.kick(reason=reason)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use kick command.")

    '''
    banning
    '''
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
            await member.ban(reason=reason)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use ban command.")
    

def setup(bot):
    bot.add_cog(ManagementCommands(bot))