import discord
from discord.ext import commands, tasks

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(aliases=["help"])
    async def oldhelp(self, ctx):
        embed = discord.Embed(
            title="Baguette Help Menu",
            color=discord.Color(0x2f3136),
            description=f"Displaying the most important Baguette commands.\n\n"
        + "b!help - Brings up the help menu.\n"
        + "b!ping - Check the bots ping.\n"
        + "b!stats - Shows the bots stats.\n"
        + "b!whois - Check someones userinfo.\n"
        + "b!serverinfo - Check the serevrinfo.\n"
        + "b!spotify - Look if someone is using baguettify.\n"
        + "b!reverse - Let the bot say something in reverse.\n"
        + "b!upper - Upper case some text.\n"
        + "b!perms - Check someone's perms.\n"
        + "b!fight - Fight someone.\n"
        + "b!num - Grab a random number.\n"
        + "b!calc - Use the calculator.\n"
        + "b!avatar - Look at someones avatar.\n"
        + "b!baguettepic - Get a picture of a baguette.\n"
        + "b!impostor - Look if someone is the imposter. (b!impostor <user> <yes or no>)\n"
        + "b!logs <#channel or disable> - Enable or disable logs in your server.\n"
        + "b!baguette_maker - To open your Baguette maker.\n"
        + "**Type b!chelp to get help about the currency!**\n"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def chelp(self, ctx):
        embed = discord.Embed(
            title="Currency Help Menu",
            color=discord.Color(0x2f3136),
            description=f"These are the commands for currency!\n\nb!balance - Check your balance.\nb!work - Work for more cash!\n"
            + "b!daily - Claim your daily reward.\nb!shop - Show the shop.\nb!buy - Buy items from the shop.\n"
            + "b!inventory - Check your inventory.\nb!select - Select a color for on b!balance.\nb!coinflip <heads or tails> <amount to bet> - Bet some cash in coinflip\n"
            + "b!moneylb - Check the money leaderboard.\n"
            + "b!invest <amount> <time> - Invest some money!\n"
        )
        await ctx.send(embed=embed)






def setup(bot):
    bot.remove_command("help")    
    bot.add_cog(Help(bot))