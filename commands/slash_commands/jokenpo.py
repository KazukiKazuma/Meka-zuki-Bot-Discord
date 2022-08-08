from nextcord.ext import commands
import nextcord
import random
from utils import jokenpo_utils
from utils.commands_utils import command_modules, module_disabled_message


class JokenpoCog(commands.Cog):
    """Lets you play jokenpo with the bot"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="jokenpo", description="Jogue uma rodada de Jokenpo com o Mekazuki")
    async def jokenpo(self,
            interaction: nextcord.Interaction,
            player_hand = nextcord.SlashOption(
                name="esolha",
                description="Escolha a mão que vai jogar",
                required=True,
                choices=["Pedra", "Papel", "Tesoura"]
            )
            ):
        if command_modules['Jokenpo'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        bot_hand = ["Pedra", "Papel", "Tesoura"]
        bot_choice = random.choice(bot_hand)
        if player_hand == "Pedra" and bot_choice == "Papel":
            await interaction.send(embed=jokenpo_utils.player_lose_prock_bpaper, delete_after=30)
        elif player_hand == "Pedra" and bot_choice == "Tesoura":
            await interaction.send(embed=jokenpo_utils.player_win_prock_bscissors, delete_after=30)
        elif player_hand == "Pedra" and bot_choice == "Pedra":
            await interaction.send(embed=jokenpo_utils.player_draw_prock_brock, delete_after=30)
        elif player_hand == "Papel" and bot_choice == "Tesoura":
            await interaction.send(embed=jokenpo_utils.player_lose_ppaper_bscissors, delete_after=30)
        elif player_hand == "Papel" and bot_choice == "Pedra":
            await interaction.send(embed=jokenpo_utils.player_win_ppaper_brock, delete_after=30)
        elif player_hand == "Papel" and bot_choice == "Papel":
            await interaction.send(embed=jokenpo_utils.player_draw_ppaper_bpaper, delete_after=30)
        elif player_hand == "Tesoura" and bot_choice == "Pedra":
            await interaction.send(embed=jokenpo_utils.player_lose_pscissors_brock, delete_after=30)
        elif player_hand == "Tesoura" and bot_choice == "Papel":
            await interaction.send(embed=jokenpo_utils.player_win_pscissors_bpaper, delete_after=30)
        elif player_hand == "Tesoura" and bot_choice == "Tesoura":
            await interaction.send(embed=jokenpo_utils.player_draw_pscissors_bscissors, delete_after=30)


def setup(bot):
    bot.add_cog(JokenpoCog(bot))