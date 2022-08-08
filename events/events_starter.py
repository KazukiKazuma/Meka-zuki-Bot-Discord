from nextcord.ext import commands


class EventsStarter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        EVENTS_MODULES = [
            "on_join_server"
        ]
        for module in EVENTS_MODULES:
            bot.load_extension(f"events.events_modules.{module}")


def setup(bot):
    bot.add_cog(EventsStarter(bot))