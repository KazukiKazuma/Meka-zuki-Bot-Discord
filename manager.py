from nextcord.ext import commands
from alerts.stream_alerts.stream_alerts import StreamAlert


class Manager(commands.Cog):
    """Manage things"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-------------------------\nEstou online como {self.bot.user}\n-------------------------")
        StreamAlert.send_alert_message.start(self)
        StreamAlert.update_alert_message.start(self)
        
        


def setup(bot):
    bot.add_cog(Manager(bot))