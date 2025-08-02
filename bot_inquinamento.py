import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def leggi(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        
with open('token.txt', 'r', encoding='utf-8') as f:
    token = f.read()
	#token = f.read().strip()

bot.run(token)
