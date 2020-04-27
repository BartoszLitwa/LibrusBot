import discord
import random
import librus
import info
from discord.ext import commands

client = commands.Bot(command_prefix='?')
token = info.settings[2]
@client.event
async def on_ready():
    print('Discord Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms Pong!')

@client.command()
async def grades(ctx, *,teacher):
    await ctx.send(librus.GetGrades(teacher))

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['hello', 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7']
    ctx.send(f'Question: {question} /n Answer:{random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def stop(ctx):
    await ctx.send('Bot will be stopped')
    await client.logout()

client.run(token)