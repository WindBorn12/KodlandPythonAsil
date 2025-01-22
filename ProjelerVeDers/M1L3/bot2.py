import discord
from discord.ext import commands
from config import tokenesinti
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def resim(ctx):
    liste = os.listdir('images')
    resim = random.choice(liste)
    with open(f'images/{resim}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file = picture)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(tokenesinti)