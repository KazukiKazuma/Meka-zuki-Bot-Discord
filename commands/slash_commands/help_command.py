import nextcord
from nextcord.ext import commands
from utils import help_command_utils, guild_utils
from config.bot_info import bot_language
from language import languages

from config.bot_info.bot_name import BOT_NAME
bot_display_name = BOT_NAME

code_language = languages.languages[bot_language.CHOSEN_LANGUAGE]


class HelpCog(commands.Cog):
    """Commands separated in categories and how to use them"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="help", description=code_language.help_command[f"Get help related to {bot_display_name}'s commands"], guild_ids=guild_utils.guild_ids)
    async def help(self,
            interaction: nextcord.Interaction,
            help_needed = nextcord.SlashOption(
                name=code_language.help_command["category"],
                description=code_language.help_command["Choose the subject you want to get help with"],
                required=True,
                choices=code_language.help_command["help_command_choice_list"]
            )
            ):
        something_wrong_embed = nextcord.Embed(
            description=code_language.help_command["Something went wrong, if the problem persists please contact a Guild Master"],
            color=0xe53b44
        )
        
        if help_needed == code_language.help_command["help_command_choice_list"][0]:
            help_command_utils.help_music.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar)
            await interaction.send(embed=help_command_utils.help_music, ephemeral=True)
        elif code_language.help_command["help_command_choice_list"][1]:
            help_command_utils.help_dice.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar)
            await interaction.send(embed=help_command_utils.help_dice, ephemeral=True)
        else:
            await interaction.send(embed=something_wrong_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(HelpCog(bot))