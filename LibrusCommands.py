import discord
import librus

from discord.ext import commands

class LibrusCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def grades(self, ctx, *,teacher):
        async with ctx.message.channel.typing():
            embed = discord.Embed(
                title = f'Oceny - {teacher}',
                colour = discord.Colour.green(),
            )

            for grade in librus.GetGrades(teacher):
                embed.add_field(name=grade[3::], value=grade[:3:], inline=False)
        
            await ctx.message.channel.send(embed=embed)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(LibrusCommandsCog(bot))