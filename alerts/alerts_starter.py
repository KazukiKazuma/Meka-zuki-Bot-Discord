from nextcord.ext import commands


class SlashCommandsStarter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        STREAM_ALERTS_MODULES = [
            "stream_alerts"
        ]
        for module in STREAM_ALERTS_MODULES:
            bot.load_extension(f"alerts.stream_alerts.{module}")


def setup(bot):
    bot.add_cog(SlashCommandsStarter(bot))