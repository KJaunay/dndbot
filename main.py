import discord
import os


client = discord.Client()

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
    
token = os.environ['DISCORDBOTTOKEN1']
client.run(token)