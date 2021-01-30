import discord
from discord.ext import commands

class Management(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    '''
    clearing messages
    '''
    @commands.command()
    async def clear(self, ctx, amount=5):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await ctx.channel.purge(limit=amount)
            embed=discord.Embed(title="Clear", description='Cleared **{0}** messages.'.format(amount), color=0xec6014)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Clear", description='You do not have permission to use that command.', color=0xec6014)
            await ctx.send(embed=embed)

    '''
    muting
    '''
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role.position > member.top_role.position:
            mute = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles(mute)
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xec6014)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xec6014)
            await ctx.send(embed=embed)

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role.position > member.top_role.position:
            mute = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.remove_roles(mute)
            embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xec6014)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xec6014)
            await ctx.send(embed=embed)

    '''
    kicking
    '''
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *,  reason=None):
        if ctx.guild.me.top_role.position > member.top_role.position:
            await member.kick(reason=reason)
            embed=discord.Embed(title="User Kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xec6014)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xec6014)
            await ctx.send(embed=embed)

    '''
    banning
    '''
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        if ctx.guild.me.top_role.position > member.top_role.position:
            await member.ban(reason=reason)
            embed=discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0xec6014)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xec6014)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Management(bot))