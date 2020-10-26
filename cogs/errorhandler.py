import discord
from discord.ext import commands, tasks
from discord.utils import get

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title="Uh oh..",
                color=discord.Color(0x2f3136),
                description=f">>> ```fix\n{error}\n```",
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=f"Error raised by {ctx.message.author.name}")
            return await ctx.send(embed=embed)

        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(
                title="Uh oh..",
                color=discord.Color(0x2f3136),
                description=f">>> ```fix\n{error}\n```",
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=f"Error raised by {ctx.message.author.name}")
            return await ctx.send(embed=embed)

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
            await ctx.send(_message)
            return
        
        raise error

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        g = self.bot.get_guild(id=705745960575434773)
        channel = get(g.channels, name="🔧-coding-with-yorrick")
        embed = discord.Embed(
            title=f"Joined guild! #{len(self.bot.guilds)}",
            color=discord.Color(0x2f3136),
            description=f"Owner name: {guild.owner}\nOwner ID: ({guild.owner.id})\nServer name: {guild.name}\nServer ID: ({guild.id})\nServer members: {len(guild.members)}"
        )
        embed.set_thumbnail(url=guild.icon_url)
        await channel.send(embed=embed)
    

def setup(bot):
    bot.add_cog(error(bot))


