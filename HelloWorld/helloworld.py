from redbot.core import commands

class HelloWorld(commands.Cog):
    """A testing cog to test redcore and github repos"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        """Returns 'Hello World!' in the channel"""
        await ctx.send("Hello World!")
