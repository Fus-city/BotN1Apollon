import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')
token = 'your_tkn_here'


msg = message.content
athr = message.author

@bot.event
async def on_ready():
  print('Logged as')
  print(bot.user.name)
  print(bot.user.id)
  print('------------')

@bot.command
async def addblackword(pass_context=True):
  

@
