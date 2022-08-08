from nextcord.ext import commands


class TasksCommandsStarter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        REACTION_TASKS_MODULES = [
            "registration_message_reaction_handler"
        ]
        for module in REACTION_TASKS_MODULES:
            bot.load_extension(f"tasks.reaction_tasks.{module}")


def setup(bot):
    bot.add_cog(TasksCommandsStarter(bot))