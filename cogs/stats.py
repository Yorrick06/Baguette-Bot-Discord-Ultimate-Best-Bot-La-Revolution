import discord
import datetime
from discord.ext import commands

class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime

        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if days:
               fmt = f"{days} days, {hours} hours, {minutes} minutes and {seconds} seconds"
        elif hours:
             fmt = f"{hours} hours, {minutes} minutes and {seconds} seconds"
        elif minutes:
              fmt = f"{minutes} minutes and {seconds} seconds"
        else:
               fmt = f"{seconds} seconds"
        embed = discord.Embed(
			title="Baguette stats", 
			color=discord.Color(0x2f3136), 
			description=f"Name: Baguette\nPrefix: b!\nPing: {round(self.bot.latency * 1000)}"
            + f"\nServer Count: {len(self.bot.guilds)}\nUptime: {fmt}"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(stats(bot))