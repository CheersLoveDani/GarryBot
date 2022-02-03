import discord
from discord.ext import commands, tasks
import time
from time import sleep
import cleverbot



client = commands.Bot(command_prefix = 'Garry ')

@client.event
async def on_ready():
    print('Garry is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has entered the realm of Garry.')
    await ctx.send(f'Welcome {ctx.author.display_name} to the world of Garry.')
    sleep(2)
    await ctx.send('Bitch')

@client.command()
async def hey(ctx):
    print(f'Garry is insulting {ctx.author.display_name}')
    await ctx.send('Fuck off')

@client.command()
async def why(ctx):
    await ctx.send(f'Fuck you {ctx.author.display_name}')
    print(f'Garry is insulting {ctx.author.display_name}')
    sleep(2)
    await ctx.send('Bitch')


@client.command()
async def insultspeed(ctx):
    await ctx.send(f'I hate you in {round(client.latency * 1000)}ms')
    print(f'Garry insulted {ctx.author.display_name} in {round(client.latency * 1000)}ms')
    
@client.command()
async def speaktome(ctx, arg):
    print(f'Gary is replying to {ctx.author.display_name} saying {arg}')
    await ctx.send(cleverbot(arg, session="How are you?"))


client.run('ODAzNzYzNDQ4MjY1NzAzNDY2.YBChCw.h_rTAo8xiWbogZC_yM9RuBTpvzg')
