import discord
import datetime
from datetime import time
from discord.ext import commands
from discord.activity import Spotify

class spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["baguettify"])
    async def spotify(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
 

        if member.activity is None or member.activity != "Spotify":
            embed = discord.Embed(
                title="Baguettify",
                color=discord.Color(0x2f3136),
                description=f"<:SwitchOff:739752271973187675> {member.mention} is currently not using Baguettify."
            )
        
        for activity in member.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                   title=f"{member.name}#{member.discriminator}'s Baguettify",
                   color=discord.Color(0x2f3136),
                   description=f"Showing the current song {member.mention} is listening to."
                )
                embed.add_field(name="Song Title", value=f"{activity.title}")
                embed.add_field(name="Song  Album", value=f"{activity.album}")


                if len(activity.artists) == 1:
                    embed.add_field(name="Artist", value=f"{activity.artist}")
                else:
                    artists = ""
                    for artist in activity.artists:
                        artists += f"{artist}\n"
                    embed.add_field(name="Artists", value=artists)

                embed.add_field(name="Song Link:", value=f"[Click here to listen to this song!](https://open.spotify.com/track/{activity.track_id})")
                embed.add_field(name="Started listening at:", value=f"{activity.created_at}")
                embed.set_thumbnail(url=activity.album_cover_url)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(spotify(bot))