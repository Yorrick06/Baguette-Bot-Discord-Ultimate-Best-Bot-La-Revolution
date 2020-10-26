import discord
import pymongo
import datetime
from discord.utils import get
from discord.ext import commands
from pymongo import MongoClient




class logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loggign = "mongodb+srv://User1:pqRq65D5nBGQYtgB@cluster0.d9kty.azure.mongodb.net/logging?retryWrites=true&w=majority"
      
    @commands.Cog.listener()
    async def on_message(self, ctx):
	    mango_url = self.loggign
	    cluster = MongoClient(mango_url)
	    db = cluster["databasel"]
	    collection = db["logging"]

	    guild = {"guild_id": ctx.guild.id}

	    if ctx.author == self.bot.user:
	    	return

	    if ctx.author.bot:
	    	return

	    if(collection.count_documents({}) == 0):
	    	guild = {"_id": ctx.guild.id, "guild_id": ctx.guild.id, "logging": False, "loggingChannel": None}
	    	collection.insert_one(guild)

	    if(collection.count_documents(guild) == 0):
	    	guild = {"_id": ctx.guild.id, "guild_id": ctx.guild.id, "logging": False, "loggingChannel": None}
	    	collection.insert_one(guild)
        


        


    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_guild=True) 
    async def logs(self, ctx, *, channel: discord.TextChannel):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild = db.find_one({"guild_id": ctx.guild.id})
        if guild is None:
            guild = db.find_one({"guild_id": ctx.guild.id})
            


        
        db.find_one_and_update({"guild_id": ctx.guild.id}, {"$set": {"logging": True}})

        db.find_one_and_update({"guild_id": ctx.guild.id}, {"$set": {"loggingChannel": channel.id}}) 
              
        embed = discord.Embed(
            color=discord.Color(0x2f3136),
            description=f"<#{channel.id}> is now your logging channel",
            timestamp=datetime.datetime.utcnow()
        ) 
        
        await ctx.send(embed=embed)

    @logs.command()   
    @commands.has_permissions(manage_guild=True)     
    async def channel(self, ctx):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild = db.find_one({"guild_id": ctx.guild.id})
        loggingChannel = guild["loggingChannel"]
        e = discord.Embed(title="Your logging channel is:", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"<#{loggingChannel}>")
        await ctx.send(embed=e)

    @logs.command()
    @commands.has_permissions(manage_guild=True)    
    async def disable(self, ctx):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]        
        db.find_one_and_update({"guild_id": ctx.guild.id}, {"$set": {"logging": False}})
        db.find_one_and_update({"guild_id": ctx.guild.id}, {"$set": {"loggingChannel": None}})
        await ctx.send("Logging is now disabled!")     




    @commands.Cog.listener()
    async def on_member_join(self, member):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": member.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        if member.bot:
            return               
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A new member joined!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"Name: {member}\nID: {member.id}")
        e.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=e)
#\nCreated at: {member.created_at.strftime("%a, %#d %B %Y")}

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": member.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        if member.bot:
            return            
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A new member left.", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"Name: {member}\nID: {member.id}")
        e.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=e)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": message.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        if message.author.bot:
            return            
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)	
        e = discord.Embed(title="A message got deleted!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"The message content: ```fix\n{message.content}\n```")
        e.set_footer(text=f"This message got deleted by {message.author.name}", icon_url=message.author.avatar_url)
        await channel.send(embed=e)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": after.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        if after.author.bot:
            return
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)	
        e = discord.Embed(title="A message got edited!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"The message content was: ```fix\n{before.content}\n```\nThe message content is now: ```fix\n{after.content}\n```")
        e.set_footer(text=f"This message got edited by {after.author.name}", icon_url=after.author.avatar_url)
        await channel.send(embed=e)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        message = reaction.message.content        
        message2 = reaction.message
        guild_id = db.find_one({"_id": message2.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        if reaction == discord.Embed():
            return

        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)	
        e = discord.Embed(title="A reaction got added", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"{user} added {reaction} to {message}.")
        await channel.send(embed=e)    


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        message = reaction.message.content        
        message2 = reaction.message
        guild_id = db.find_one({"_id": message2.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)	
        e = discord.Embed(title="A reaction got removed", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"{user} removed {reaction} from {message}.")
        await channel.send(embed=e)         

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": channel.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return

        g = self.bot.get_guild(id=guild_id2)
        lchannel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A channel got created!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"<#{channel.id}>")
        await lchannel.send(embed=e)
  
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": channel.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return

        g = self.bot.get_guild(id=guild_id2)
        lchannel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A channel got deleted!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"{channel.name}")
        await lchannel.send(embed=e)              

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": after.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return

        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)
        
        if before.name != after.name:
            e = discord.Embed(title="A channel got changed!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"**Name:** ```fix\n{before.name}\n```\n**To the name:** ```fix\n{after.name}\n```")
            await channel.send(embed=e)


        
        #e = discord.Embed(title="A channel got changed!", color=0x2f3136, description=f"```fix\n{before}\n```\nTo: ```fix\n{after}\n```")




    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": after.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return
        
        if before.color != after.color:
            e = discord.Embed(title="A role got changed!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"**Color**: ```fix\n{before.color}\n```\n**To Color:** ```fix\n{after.color}\n```")
        elif before.name != after.name:
            e = discord.Embed(title="A role got changed!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"**Name**: ```fix\n{before.name}\n```\n**To Name:** ```fix\n{after.name}\n```") 
        else:
            return
        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)
        #e = discord.Embed(title="A role got changed!", color=0x2f3136, description=f"```fix\n{before}\n```\nTo: ```fix\n{after}\n```")
        await channel.send(embed=e) 

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": role.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return

        g = self.bot.get_guild(id=guild_id2)
        channel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A new role got created!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"Name: {role.name}\nID: {role.id}\nColor: {role.color}\nPosition: {role.position}\nHoisted: {role.hoist}\nMentionable: {role.mentionable}")
        await channel.send(embed=e) 

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": role.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return

        g = self.bot.get_guild(id=guild_id2)
        lchannel = discord.utils.get(g.channels, id=loggingChannel)
        e = discord.Embed(title="A role got removed!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"Name: {role.name}\nID: {role.id}\nColor: {role.color}\nPosition: {role.position}\nHoisted: {role.hoist}\nMentionable: {role.mentionable}")
        await lchannel.send(embed=e) 

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        mango_url = self.loggign
        cluster = MongoClient(mango_url)
        db = cluster["databasel"]["logging"]

        guild_id = db.find_one({"_id": after.guild.id})
        loggingChannel = guild_id["loggingChannel"]
        loggingyes = guild_id["logging"]
        guild_id2 = guild_id["guild_id"] 
        if guild_id == None:
            return
        if loggingyes == False:
            return  

        if before.name != after.name:
            e = discord.Embed(title="A emote got updated!", color=0x2f3136, timestamp=datetime.datetime.utcnow(), description=f"```fix\n{before.name}\n```\nTo: ```fix\n{after.name}\n```")
        g = self.bot.get_guild(id=guild_id2)
        lchannel = discord.utils.get(g.channels, id=loggingChannel)
        #e = discord.Embed(title="A emote got updated!", color=0x2f3136, description=f"```fix\n{before}\n```\nTo: ```fix\n{after}\n```")
        await lchannel.send(embed=e) 




def setup(bot):
    bot.add_cog(logging(bot))