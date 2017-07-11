import discord
from discord.ext import commands

class Obey:
    """This coq allows claiming ownership without console interaction. Use it with care!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.serverowner_or_permissions(administrator=True)
    async def obey(self, ctx):
        """Request ownership!"""
        self.bot.settings.owner = ctx.message.author.id
        self.bot.settings.save_settings()

def setup(bot):
    bot.add_cog(Obey(bot))
