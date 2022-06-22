from nextcord.ext import commands
from alerts import stream_alerts


class Manager(commands.Cog):
    """Manage things"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-------------------------\nEstou online como {self.bot.user}\n-------------------------")
        stream_alerts.StreamData.send_alert_message.start(self)
        stream_alerts.StreamData.update_alert_message.start(self)
        
        


def setup(bot):
    bot.add_cog(Manager(bot))