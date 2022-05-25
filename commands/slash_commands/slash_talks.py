from nextcord.ext import commands
import nextcord


class TalksCog(commands.Cog):
    """Lets you talk to the bot in slash commands"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Dê um oi para o Meka-zuki")
    async def oi(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Olá, {interaction.user.display_name}")

    @nextcord.slash_command(description="Dê um tchau para o Meka-zuki")
    async def tchau(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"Tchau, {interaction.user.display_name}")

    @nextcord.slash_command(description="Consulte sobre o servidor de Minecraft, Alicchia")
    async def server_mine(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"O nosso servidor de Minecraft: **Alicchia** está no período de testes alpha {interaction.user.display_name}! Esperamos que essa etapa do desenvolvimento vá levar por volta de 20 dias.")


def setup(bot):
    bot.add_cog(TalksCog(bot))