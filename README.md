
# **Discord music bot**
Music bot for discord that can be run on your machine. That bot can playing music playlist from your local storage (defult: *C:\Music*).

# Installing
Python 3.5.3 or higher is required.

To run this bot you will need this python modules:
* pip install discord.py
* pip install PyNaCl
* pip install ffmpeg

Also you will need to change the name and token of the bot (changing the command prefix and your path to the music folder is optional) in bot.py.

> path = 'C:\\Music'
> 
> token = 'Put your token here'
> 
> botName = 'Name of your bot#1111'
> 
> bot = commands.Bot(command_prefix = '.')

# Help
For now the bot have only this commands: 
* ***.join**  - enter the bot to voice channel where you are*
* ***.leave** - the bot will stop playing and exit the voice channel*
* ***.play**  - the bot will start play music from your playlist in a random order*
* ***.next**  - skip currently playing music*

In a future i'll rework some stuff and will add more commands...
