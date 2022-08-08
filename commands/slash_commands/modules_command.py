import nextcord
from nextcord.ext import commands
from alerts.stream_alerts.stream_alerts import StreamAlert
from utils import help_command_utils, guild_utils
from utils.commands_utils import command_modules


class ModuleCog(commands.Cog):
    """Commands that show what command modules are ON and OFF and a way of changing that"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="module", description="Activate and deactivate a commands module", guild_ids=guild_utils.guild_ids)
    async def module(self,
            interaction: nextcord.Interaction,
            module = nextcord.SlashOption(
                name="módulo",
                description="Escolha o módulo que quer desativar ou ativar",
                required=True,
                choices=["Alerta de Stream"]
            ),
            state = nextcord.SlashOption(
                name="status",
                description="Escolha o se quer desligar ou ligar este módulo",
                required=True,
                choices=["On", "Off"]
            )
            ):
        if module == "Alerta de Stream":
            if state == "On":
                command_modules['Alerta de Stream']="On"
                try:
                    StreamAlert.turn_on_stream_alerts()
                    response_on = nextcord.Embed(
                        description="O módulo de `Alerta de Streams` agora está **ligado**",
                        color=0x83b834
                    )
                except Exception:
                    response_on = nextcord.Embed(
                        description="O módulo de `Alerta de Streams` já se encontra **ligado**",
                        color=0xffb11a
                    )
                await interaction.send(embed=response_on, ephemeral=True)
            elif state == "Off":
                command_modules['Alerta de Stream']="Off"
                try:
                    StreamAlert.turn_off_stream_alerts()
                    response_off = nextcord.Embed(
                        description="O módulo de `Alerta de Streams` agora está **desligado**",
                        color=0xe53b44
                    )
                except Exception:
                    response_off = nextcord.Embed(
                        description="O módulo de `Alerta de Streams` já se encontra **desligado**",
                        color=0xffb11a
                    )
                await interaction.send(embed=response_off, ephemeral=True)


def setup(bot):
    bot.add_cog(ModuleCog(bot))