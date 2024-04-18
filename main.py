import discord 
from discord.ext import commands, tasks
from discord import app_commands
import os 
# import datetime, pytz

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

fabio = "https://itforum.com.br/wp-content/uploads/2022/12/grupo-viasoft-CEO-baixa.jpg"

igor = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpGwa-qSp0h-AhLM-n9OKgoLrV5ZFbffeaL9yy8e-T7A&s"

ham = 'https://images-ext-1.discordapp.net/external/u-C40Ly0GeCNX9_OsOcY0gfoKUwFLSyDeYcNmT5VARQ/https/media.tenor.com/INGrPqw8LKoAAAPo/alvin-and-the-chipmunks-zegoyah.mp4'

marcio = 'https://images-ext-1.discordapp.net/external/7-9hmbwL3nwBReTQamHhBSEQGktuYlro9YI_39_9ukc/https/media.tenor.com/DRg_BNVnnlUAAAPo/showdebola-marcioemarcelo.mp4'


palavras_proibidas = [
    "daniel",
    "DANIEL",
    "DaNiEl",
    "dAnIeL",
    "DAnIeL",
    "@Daniel Brisch Cibolli"
]

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.author.display_name == 'Igor José' or message.author == 'igor.jose':
        if any(palavra in message.content.lower() for palavra in palavras_proibidas.lower()):
            await message.delete()
       

    if 'fabio' in message.content.lower():
        await message.channel.send(fabio)
        await message.channel.send('me empresta 100zão? 😥')

    if 'igor' in message.content.lower():
        await message.channel.send(igor)

    if 'hammster' in message.content.lower():
        await message.channel.send(ham)

    if 'marcio' in message.content.lower():
        await message.channel.send(marcio)

# @bot.command()
# async def abraco(ctx:commands.Context, nome:str):
#     meu_embed = discord.Embed(title = 'Olha que fofo', description=f'')
#     imagem_arquivo = discord.File('img/foxy.jpg', 'foxy.jpg')
#     thumb_embed = discord.File('img/pupet.jpg', 'pupet.jpg')
#     foto = discord.File('img/iconPlague.png', 'foto.png')
    
#     meu_embed.color = discord.Color.pink()

#     meu_embed.set_image(url="hug")

#     await ctx.reply(files=hug, embed=meu_embed)

@bot.event
async def on_ready():
    print('i am ready')

bot.run('')
