import discord
import os
import random
from discord.ext import commands
from discord.utils import get

path = 'C:\\Music'
token = 'Put your token here'
botName = 'Name of your bot#1111'
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    global voice
    global num
    global message
    num = []
    print('Logged in as: ' + bot.user.name + '\n')

@bot.event
async def on_reaction_add(reaction, user):
    if (str(user) != "Music Bot (for test)#6010") and (str(reaction) == '⏭️'):
        voice = get(bot.voice_clients, guild=user.guild)
        if voice and voice.is_playing():
            print(f"Music skipped")
            voice.stop()

@bot.command(pass_contex=True, aliases=['joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice = await channel.connect()
    print(f"The bot has connected to {channel}\n")

@bot.command(pass_contex=True, aliases=['le','kick','ki'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    print(f"The bot has left the channel {channel}\n")
    await voice.disconnect()

@bot.command(pass_contex=True)
async def play(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.mp3' in file:
                files.append(os.path.join(r,file))

    for f in files:
        print(f)

    i=0
    while i<len(files):
        num.append(i)
        i = i + 1

    random.shuffle(num)

    reactions = ['⏭️']
    message = await ctx.send(":musical_note:Playing music:sparkles: ")
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await message.add_reaction(emoji or name)

    playNow(ctx, files, 0)
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.5

def playNow(ctx, files, i):
    if i < len(files):
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(files[num[i]]), after=lambda e: playNow(ctx, files, i+1))
        print(f"-> " + files[num[i]])
        del voice
    else:
        print(f"No more music in this list...")

@bot.command(pass_contex=True, aliases=['ne','skip','sk'])
async def next(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print(f"Music skipped")
        voice.stop()
        await ctx.send("Skipped")

bot.run(token)
