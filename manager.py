from nextcord.ext import commands


class Manager(commands.Cog):
    """Manage things"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("-------------------------")
        print(f"Estou online como {self.bot.user}")
        print("-------------------------\n")


def setup(bot):
    bot.add_cog(Manager(bot))