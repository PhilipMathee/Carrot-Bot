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
        else:
            await ctx.send("You do not have permission to use clear command.")

    '''
    muting
    '''
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role.position > member.top_role.position:
        #if ctx.message.author.guild_permissions.mute_members:
            mute = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.add_roles(mute)
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await ctx.send(embed=embed)

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.mute_members:
            mute = discord.utils.get(ctx.guild.roles, name='Muted')
            await member.remove_roles(mute)
            embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await ctx.send(embed=embed)

    '''
    kicking
    '''
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *,  reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
            await member.kick(reason=reason)
        else:
            await ctx.send('You do not have permission to use kick command.')

    '''
    banning
    '''
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *,  reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
            await member.ban(reason=reason)
        else:
            await ctx.send("You do not have permission to use ban command.")
    
def setup(bot):
    bot.add_cog(ManagementCommands(bot))