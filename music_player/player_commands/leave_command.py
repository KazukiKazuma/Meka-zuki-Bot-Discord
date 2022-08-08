import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerLeaveCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Faz com que o bot saia do canal de voz que está conectado", guild_ids=guild_utils.guild_ids)
    async def leave(self, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return

        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel or not vc.is_playing():
            leave_embed = nextcord.Embed(
            title="Saindo do canal",
            description="até a próxima !",
            color=0xd43b3d
            )
            
            await interaction.send(embed=leave_embed, delete_after=5)
            await vc.stop()
            await vc.disconnect()
            try:
                await ControlPanelHandler.delete_old_panel(self, interaction=interaction)
            except AttributeError:
                pass
            except:
                pass
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
            

def setup(bot):
    bot.add_cog(PlayerLeaveCommand(bot))