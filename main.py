import discord 
from discord.ext import commands, tasks
from discord import app_commands
import os 
# import yt_dlp as youtube_dl
import youtube_dl
from youtube_dl import YoutubeDL
# import datetime, pytz

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

fabio = "https://itforum.com.br/wp-content/uploads/2022/12/grupo-viasoft-CEO-baixa.jpg"

igor = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpGwa-qSp0h-AhLM-n9OKgoLrV5ZFbffeaL9yy8e-T7A&s"


palavras_proibidas = [
    "daniel",
    "danlel",
    "@daniel brisch cibolli",
    "daniéu"
    ]

@bot.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()

@bot.command()
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()

@bot.command()
async def play(ctx, url):
    if not ctx.voice_client:
        await ctx.send("Eu preciso estar conectado a um canal de voz para tocar música.")
        return

    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'verbose': True
    }

    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']  
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            ctx.voice_client.play(source, after=lambda e: print('Erro no player: %s' % e) if e else None)
            await ctx.send(f"Tocando: {info['title']}")
        except Exception as e:
            await ctx.send(f"Ocorreu um erro ao processar este vídeo: {e}")

@bot.command()
async def embed_igor(ctx:commands.Context):
    meu_embed = discord.Embed(title = 'Viasofter', description='viadinho', color=discord.Color.red())
  
    meu_embed.set_author(name='Igor')
    meu_embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpGwa-qSp0h-AhLM-n9OKgoLrV5ZFbffeaL9yy8e-T7A&s")
    meu_embed.set_thumbnail(url='https://s3.sa-east-1.amazonaws.com/remotar-assets-prod/company-profile-pictures/cl6ev46xg001z042q0q9z1kn2.jpg')

    await ctx.reply(embed=meu_embed)

@bot.command()
async def stupid(ctx:commands.Context):
    await ctx.reply('Stupid flanders')

# @bot.command()
# async def gay(ctx:commands.Context):
#     await ctx.reply('https://giphy.com/gifs/love-kiss-gays-2aHPr6w2qrsxa')

@bot.event
async def on_message(message):
    if 'fabio' in message.content.lower():
        message.channel.send(fabio)


    if message.author.display_name == 'Igor José' or message.author == 'igor.jose':
        if any(palavra.lower() in message.content.lower() for palavra in palavras_proibidas):
            await message.delete()       

    await bot.process_commands(message)


@bot.event
async def on_message_edit(before, after, message):
    if before.content != after.content:  
        if message.author.display_name == 'Igor José' or message.author == 'igor.jose':
            if any(palavra.lower() in message.content.lower() for palavra in palavras_proibidas):
                await message.delete()    

@bot.event
async def on_ready():
    print('i am ready')
    #channel = bot.get_channel(1186282610658381936)
    # await channel.send('uma vez o igor foi cantar e cantou bem assim 1,2,3, 5 rola na minha boca de uma vez')

bot.run('')
