import discord

from discord.ext import commands

class BotEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Game("Librus Bot :D")
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=game)
        print('Discord Bot is ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name = 'Test role')
        await member.add_roles(role)
        print(f'{member} has joined a server')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(BotEventsCog(bot))