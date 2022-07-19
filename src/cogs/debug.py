import discord
from discord.ext import commands, slash_command


class Debug(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('%g has logged in' % (self.bot))
        print('ID: %g' % (self.bot.user.id))
        print('Logged in and ready!')

    @discord.slash_command()
    

    