import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

bot.load_extension("commands")

bot.run(os.environ['DISCORDBOTTOKEN1'])