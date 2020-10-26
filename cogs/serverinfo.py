import discord
import datetime
from discord.ext import commands

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["guildinfo", "sinfo"])
    async def serverinfo(self, ctx):
        #members = ctx.guild.members
        guild = ctx.guild
        guild_id = ctx.guild.id
        owner_of_guild = ctx.guild.owner 
        region_of_guild = ctx.guild.region
        created_at = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")
        members_of_guild = len(ctx.guild.members)
        #banned_members = len(await ctx.guild.bans())
        text_channels_of_guild = len(ctx.guild.text_channels)
        voice_channels_of_guild = len(ctx.guild.voice_channels)
        roles_of_guild = len(ctx.guild.roles)
        bots_of_guild = (len([member for member in guild.members if member.bot]))



        e = discord.Embed(title=f"{ctx.guild.name} serverinfo.", color=discord.Color(0x2f3136), description=f"```fix\nMain info about {ctx.guild.name}:```\n**ID**: {guild_id}\n**Owner**: {owner_of_guild}\n"
        + f"**Region**: {region_of_guild}\n\n```fix\nMore info about {ctx.guild.name}:```\n**Created at**: {created_at}\n**Members**: {members_of_guild}\n**Total bots**: {bots_of_guild}\n\n```fix\nChannels/Roles info:```\n**Text channels**: <:channel:756100543092621332> {text_channels_of_guild}\n"
        + f"**Voice channels**: <:voice:756100977450287124> {voice_channels_of_guild}\n**Roles**: <:role:756119758591623188> {roles_of_guild}"
        )
        e.set_thumbnail(url=ctx.guild.icon_url)
        e.set_footer(text=f"Requested by {ctx.author.name}")

        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(serverinfo(bot))

