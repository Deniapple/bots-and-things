import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='--', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def ahh(ctx, count_ahh = 1):
    await ctx.send("ahh " * count_ahh)
@bot.command()
async def mem(ctx):
    pic_list = os.listdir("images")
    picture = random.choice(pic_list)
    with open(f"images/{picture}" , mode = "rb") as meme:
        meme_pic = discord.File(meme)
    await ctx.send(file = meme_pic)

oneriler = [
    "pet şişeleri saksı yapabilirsiniz",
    "plastik ve metal atıkları birleştirip süs eşyası olarak kullanabilirsiniz",
    "ilaç kutusunu kürdan ve pet şişe kapağı ile araba modeline çevirebilirsiniz",
    "gıda atıklarını toplayıp gübre olarak kullanabilirsiniz",
    "kırık cam parçalarından sanat icra edebilirsin"
]

@bot.command()
async def oneri(ctx):
    await ctx.send(random.choice(oneriler))

bot.run("ENTER TOKEN")