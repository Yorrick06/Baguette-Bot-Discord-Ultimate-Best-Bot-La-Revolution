import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pong'])
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Ping",
            color=discord.Color(0x2f3136),
            description=f"🏓Pong!, {round(self.bot.latency * 10000)}ms"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
    