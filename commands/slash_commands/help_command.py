import nextcord
from nextcord.ext import commands
from utils import help_command_utils


class HelpCog(commands.Cog):
    """Commands separated in categories and how to use them"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="help", description="Obtenha ajuda relacionada aos comandos do Mekazuki")
    async def help(self,
            interaction: nextcord.Interaction,
            help_needed = nextcord.SlashOption(
                name="categoria",
                description="Escolha o assunto que quer receber ajuda",
                required=True,
                choices=["Música"]
            )
            ):
        if help_needed == "Música":
            help_command_utils.help_music.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar)
            await interaction.send(embed=help_command_utils.help_music, ephemeral=True)
        else:
            await interaction.send("Aconteceu algo de errado, tente novamente noutra ocasião.")


def setup(bot):
    bot.add_cog(HelpCog(bot))