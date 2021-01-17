import discord
from discord.ext import commands

class Management(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(f'banned {member.mention}')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminater = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminater) == (member_name, member_discriminater):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(Management(client))