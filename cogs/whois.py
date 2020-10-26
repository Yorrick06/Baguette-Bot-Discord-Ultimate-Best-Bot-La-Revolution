import discord
import random
import os
import datetime
import asyncio
import json
import sys
from discord.ext import commands, tasks
from discord.utils import get, find
from itertools import cycle
from discord.activity import CustomActivity, Spotify


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


    @commands.command()
    async def status(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        if len(member.activities) == 0:
            embed = discord.Embed(
            title=f"{member}'s status.",
            color=discord.Color(0x2f3136),
            description="<:SwitchOff:739752271973187675> This user currently got no status/is offline"
            )
            await ctx.send(embed=embed)

        for activity in member.activities:
            if isinstance(activity, CustomActivity):
                embed = discord.Embed(title=f"{member}'s status.", color=discord.Color(0x2f3136), description=f"> {member.activity}\n<:SwitchOnWHC:739753214630690856>")
                if activity.emoji is not None:
                    if activity.emoji.url == "py":
                        pass
                    else:
                        embed.set_thumbnail(url=activity.emoji.url)

                await ctx.send(embed=embed)

    @commands.command(aliases=["userinfo", "profile"])
    async def whois(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        roles = []
        for role in member.roles:
             if role.is_default():
                 pass
             else:
                 roles.append(role)
        
        
        if member.status is discord.Status.offline:
            status = "<:offline:723840924236382268>"
        elif member.status is discord.Status.online:
            status = "<:online:723840924282650624>"
        elif member.status is discord.Status.dnd:
            status = "<:dnd:723840924332982342>"
        elif member.status is discord.Status.idle:
            status = "<:idle:723840924257353768>"
        else:
            return

        embed = discord.Embed(
            title=f"{member}'s userinfo", 
            color=discord.Color(0x2f3136), 
            timestamp=ctx.message.created_at,
            description=f"{member.name} is: {status}"
            )

        if member.bot == 0:
            embed.add_field(name="Bot:", value="<:SwitchOff:739752271973187675>")
        else:
            embed.add_field(name="Bot:", value="<:SwitchOnWHC:739753214630690856>")

        embed.add_field(name="User nickname:", value=member.display_name)
        embed.add_field(name="User id:", value=member.id)

        if member.guild_permissions.kick_members == True:
            embed.add_field(name="Kick members:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Kick members:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.ban_members == True:
            embed.add_field(name="Ban members:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Ban members:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.administrator == True:
            embed.add_field(name="administrator:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="administrator:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_guild == True:
            embed.add_field(name="Manage server:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage server:", value="<:SwitchOff:739752271973187675>")

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)

        if len(member.activities) == 0:
            embed.add_field(name="Activity:", value="> This user currently got no status.", inline=False)

        for activity in member.activities:
            if isinstance(activity, CustomActivity):
                embed.add_field(name="Status Activity", value=f"> {member.activity}", inline=False)
            elif isinstance(activity, Spotify):
                embed.add_field(name="Spotify Activity", value=f"> This user is listening to Spotify: **{activity.title}**", inline=False)


        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=member.avatar_url)



        await ctx.send(embed=embed)

    @commands.command()
    async def perms(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        embed = discord.Embed(
            title=f"{member.name}'s perms.",
            color=discord.Color(0x2f3136),
            timestamp=ctx.message.created_at
        )
        
        if member.guild_permissions.send_messages == True:
            embed.add_field(name="Send messages:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Send messages:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.kick_members == True:
            embed.add_field(name="Kick members:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Kick members:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.ban_members == True:
            embed.add_field(name="Ban members:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Ban members:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.administrator == True:
            embed.add_field(name="Administrator:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Administrator:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_guild == True:
            embed.add_field(name="Manage server:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage server:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_roles == True:
            embed.add_field(name="Manage roles:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage roles:", value="<:SwitchOff:739752271973187675>")
        
        if member.guild_permissions.manage_messages == True:
            embed.add_field(name="Manage messages:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage messages:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_webhooks == True:
            embed.add_field(name="Manage webhooks:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage webhooks:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_emojis == True:
            embed.add_field(name="Manage emojis:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage emojis:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.manage_nicknames == True:
            embed.add_field(name="Manage nicknames:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage nicknames:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.view_audit_log == True:
            embed.add_field(name="Manage audit log:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Manage audit log:", value="<:SwitchOff:739752271973187675>")

        if member.guild_permissions.add_reactions == True:
            embed.add_field(name="Add reactions:", value="<:SwitchOnWHC:739753214630690856>")
        else:
            embed.add_field(name="Add reactions:", value="<:SwitchOff:739752271973187675>")

        

        embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed.set_author(name="Adminstrator means the user got all the perms!", icon_url=member.avatar_url, url="https://google.com")

        await ctx.send(embed=embed)


    @commands.command()
    async def uinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        roles = []
        for role in member.roles:
             if role.is_default():
                 pass
             else:
                 roles.append(role)
        
        
        if member.status is discord.Status.offline:
            status = "<:offline:723840924236382268>"
        elif member.status is discord.Status.online:
            status = "<:online:723840924282650624>"
        elif member.status is discord.Status.dnd:
            status = "<:dnd:723840924332982342>"
        elif member.status is discord.Status.idle:
            status = "<:idle:723840924257353768>"
        else:
            return


        if member.bot == 0:
            Bot = "<:SwitchOff:739752271973187675>"
        else:
            Bot = "<:SwitchOnWHC:739753214630690856>"

        if member.guild_permissions.manage_messages == True:
            messagen = "<:SwitchOnWHC:739753214630690856>"
        else:
            messagen = "<:SwitchOff:739752271973187675>"


        if member.guild_permissions.manage_guild == True:
            servern ="<:SwitchOnWHC:739753214630690856>"
        else:
            servern ="<:SwitchOff:739752271973187675>"

        if member.guild_permissions.kick_members == True:
            kickn ="<:SwitchOnWHC:739753214630690856>"
        else:
            kickn ="<:SwitchOff:739752271973187675>"

        embed = discord.Embed(
            title=f"{member}'s userinfo", 
            color=discord.Color(0x2f3136), 
            timestamp=ctx.message.created_at,
            description=f"> {member.name} is: {status}\n> Bot: {Bot}\n> {member.name}'s id: {member.id}\n\n**Server permissions:**\n> Manage messages: {messagen}\n> Manage server: {servern}\n> Kick members: {kickn}\n"
            + "\n**More about " + member.name + f":**\n> Roles: ({len(roles)})\n> " + " ".join([role.mention for role in roles]) + "\n> Created at: " + member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
            )


        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)



        await ctx.send(embed=embed)




    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        e = discord.Embed(title=f"{member.name} his avatar.", color=discord.Color(0x2f3136), description=f"[Link]({member.avatar_url})")
        e.set_image(url=member.avatar_url)
        await ctx.send(embed=e)


    
    #@commands.command()
    #@commands.has_role('baget')
    #async def give(self, ctx, member: discord.Member = None, role: discord.Role = None):
    #    member = ctx.author if not member else member
    #    
    #    baget = discord.utils.get(member.guild.roles, name="baget")

    #    await member.add_roles(baget)


    #    embed = discord.Embed(
    #        ttile="Baguette?",
    #        color=discord.Color(0x2f3136),
    #        description=f"Wow! {ctx.author.name} gave {member.name} the baguette role!"
    #    )
    #    await ctx.send(embed=embed)


        


    
            
        
            



            


def setup(bot):
    bot.add_cog(userinfo(bot))