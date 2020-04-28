import discord
import random
import info

from discord.ext import commands

bot = commands.Bot(command_prefix='?')
token = info.settings[2]

# this specifies what extensions to load when the bot starts up
startup_extensions = ['BotEvents', 'BotCommands', 'LibrusCommands']

if __name__ == "__main__":
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception:
            print(f'Failed to load {ext} extension.')

bot.run(token, bot=True, reconnect=True)