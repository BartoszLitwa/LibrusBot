import discord
import librus

from discord.ext import commands
from datetime import datetime

class LibrusCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['oceny'])
    async def grades(self, ctx, *,teacher):
        async with ctx.message.channel.typing():
            embed = discord.Embed(
                title = f'Oceny - {teacher}',
                colour = discord.Colour.green(),
            )

            for k,v in librus.GetGradesByTeacher(teacher).items():
                embed.add_field(name=v, value=k, inline=False)
        
            await ctx.message.channel.send(embed=embed)

    @commands.command(aliases=['wolne', 'dniwolne'])
    async def freeDays(self, ctx):
        async with ctx.message.channel.typing():
            embed = discord.Embed(
                title = f'Dni Wolne',
                colour = discord.Colour.green(),
            )

            for k,v in librus.GetFreeDays().items():
                embed.add_field(name=k, value=v, inline=False)
        
            await ctx.message.channel.send(embed=embed)

    @commands.command(aliases=['lekcje', 'plan'])
    async def timeTable(self, ctx, day : str = 'dzisiaj'):
        async with ctx.message.channel.typing():
            embed = discord.Embed(
                title = f'Plan lekcji -{day}',
                colour = discord.Colour.green(),
            )

            for k,v in librus.GetLessons(1 if day in 'jutro' else 0).items():
                embed.add_field(name=k, value=v, inline=False)
        
            await ctx.message.channel.send(embed=embed)

    @commands.command(aliases=['sprawdziany', 'klasowki', 'testy', 'kartkowki'])
    async def exams(self, ctx, subject : str = ''):
        async with ctx.message.channel.typing():
            embed = discord.Embed(
                title = f'Exams',
                colour = discord.Colour.green(),
            )

            exams = librus.GetExams(subject).items()
            if len(exams) <= 0:
                embed.add_field(name='Brak nadchodzacych sprawdzianow', value='')
            else:
                for k,v in exams:
                    embed.add_field(name=k, value=v, inline=False)
        
            await ctx.message.channel.send(embed=embed)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case LibrusCommandsCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(LibrusCommandsCog(bot))