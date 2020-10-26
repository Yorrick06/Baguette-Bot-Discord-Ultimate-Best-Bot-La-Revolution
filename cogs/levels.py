import discord
import json
import pymongo
import os
import math
import asyncio
from discord.ext import commands
from pymongo import MongoClient




class level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

	
    @commands.Cog.listener()
    async def on_message(self, ctx):
	    mango_url = "mongodb+srv://User1:pqRq65D5nBGQYtgB@cluster0.d9kty.azure.mongodb.net/level?retryWrites=true&w=majority"
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]
	    collection = db["level"]
	    author_id = ctx.author.id
	     

	    author = ctx.author

	    user_id = {"_id": author_id}

	    if ctx.author == self.bot.user:
	    	return

	    if ctx.author.bot:
	    	return

	    if(collection.count_documents({}) == 0):
	    	user_info = {"_id": author_id, "GuildID": ctx.guild.id, "Level": 1, "XP": 0}
	    	collection.insert_one(user_info)

	    if(collection.count_documents(user_id) == 0):
	    	user_info = {"_id": author_id, "GuildID": ctx.guild.id, "Level": 1, "XP": 0}
	    	collection.insert_one(user_info)


		

	    exp = collection.find(user_id)
	    for xp in exp:
	    	cur_xp = xp["XP"]

	    	new_xp = cur_xp + 1 

	    collection.update_one({"_id": author_id}, {"$set":{"XP":new_xp}}, upsert=True)

	    #await ctx.channel.send("1 xp up")

		
		
	    lvl = collection.find(user_id)
	    for levl in lvl:
	    	lvl_start = levl["Level"]

	    	new_level = lvl_start + 1

	    user = collection.find_one({"_id": ctx.author.id})
	    xp23 = user["Level"]

	    if xp23 == 1:
	    	morexp = round(5 * (1 ** 4 / 7) + 20) 
	    elif xp23 == 2:
	    	morexp = round(5 * (2 ** 4 / 7) + 50)         
	    elif xp23 == 3:
	    	morexp = round(5 * (3 ** 5 / 7) + 10)    
	    elif xp23 == 4:
	    	morexp = round(4 * (4 ** 5 / 7) + 20)  
	    elif xp23 == 5:
	    	morexp = round(8 * (5 ** 5 / 9) + 20)
	    elif xp23 == 6:
	    	morexp = round(4 * (6 ** 5 / 9) + 20)
	    elif xp23 == 7:
	    	morexp = round(3 * (7 ** 5 / 11) + 20)
	    elif xp23 == 8:
	    	morexp = round(3 * (8 ** 5 / 13) - 1700)
	    elif xp23 == 9:
	    	morexp = round(3 * (9 ** 5 / 13) - 5600)
	    elif xp23 == 10:
	    	morexp = round(6 * (10 ** 4 / 6))
	    else:
	    	morexp = round(5 * (xp23 ** 4 / 7))

	    if cur_xp >= morexp:
	    	collection.update_one({"_id": author_id}, {"$set":{"Level":new_level}}, upsert=True)
	    	await ctx.channel.send(f"{author.mention} has leveled up to {new_level}!")

    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
	    member = ctx.author if not member else member
	    mango_url = "mongodb+srv://User1:pqRq65D5nBGQYtgB@cluster0.d9kty.azure.mongodb.net/level?retryWrites=true&w=majority"
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["level"]

	    if ctx.author == self.bot.user:
	    	return
	    if ctx.author.bot:
	    	return    

	    user = db.find_one({"_id": member.id})
	    rank = user["Level"]
	    rank2 = user["XP"]
	   # color = user["Color"]


	    embed = discord.Embed(
			title=f"{member}'s rank.",
			color=discord.Color(0x2f3136),
			description=f"XP: {rank2}\nLevel: {rank}"
	    )
	    await ctx.send(embed=embed)
	
    @commands.command(aliases=["top", "lb"])
    async def leaderboard(self, ctx):
	    mango_url = "mongodb+srv://User1:pqRq65D5nBGQYtgB@cluster0.d9kty.azure.mongodb.net/level?retryWrites=true&w=majority"
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]["level"]

	    players = []

	    cursor = db.find({})
	    cursor.sort("XP", -1).limit(10)

	    for document in cursor:
	        for member in ctx.guild.members:
	            if document["_id"] != member.id:
	                pass
	            else:
	                players.append(document)

	    embed = discord.Embed(title="Top Members levels", color=discord.Color(0x2f3136))

	    for e, player in enumerate(players, 1):
	        if e == 1:
	            medal = "🥇"
	        elif e == 2:
	            medal = "🥈"
	        elif e == 3:
	            medal = "🥉"
	        else:
	            medal = ""


	       
	        grapes = player["XP"]
	        xps = player["Level"]
	        member = discord.utils.get(ctx.guild.members, id=player["_id"])

	        if member is not None:
	            name = str(member)
	        else:
	            name = str(self.bot.get_user(player["_id"]))

	        name = name if name != "None" else "*Unknown*"

	        embed.add_field(name=f"{e}. {medal} {name}", value=f"Level {xps}, XP {grapes}", inline=False)

	    await ctx.send(embed=embed)

	    





def setup(bot):
    bot.add_cog(level(bot))