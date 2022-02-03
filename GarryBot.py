import discord
from discord.ext import commands, tasks
import time
from time import sleep
from tokens import token
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Garry')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

client = commands.Bot(command_prefix = '/g ')


@client.event
async def on_ready():
    print('Garry is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has entered the realm of Garry.')
    await ctx.send(f'Welcome {ctx.author.display_name} to the world of Garry.')
    sleep(2)
    await ctx.send('Bitch')
    
@client.event
async def on_message(message):
    if ('Garry' in message.content or 'garry' in message.content):
        print(message.channel)
        await message.channel.send(chatbot.get_response(message.content))
    elif '/g ' in message.content:
        await client.process_commands(message)
    
@client.command(usage='Say hey to Garry')
async def hey(ctx):
    print(f'Garry is insulting {ctx.author.display_name}')
    await ctx.send('Fuck off')
    
@client.command()
async def helpmegarry(ctx):
    print(f'Garry is helping {ctx.author.display_name}')
    await ctx.send('No lmfao')
    sleep(2)
    await ctx.send('but do /g help if you really need some help... dumbass')

@client.command()
async def why(ctx):
    await ctx.send(f'Fuck you {ctx.author.display_name}')
    print(f'Garry is insulting {ctx.author.display_name}')
    sleep(2)
    await ctx.send('Bitch')


@client.command(usage='See how fast Garry is running today')
async def insultspeed(ctx):
    await ctx.send(f'I hate you in {round(client.latency * 1000)}ms')
    print(f'Garry insulted {ctx.author.display_name} in {round(client.latency * 1000)}ms')
    




client.run(token)
