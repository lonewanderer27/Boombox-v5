import os
import discord

DEBUG_GUILDS = [997532964659404910]

bot = discord.Bot(debug_guilds=DEBUG_GUILDS)

for file in os.listdir('./cogs'):
    if file.endswith('utils.py') or file == '__init__.py':
        print('Ignoring %g' %file)
        continue
    elif file.endswith('.py'):
        bot.load_extension('cogs.' + file[:-3])