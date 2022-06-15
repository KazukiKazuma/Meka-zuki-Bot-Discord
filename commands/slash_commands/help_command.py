import nextcord
from nextcord.ext import commands
from utils import help_command_utils, guild_utils


class HelpCog(commands.Cog):
    """Commands separated in categories and how to use them"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="help", description="Obtenha ajuda relacionada aos comandos do Mekazuki", guild_ids=guild_utils.guild_ids)
    async def help(self,
            interaction: nextcord.Interaction,
            help_needed = nextcord.SlashOption(
                name="categoria",
                description="Escolha o assunto que quer receber ajuda",
                required=True,
                choices=["Música", "Rolagem de Dados"]
            )
            ):
        if help_needed == "Música":
            help_command_utils.help_music.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar)
            await interaction.send(embed=help_command_utils.help_music, ephemeral=True)
        elif help_needed == "Rolagem de Dados":
            help_command_utils.help_dice.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar)
            await interaction.send(embed=help_command_utils.help_dice, ephemeral=True)
        else:
            await interaction.send("Aconteceu algo de errado, tente novamente noutra ocasião.")


def setup(bot):
    bot.add_cog(HelpCog(bot))