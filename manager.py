from nextcord.ext import commands


class Manager(commands.Cog):
    """Manage things"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-------------------------\nEstou online como {self.bot.user}\n-------------------------")
        
        


def setup(bot):
    bot.add_cog(Manager(bot))