import discord

from discord.ext import commands
from datetime import datetime

class BotCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}ms Pong!')

    @commands.command()
    async def clear(self, ctx, amount = 5):
        embed = discord.Embed(
            title = 'Clear command',
            description = f'{amount} messages has been removed!',
            colour = discord.Colour.magenta()
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.channel.purge(limit = amount + 1)

        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        embed = discord.Embed(
            title = 'Bot will be stopped',
            description = f'Requested by {ctx.author.name} at {datetime.now().strftime("%H:%M:%S")}',
            colour = discord.Colour.red()
        )

        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.message.channel.send(embed=embed)
        await self.bot.logout()

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case BotCommandsCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(BotCommandsCog(bot))