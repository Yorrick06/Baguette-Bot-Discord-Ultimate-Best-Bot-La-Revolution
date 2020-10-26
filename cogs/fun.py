import discord
import asyncio
import wikipedia
import random
import datetime
from discord.ext import commands
from discord.utils import get



class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fights = [
            '{0} tried to throw a snowball at {1} but it hits Dabbit\'s car, and Dabbit is not pleased!',
            '{0} tackled {1} down with a fish.',
            '{0} fought {1}, but it was not effective...',
            '{0} tried to throw a bucket of water at {1}, but accidentally threw it all over {2}!',
            '{0} got tired of ks’ puns and tried to fight but accidentally hit {1}',
            '{0} tried to hit {1}, but {1} had a reverse card up their sleeve so {0} got hit instead',
            '{0} tried to fight {1}, but ended up being given cereal soup by Dabbit.',
            '{0} tried to attack {1}, but they slipped and crashed into Ghoul\'s car, making a huge cat shaped dent in the hood',
            '{0} tried to fight {1} but was attacked by a gang of kittens',
            '{0} challenged {1} to a race in Mario Kart but the CPU won instead!',
            '{1} dodged a mighty fine swing from {0}, and then backhanded {0} in self defense.',
            '{0} begged their pet to attack {1}, but the pet stared back with no indication of understanding.',
            '{0} fought like a dog, but {1} fought back like a bear, winning the fight!',
            'A wild {1} appears!\n{1} uses Bite! It\'s not very effective...\n{0} uses Mega Punch! It\'s very effective!\n{0} has won!',
            'As {0} ran all sweaty and tired reaching out for a last punch, {1} dashed to the side, leaving {0} tumbling onto the ground.',
            '{0} tried to modify the Dupe Bomber 3000 to take down {1} with tons of dupe reports, but Dannysaur got there first and denied them all... Which broke the machine.',
            '{0} Mega Evolved and tried to wipe out {1} with Hyper Beam! But {1} used Mimic and reversed it back onto {0} instead!',
            '{0} threw a snowball at {1} but unfortunately it hits a window at Discord HQ. Oops',
            '{0} tricked {1} into waking up the Sleeping Pizza. The Sleeping Pizza does not like being woken up, so it turned both {0} and {1} into Calzone Pizza. Rest In Pepperoni.',
            '{0} went to tackle {1}, but they did a dank meme and lowkey dabbed out of the way',
            '{0} hit the Smash ball, but fell off the stage before they could use it on {1}',
            '{0} threw a pokeball at {1}, but it was only a Goldeen'
            ]

    @commands.command()
    async def reverse(self, ctx, *, message):
        if message == "enoyreve@":
            await ctx.send("Haha nice try.")
            return
        elif message == "ereh@":
            await ctx.send("Close but not close.")
            return
        else:
            await ctx.send(message[::-1])

    # @commands.command()
    # async def say(self, ctx, *, message):
    #     await ctx.send(message)

    @commands.command()
    async def upper(self, ctx, *, message):
        if message == "@everyone":
            return
        else:
            await ctx.send(message.upper())

    @commands.command()
    async def fakeban(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        await ctx.send(f"{ctx.author} has banned {member}! Oh no, he must be crying right now.\nGive him some **baguette** love.")
        await ctx.message.delete()

    @commands.command()
    async def fight(self, ctx, user: discord.Member):
        await ctx.send(random.choice(self.fights).format(ctx.author.name, user.name, ctx.guild.owner.name))
    
    @commands.command()
    async def suggest(self, ctx, *, desc):
        g = self.bot.get_guild(id=705745960575434773)
        channel = get(g.channels, id=721804046096138311)

        e = discord.Embed(title="New suggestion!", color=discord.Color(0x2f3136), description=f"```fix\n{desc}\n```")
        e.set_footer(text="Click ⬆️ to upvote and ⬇️ to downvote.")
        e.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)

        msg = await channel.send(embed=e)
        await msg.add_reaction('⬆️')
        await msg.add_reaction('⬇️')
        await ctx.message.delete()  

    @commands.command()
    async def num(self, ctx, numb: int):
        number = random.randint(0, numb)
        await ctx.send(number)

    @commands.command()
    async def calc(self, ctx, numb: float, value: str, number: float):          
        if value == "+":
            await ctx.send(numb + number)
        elif value == "-":
            await ctx.send(numb - number)
        elif value == "*":
            await ctx.send(numb * number)
        elif value == "x":
            await ctx.send(numb * number)
        elif value == "/":
            try:
                await ctx.send(numb / number)
            except ZeroDivisionError:
                await ctx.send("Don't divide by 0 you should've learnt that.")
        elif value == ":":
            try:
                await ctx.send(numb / number)
            except ZeroDivisionError:
                await ctx.send("Don't divide by 0 you should've learnt that.")
        elif value == "**":
            try:
                await ctx.send(numb ** number)
            except OverflowError:
                await ctx.send("Your number is too large! Try a smaller one.")
        else:
            await ctx.send("Try using +, -, * or /")

    @commands.command()
    async def baguettepic(self, ctx):
        brr = random.randint(1, 5)
        if brr == 1:
            await ctx.send("https://i.imgur.com/T5wKvDX.png")
        elif brr == 2:
            await ctx.send("https://i.imgur.com/nZgm8w4.png")
        elif brr == 3:
            await ctx.send("https://i.imgur.com/2NX7uNP.png")
        elif brr == 4:
            await ctx.send("https://i.imgur.com/oj0yERN.png")
        elif brr == 5:
            await ctx.send("https://i.imgur.com/7V5Z8qg.png")
        else:
            await ctx.send("Nice you got an easter egg, how? I dont know.")

    @commands.command()
    async def blub(self, ctx):
        blub = random.randint(0, 1)
        if blub == 0:
            await ctx.send("Poggest supporter.")
        elif blub == 1:
            await ctx.send("<:ThinkShrug:741266583267049503>")
        else:
            return

    @commands.command()
    async def report(self, ctx, *, desc):
        g = self.bot.get_guild(id=705745960575434773)
        channel = get(g.channels, id=738080761529499650)
        reporter = ctx.author.name

        e = discord.Embed(title="New report!", color=discord.Color(0x2f3136), description=f"```fix\n{desc}\n```")
        e.set_footer(text=reporter)
        e.add_field(name="User information:", value=f"Mention: {ctx.author.mention}\nJoined at:" + ctx.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await channel.send(embed=e)
        await ctx.message.delete()
    
    @commands.command()
    async def impostor(self, ctx, user: discord.Member, desc):
        impostor_left = random.randint(0, 2)
        if user.mention == 0:
            await ctx.send("You need to mention someone!")
        elif desc == 0:
            await ctx.send("Yes or no.")
        elif desc == "yes":
            await ctx.send(
                f".      　。　　　　•　    　ﾟ　　。         。\n　　.　　　.　　　  　　.　　　　　。　　   。　.\n　.　　      。　               ඞ   。　    .    •\n            .       {user.name} was  an Impostor. \n　 。　.              {impostor_left} impostors remain.\n 　　。　　　　　　ﾟ　　　.　　　　　.\n,　　　　.　 .　　       .               。　　　.　　　.   。"
            )
        else:
            await ctx.send(
                f".      　。　　　　•　    　ﾟ　　。         。　　　　•　 \n　　.　　　.　　　  　　.　　　　　。　　   。　.\n　.　　      。　               ඞ   。　    .    •\n                 {user.name} was not an Impostor.\n　 。　.              {impostor_left} impostors remain.\n　 　　。　　　　　　ﾟ　　　.　　　　　.\n,　　　　.　 .　　       .               。　　　.　　　.   。"
            )

    @commands.command()
    async def reddit(self, ctx):
        e = discord.Embed(title="Enchanted Subreddit", color=discord.Color(0x2f3136), description="https://www.reddit.com/r/EnchantedGG/")
        await ctx.send(embed=e)

    @commands.command()
    async def html(self, ctx):
        e = discord.Embed(color=discord.Color(0x2f3136), description="<html>\n</html>")
        msg = await ctx.send(embed=e)
        await asyncio.sleep(0.5)
        e2 = discord.Embed(color=discord.Color(0x2f3136), description="<html>\n<body>\n</body>\n</html>")
        await msg.edit(embed=e2)
        await asyncio.sleep(0.5)
        e3 = discord.Embed(color=discord.Color(0x2f3136), description="<html>\n<body>\n<p>This is Baguette Bot!</p>\n</body>\n</html>")
        await msg.edit(embed=e3)        
        await asyncio.sleep(0.5)
        e4 = discord.Embed(color=discord.Color(0x2f3136), description="<html>\n<body>\n<h1>This is Baguette Bot!</h1>\n<p>This bot is made for learning purpose!</p>\n</body>\n</html>")
        await msg.edit(embed=e4)      
        await asyncio.sleep(0.5)
        e5 = discord.Embed(color=discord.Color(0x2f3136), description="<!DOCTYPE html>\n<html>\n<body>\n<h1>This is Baguette Bot!</h1>\n<p>This bot is made for learning purpose!</p>\n</body>\n</html>")
        await msg.edit(embed=e5)   
        await asyncio.sleep(0.5)
        e6 = discord.Embed(color=discord.Color(0x2f3136), description="<!DOCTYPE html>\n<html>\n<body>\n<h1>This is Baguette Bot!</h1>\n<p>This bot is made for learning purpose!</p>\n<img src=\"https://cdn.discordapp.com/avatars/738653291873042551/90d7ff63983e72e3e1a19345ac3a7fca.webp?size=1024 \">\n</body>\n</html>")
        await msg.edit(embed=e6)
        await asyncio.sleep(0.5)
        e7 = discord.Embed(color=discord.Color(0x2f3136), description="<!DOCTYPE html>\n<html>\n<style>\n</style>\n<body>\n<h1>This is Baguette Bot!</h1>\n<p>This bot is made for learning purpose!</p>\n<img src=\"https://cdn.discordapp.com/avatars/738653291873042551/90d7ff63983e72e3e1a19345ac3a7fca.webp?size=1024 \">\n</body>\n</html>")
        await msg.edit(embed=e7)
        await asyncio.sleep(0.5)
        e8 = discord.Embed(color=discord.Color(0x2f3136), description="<!DOCTYPE html>\n<html>\n<style>\n</style>\n<body>\n<h1>This is Baguette Bot!</h1>\n<p>This bot is made for learning purpose!</p>\n<a href=\"https://baguette.com \">Baguette</a>\n<img src=\"https://cdn.discordapp.com/avatars/738653291873042551/90d7ff63983e72e3e1a19345ac3a7fca.webp?size=1024 \">\n</body>\n</html>")
        await msg.edit(embed=e8)







        #msg = await ctx.send("<html>\n</html>")
        #await asyncio.sleep(4)    
        #await msg.edit(conent="<html>\n<body>\n</body>\n</head>")        
        #https://cdn.discordapp.com/avatars/738653291873042551/90d7ff63983e72e3e1a19345ac3a7fca.webp?size=1024

    @commands.command(aliases=["baguettemaker", "oog_maker", "baguette maker"])
    async def baguette_maker(self, ctx):
        e = discord.Embed(color=discord.Color(0x2f3136), description="Bag")
        msg = await ctx.send(embed=e)
        
        e = discord.Embed(color=discord.Color(0x2f3136), description="Baguet")
        await msg.edit(embed=e)
        
        e3 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette")
        await msg.edit(embed=e3)        
        
        e4 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette mak")
        await msg.edit(embed=e4)      
        
        e5 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette maker")
        await msg.edit(embed=e5)   
        
        e6 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette maker sta")
        await msg.edit(embed=e6)
        
        e7 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette maker start")
        await msg.edit(embed=e7)
        
        e8 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette maker starting")
        await msg.edit(embed=e8)
        
        e9 = discord.Embed(color=discord.Color(0x2f3136), description="Baguette maker starting...")
        await msg.edit(embed=e9)

        ee = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=ee)

        await asyncio.sleep(1)

        e10 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - B")
        await msg.edit(embed=e10)   

        e11 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Bagu")
        await msg.edit(embed=e11)

        e12 = discord.Embed(color=discord.Color(0x2f3136), description="🥖- Baguett")
        await msg.edit(embed=e12)   

        e13 = discord.Embed(color=discord.Color(0x2f3136), description="🥖- Baguette ma")
        await msg.edit(embed=e13)  

        e14 = discord.Embed(color=discord.Color(0x2f3136), description="🥖- Baguette maker ")
        await msg.edit(embed=e14)   

        e15 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker ha")
        await msg.edit(embed=e15) 

        e16 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker has s")
        await msg.edit(embed=e16) 

        e17 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker has star")
        await msg.edit(embed=e17) 
        
        e18 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker has started")
        await msg.edit(embed=e18) 
        
        e19 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker has started...")
        await msg.edit(embed=e19) 
        
        e20 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Baguette maker has started... ✅")
        await msg.edit(embed=e20) 

        e21 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e21) 

        e22 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Down")
        await msg.edit(embed=e22) 
                
        e23 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloa")
        await msg.edit(embed=e23) 

        e24 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloadin")
        await msg.edit(embed=e24)         

        e25 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading B")
        await msg.edit(embed=e25) 

        e26 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading Bagu")
        await msg.edit(embed=e26) 

        e27 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading Baguett")
        await msg.edit(embed=e27) 
                   
        e28 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading Baguette")
        await msg.edit(embed=e28) 

        e29 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading Baguette...")
        await msg.edit(embed=e29) 

        e30 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Downloading Baguette... ✅")
        await msg.edit(embed=e30) 

        e31 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e31) 

        e32 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Ins")
        await msg.edit(embed=e32) 

        e33 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Instal")
        await msg.edit(embed=e33) 

        e34 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installi")
        await msg.edit(embed=e34) 

        e35 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing")
        await msg.edit(embed=e35) 

        e36 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing Ba")
        await msg.edit(embed=e36) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing Baguet")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing Baguette")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing Baguette...")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Installing Baguette... ✅")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Cre")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creati")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating L")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La R")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La Revo")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La Revolut")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La Revolution")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La Revolution...")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Creating La Revolution... ✅")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 1%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 5%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 10%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 20%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Fou")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Found B")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Found Bug")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Found Bug...")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Kil")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Killin")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Killing Bug")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 25%" + " Killing Bug... ✅")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 40%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 50%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 75%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - 100%")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Co")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Comple")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed ")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed Ins")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed Instal")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed Installi")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed Installing")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Completed Installing ✅")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Wel")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcom")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome T")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To B")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To Bagu")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To Baguette")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To Baguette Ma")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To Baguette Maker")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖 - Welcome To Baguette Maker!")
        await msg.edit(embed=e37) 

        e37 = discord.Embed(color=discord.Color(0x2f3136), description="🥖")
        await msg.edit(embed=e37) 





    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if ctx.author.id == member.id:    
            await ctx.send(f"{ctx.author.mention} hugs himself! :3\n") 
            await ctx.send("https://i.imgur.com/PSIj19Q.png")
            await ctx.author.send(f"You hugged Yourself you qt :3")
        else:     
            await ctx.send(f"{ctx.author.mention} hugs {member.mention}!\n")
            await ctx.send("https://i.imgur.com/PSIj19Q.png")
            await member.send(f"{ctx.author.mention} hugged you :3")
            await ctx.author.send(f"You hugged {member.mention}")


    @commands.command()
    async def ad(self, ctx):
        await ctx.send("Today's bot is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2019 and it's totally free! Currently almost 10 million users have joined Raid over the last six months, and it's one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them's a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It's easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the bot's description, click on the special links and you'll get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I'll see you there!")


    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx):
        responses = [
                  "It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes - definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
        await ctx.send(f"{random.choice(responses)} {ctx.author.name}")



def setup(bot):
    bot.add_cog(fun(bot))
