import discord
import pymongo
import os
import random
import asyncio
import asyncpg

from discord.ext import tasks, commands
from discord.utils import get
from pymongo import MongoClient


class currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mongodb = "mongodb+srv://User1:pqRq65D5nBGQYtgB@cluster0.d9kty.azure.mongodb.net/currency?retryWrites=true&w=majority"
        self.blacklisted = [
            ("No one", 697879596040716455)
        ]

    async def drops(self, message):		
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]

	    #dropnumb = random.randint(1, 2)
	    amountofmoney = random.randint(100, 500)
	    baguette = "🥖"
	    #if dropnumb == 1:
	    e = discord.Embed(title="Some cash dropped!", color=0x2f3136, description=f"Grab {amountofmoney} clicking on 🥖 now!")
	    drop = await message.channel.send(embed=e)
		
	    def check(reaction, user):
		    return user == message.author and reaction.emoji == '🥖'

	    await drop.add_reaction(baguette)
	    try:
		    reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)
	    except asyncio.TimeoutError:
		    e = discord.Embed(title="You were too late :(", color=0x2f3136, description=f"Sad, try it next time!")
		    await drop.edit(emebd=e)
		    return
		
	    
	    #await reaction.remove(user)
	    await reaction.message.clear_reactions()	
	    e2 = discord.Embed(title=f"Congrats {message.author.name}!", color=0x2f3136, description=f"You grabbed {amountofmoney}!")
	    #await msg.edit(content="hey")
	    await drop.edit(embed=e2)	
	    db.update_one({"_id": message.author.id}, {"$inc": {"Money": amountofmoney}}, upsert=True)								   		    
	    #else: 
		    #return


    @commands.Cog.listener()
    async def on_message(self, message):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]
	    
	    author_id = message.author.id
	    user_id = {"_id": author_id}
	    if message.author == self.bot.user:
	    	return
	    if message.author.bot:
	    	return

	    thedropnumber = (0, 150)
	    if thedropnumber == 0:
		    await self.drops(message)
		    print(f"The lucky number for drops was.... {thedropnumber}")			



	    #if(db.count_documents({}) == 0):
	    #	user_info = {"_id": ctx.author.id, "Money": 10, "Color": "discord.Color(0x2f3136)", "MP": 1, "Red": False, "Blue": False, "Green": False, "Gold": False}
	    #	db.insert_one(user_info)

	    if(db.count_documents(user_id) == 0):
	    	user_info = {"_id": message.author.id, "Money": 0, "Color": "discord.Color(0x2f3136)", "MP": 1, "Red": False, "Blue": False, "Green": False, "Gold": False, "Passive": False}
	    	db.insert_one(user_info)




		    





    @commands.command()
    async def moneyez(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        if ctx.author.id == 457553415807959050:
	        while True:
	    	    mango_url = self.mongodb
	    	    cluster = MongoClient(mango_url)
	    	    db = cluster["databasel"]["currency"]
	    	    cash = 1
	    	    db.update_one({"_id": ctx.member.id}, {"$inc": {"Money": cash}}, upsert=True)	       
	    	    await asyncio.sleep(0.2)    
        else:
	        return




    @commands.command(aliases=["bal"])
    async def balance(self, ctx, member: discord.Member = None):
	    member = ctx.author if not member else member
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  	


	    user = db.find_one({"_id": member.id})
	    rank = user["Money"]
	    color = user["Color"]
	    mp = user["MP"]	

	    if color == "discord.Color(0x2f3136)":
	        e = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color(0x2f3136), description=f"Money: {int(rank)}")
	        e.set_footer(text=f"This user got a multiplier of {mp}")
	        await ctx.send(embed=e)		
	    elif color == "discord.Color(0x2EF22B)":
	        e = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color(0x2EF22B), description=f"Money: {int(rank)}")
	        e.set_footer(text=f"This user got a multiplier of {mp}")	
	        await ctx.send(embed=e)			
	    elif color == "discord.Color(0x2E2BF2)":
	        e = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color(0x2E2BF2), description=f"Money: {int(rank)}")
	        e.set_footer(text=f"This user got a multiplier of {mp}")
	        await ctx.send(embed=e)			
	    elif color == "discord.Color(0xF22B2B)":
	        e = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color(0xF22B2B), description=f"Money: {int(rank)}")
	        e.set_footer(text=f"This user got a multiplier of {mp}")
	        await ctx.send(embed=e)	
	    elif color == "discord.Color(0xF2DD2B)":
	        e = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color(0xF2DD2B), description=f"Money: {int(rank)}")
	        e.set_footer(text=f"This user got a multiplier of {mp}")
	        await ctx.send(embed=e)							
	    else:
	        await ctx.send("Oops, something went wrong")

	


    @commands.command()
    @commands.cooldown(1, 60*10, commands.BucketType.user)	
    async def work(self, ctx):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    randomnum = random.randint(100, 1000)
	    workingn = random.randint(1, 10)
	    user = db.find_one({"_id": ctx.author.id})		
	    Mp = user["MP"]
	    passive = user["Passive"]
	    if passive == True:
		    Cash = int(randomnum*Mp*0.75)		
	    else:
		    Cash = int(randomnum*Mp)
	    if workingn == 1:
		    working = f"{ctx.author.mention} worked on some channels and earned {Cash}."
	    elif workingn == 2:
		    working = f"{ctx.author.mention} sold a server and earned {Cash}."
	    elif workingn == 3:
		    working = f"{ctx.author.mention} managed to sell nitro for a higher price and earn {Cash}."
	    elif workingn == 4:
		    working = f"{ctx.author.mention} got some YouTube views and earned {Cash}."
	    elif workingn == 5:
		    working = f"{ctx.author.mention} managed to hack someone's paypal and steal {Cash}."
	    elif workingn == 6:
		    working = f"{ctx.author.mention} realised they can steal their mommy's credit card and gainded {Cash}."
	    elif workingn == 7:
		    working = f"{ctx.author.mention} played te lottery and gained {Cash}."
	    elif workingn == 8:
		    working = f"{ctx.author.mention} stole Yorrick's bank account and gained {Cash}. (he should never do that again)"	
	    elif workingn == 9:
		    working = f"{ctx.author.mention} sold baguette's in France and gained {Cash}."		
	    elif workingn == 10:
		    working = f"{ctx.author.mention} worked on a html site and earned {Cash}."		
	    else:
		    await ctx.send("error..")

	    embed = discord.Embed(title="Baguette Cash", color=discord.Color(0x2f3136), description=f"{working}") 
	    await ctx.send(embed=embed)

	    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": Cash}}, upsert=True)


    @commands.command(aliases=["inv"])
    async def inventory(self, ctx):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    user = db.find_one({"_id": ctx.author.id})	

	    Red = user["Red"]
	    Green = user["Green"]
	    Blue = user["Blue"]
	    Gold = user["Gold"]


	    if Red == True:
		    red = "True"
	    else: 
		    red = "False"
		
	    if Green == True:
		    green = "True"
	    else:
		    green = "False"

	    if Blue == True:
		    blue = "True"
	    else:
		    blue = "False"

	    if Gold == True:
		    gold = "True"
	    else:
		    gold = "False"

	    e = discord.Embed(title=f"{ctx.author.name}'s inventory", color=discord.Color(0x2f3136), description=f"You got:\nRed: {red}\nBlue: {blue}\nGreen: {green}\nGold: {gold}")
	    await ctx.send(embed=e)

    @commands.command()
    async def select(self, ctx, select: str):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    user = db.find_one({"_id": ctx.author.id})	

	    Red = user["Red"]
	    Green = user["Green"]
	    Blue = user["Blue"]
	    Gold = user["Gold"]
		
	    if select == "red":
		    if Red == True:
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Color": "discord.Color(0xF22B2B)"}}, upsert=True)
			    await ctx.send("Done!")
		    else:
			    await ctx.send("Sadly you dont got this color, use `b!inv` to see your colors.")
	    elif select == "blue":
		    if Blue == True:
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Color": "discord.Color(0x2E2BF2)"}}, upsert=True)
			    await ctx.send("Done!")
		    else:
			    await ctx.send("Sadly you dont got this color, use `b!inv` to see your colors.")		
	    elif select == "green":
		    if Green == True:		
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Color": "discord.Color(0x2EF22B)"}}, upsert=True)
			    await ctx.send("Done!")
		    else:
			    await ctx.send("Sadly you dont got this color, use `b!inv` to see your colors.")		
	    elif select == "gold":
		    if Gold == True:
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Color": "discord.Color(0xF2DD2B)"}}, upsert=True)
			    await ctx.send("Done!")
		    else:
			    await ctx.send("Sadly you dont got this color, use `b!inv` to see your colors.")	
	    elif select == "reset":
		    db.update_one({"_id": ctx.author.id}, {"$set": {"Color": "discord.Color(0x2f3136)"}}, upsert=True)
		    await ctx.send("Done!")
	    else:
		    await ctx.send("Something went wrong.")

    @commands.command()
    async def shop(self, ctx):
	    e = discord.Embed(title="The shop", color=discord.Color(0x2f3136), description="1. Red Color - $40000\n2. Green Color - $50000\n3. Blue Color - $60000\n4. Gold Color - $80000\n5. Multipliers - $10000") 
	    await ctx.send(embed=e)		

    @commands.command()
    async def buy(self, ctx, number: int):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    user = db.find_one({"_id": ctx.author.id})	
	    usermoney = user["Money"]
	    
	    redcost = 40000
	    greencost = 50000
	    bluecost = 60000
	    goldcost = 80000
	    mpcost = 10000

	    if number == 1:
		    if user["Red"] == True:
			    await ctx.send("You already got this color!")
			    return
		    elif redcost > usermoney:
			    await ctx.send("Sadly you do not got enough money.")				
		    else:
			    await ctx.send("Done! You bought the color Red.")
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Red": True}}, upsert=True)
			    boughtred = 40000
			    usermoney -= boughtred
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)
	    elif number == 2:
		    if user["Green"] == True:
			    await ctx.send("You already got this color!")
		    elif greencost > usermoney:
			    await ctx.send("You do not got enough money.") 
		    else:
			    await ctx.send("Done! You bought the color Green.")
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Green": True}}, upsert=True)
			    boughtgreen = 50000
			    usermoney -= boughtgreen
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)	
	    elif number == 3:
		    if user["Blue"] == True:
			    await ctx.send("You already got this color!")
		    elif bluecost > usermoney:
			    await ctx.send("Sadly you do not got enough money.")
		    else:			 
			    await ctx.send("Done! You bought the color Blue.")
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Blue": True}}, upsert=True)
			    boughtblue = 60000
			    usermoney -= boughtblue
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)	
	    elif number == 4:
		    if user["Gold"] == True:
			    await ctx.send("You already got this color!")
		    elif goldcost > usermoney:
			    await ctx.send("Sadly you do not got enough money.")
		    else:
			    await ctx.send("Done! You bought the color Gold.")
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Gold": True}}, upsert=True)
			    boughtgold = 800000
			    usermoney -= boughtgold
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)
	    elif number == 5:
		    if user["MP"] == 1:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 1.25 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 1.25}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)		
		    elif user["MP"] == 1.25:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 1.50 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 1.50}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)		
		    elif user["MP"] == 1.50:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 1.75 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 1.75}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)		
		    elif user["MP"] == 1.75:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 2 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 2}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)		
		    elif user["MP"] == 2:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 2.25 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 2.25}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)		
		    elif user["MP"] == 2.25:
			    if mpcost > usermoney:
				    await ctx.send("Sadly you do not got enough money.")
			    else:
				    await ctx.send("Done! You bought the 1.25 multiplier!")
				    db.update_one({"_id": ctx.author.id}, {"$set": {"MP": 2.50}}, upsert=True)
				    usermoney -= mpcost
				    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": usermoney}}, upsert=True)
				    await ctx.send("This also is the final upgrade of multipliers!")	
		    elif user["MP"] == 2.50:
			    await ctx.send("This was the final upgrade.")
	    else:
		    await ctx.send("Select a number between 1 and 4!")



    @commands.command(aliases=["moneyleaderboard", "mlb"])
    async def moneylb(self, ctx):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]

	    players = []

	    cursor = db.find({})
	    cursor.sort("Money", -1).limit(10)

	    for document in cursor:
	        for member in ctx.guild.members:
	            if document["_id"] != member.id:
	                pass
	            else:
	                players.append(document)

	    embed = discord.Embed(title="Top Members money	", color=discord.Color(0x2f3136))

	    for e, player in enumerate(players, 1):
	        if e == 1:
	            medal = "🥇"
	        elif e == 2:
	            medal = "🥈"
	        elif e == 3:
	            medal = "🥉"
	        else:
	            medal = ""


	       
	        grapes = player["Money"]
	        xps = player["MP"]
	        passive = player["Passive"]
	        member = discord.utils.get(ctx.guild.members, id=player["_id"])

	        if member is not None:
	            name = str(member)
	        else:
	            name = str(self.bot.get_user(player["_id"]))

	        name = name if name != "None" else "*Unknown*"

	        embed.add_field(name=f"{e}. {medal} {name}", value=f"Multiplier {xps}, Money {int(grapes)}, Passive mode {passive}", inline=False)

	    await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)		
    async def daily(self, ctx):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    user = db.find_one({"_id": ctx.author.id})
	    if user["Money"] == 0:
		    await ctx.send("You need to work first to claim your daily money!")
		    return
	    mp = user["MP"]
	    passive = user["Passive"]
	    dailycash = random.randint(1000, 1500)
	    fulldailycash = int(dailycash*mp)
	    if passive == True:
		    fulldailycash = int(dailycash*mp*0.75)		
	    else:
		    fulldailycash = int(dailycash*mp)							
	    e = discord.Embed(title="Daily cash claimed!", color=discord.Color(0x2f3136), description=f"You claimed {fulldailycash}!")
	    await ctx.send(embed=e)
	    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": fulldailycash}}, upsert=True)	    

    @commands.command(aliases=["cf"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def coinflip(self, ctx, coin: str, bet: int):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == self.blacklisted:
	        await ctx.send("Sadly you have been blacklisted.")
	        return  

	    user = db.find_one({"_id": ctx.author.id})
	    availablemoney = user["Money"]
	    mp = user["MP"]
	    passive = user["Passive"]
	    thecoin = random.randint(1, 2)
	    if passive == True:
		    cashgotten = int(bet*mp*0.75)
	    else:
		    cashgotten = int(bet*mp)			
	    if bet > availablemoney:
		    await ctx.send("You do not got that much money! Bet less.")
		    return
	    elif bet < 2500:
		    await ctx.send("You need to bet 2500 or higher!")
		    return
	    elif bet > 25000:
		    await ctx.send("You need to bet 25000 or lower!")
		    return
	    elif coin == "heads":
		    if thecoin == 1:
			    e = discord.Embed(title="It was Heads!", color=discord.Color(0x2f3136), description=f"You earned {cashgotten}.")
			    await ctx.send(embed=e)
			    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": cashgotten}}, upsert=True)	 
		    elif thecoin ==2:
			    await ctx.send("Sad, it was tails.")
			    availablemoney -= bet
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": availablemoney}}, upsert=True)	 
	    elif coin == "tails":
		    if thecoin == 1:
			    e = discord.Embed(title="It was Tails!", color=discord.Color(0x2f3136), description=f"You earned {cashgotten}.")
			    await ctx.send(embed=e)
			    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": cashgotten}}, upsert=True)	 
		    elif thecoin == 2:
			    await ctx.send("Sad, it was heads.")
			    availablemoney -= bet
			    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": availablemoney}}, upsert=True)	 
	    else: 
		    await ctx.send("You just catched a bug.")


    @commands.command()
    async def addmoney(self, ctx, member: discord.Member, amount: int):
	    member = ctx.author if not member else member	
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    if ctx.author.id == 457553415807959050:
		    db.update_one({"_id": member.id}, {"$inc": {"Money": amount}}, upsert=True)	 
		    await ctx.send(f"You added {amount} to {member}.")
	    else:
		    return

    @commands.command()
    async def removemoney(self, ctx, member: discord.Member, amount: int):
	    member = ctx.author if not member else member	
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    
	    user = db.find_one({"_id": member.id})
	    money = user["Money"]
	    if ctx.author.id == 457553415807959050:
		    money -= amount
		    db.update_one({"_id": member.id}, {"$set": {"Money": money}}, upsert=True)	 
		    await ctx.send(f"You removed {amount} from {member}.")
	    else:
		    return

    @commands.command()
    async def passive(self, ctx):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return 
	    user = db.find_one({"_id": ctx.author.id})
	    passive = user["Passive"]			
	    if passive == False:
		    db.update_one({"_id": ctx.author.id}, {"$set": {"Passive": True}}, upsert=True)					
		    await ctx.send(f"Done, you are now in passive mode.")
	    elif passive == True:
		    db.update_one({"_id": ctx.author.id}, {"$set": {"Passive": False}}, upsert=True)					
		    await ctx.send(f"Done, you are now out of passive mode.")
	    else:
		    return

    @commands.command()
    async def rob(self, ctx, member: discord.Member):
	    member = ctx.author if not member else member	
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return 
	    user = db.find_one({"_id": member.id})
	    user2 = db.find_one({"_id": ctx.author.id})
	    passive = user["Passive"]	
	    money = user["Money"]
	    money2 = user2["Money"]
	    passive2 = user2["Passive"]
	    cashrobbed = random.randint(2500, money)

	    if ctx.author.id == member.id:
		    await ctx.send("You can't rob yourself!")
	    elif passive == True:
		    await ctx.send("This user is in passive mode!")
	    elif passive2 == True:
		    await ctx.send("Disable passive mode to rob!")
	    elif 2500 > money2:
		    await ctx.send("You need atleast 2500$!")
	    elif 2500 > money:
		    await ctx.send("This user doesn't got a lot of money, it's not worth it.")
	    else:
		    await ctx.send(f"You just robbed {member.name} and stole {cashrobbed}!")
		    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": cashrobbed}}, upsert=True)
		    money -= cashrobbed
		    db.update_one({"_id": member.id}, {"$set": {"Money": money}}, upsert=True)		    

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)    	
    async def invest(self, ctx, amount: int, time: int):
	    mango_url = self.mongodb
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["currency"]   	

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return   
 

	    user = db.find_one({"_id": ctx.author.id})
	    luck1 = 100 - time
	    money = user["Money"]
	    money1 = amount / 0.75
	    money2 = amount * time / 0.5
	    

	    if luck1 == 1:
		    e = discord.Embed(title="Oops", color=0x2f3136, description=f"You just lost {int(money1)}.")
		    await ctx.send(embed=e)
		    money -= money1
		    db.update_one({"_id": ctx.author.id}, {"$set": {"Money": money}}, upsert=True)	
	    elif time == None:
		    e = discord.Embed(title="Oops", color=0x2f3136, description=f"You need to give an amount of time to invest! Must be less than 100.")
		    await ctx.send(embed=e)										
	    elif time > 100:
		    e = discord.Embed(title="Oops", color=0x2f3136, description="You cant use more time than 100. Yes this sounds stupid but you know what i mean. (hopefully)")
		    await ctx.send(embed=e)	
	    elif amount > money: 
		    e = discord.Embed(title="Oops", color=0x2f3136, description="You dont got that amount of money!")
		    await ctx.send(embed=e)	
	    elif amount < 0:
		    e = discord.Embed(title="Oops", color=0x2f3136, description="Invest more than 0!")
		    await ctx.send(embed=e)			  			
	    else:
		    e = discord.Embed(title="Nice!", color=0x2f3136, description=f"You just invested and got {int(money2)}!")
		    await ctx.send(embed=e)				
		    db.update_one({"_id": ctx.author.id}, {"$inc": {"Money": money2}}, upsert=True)	
		

def setup(bot):
    bot.add_cog(currency(bot))
