from nextcord.ext import commands


class CommandsStarter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        SLASH_COMMANDS_MODULES = [
            "delete_bot_message_command",
            "dice",
            "help_command",
            "jokenpo",
            "modules_command",
            "slash_talks"
        ]
        for module in SLASH_COMMANDS_MODULES:
            bot.load_extension(f"commands.slash_commands.{module}")
            
        STANDARD_COMMANDS_MODULES = [
            "minecraft_server_status",
            "new_member_verification_message",
            "registration_message"
        ]
        for module in STANDARD_COMMANDS_MODULES:
            bot.load_extension(f"commands.standard_commands.{module}")
            
        STREAMERS_ROLE_MESSAGES = [
            "daxlian_role_message",
            "scocotta_role_message"
        ]
        for streamer_message in STREAMERS_ROLE_MESSAGES:
            bot.load_extension(f"commands.standard_commands.streamer_roles_messages.{streamer_message}")


def setup(bot):
    bot.add_cog(CommandsStarter(bot))