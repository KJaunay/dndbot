import discord
import os
from discord.ext import commands
from replit import db

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='dnd', help='Displays a welcome message with an example of how to use this bot') 
async def dnd(ctx):
  response="Hello! I am D&DBot. I can help you manage your campaign. Try typing !help to show the commands that are available. Each command will have a subcommand such as glossary add <person> <description>"
  await ctx.send(response)

@bot.command(name='glossary', help='Displays descriptions of people, places or things')
async def glossary(ctx):
  response="This is the glossary"
  await ctx.send(response)


'''
#client = discord.Client()

@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content
  if msg.startswith("!hello"):
    await message.channel.send("Hello there!")

  if msg.startswith("!dwarf"):
    await message.channel.send(db["dwarf"])
''' 

token = os.environ['DISCORDBOTTOKEN1']
bot.run(token)