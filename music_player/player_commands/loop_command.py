import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerLoopCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Repete ou Para de Repetir a música atual", guild_ids=guild_utils.guild_ids)
    async def loop(self, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
            
        try:
            await ControlPanelHandler.check_if_panel_exists(self, interaction=interaction)
            return await interaction.send(embed=music_player_utils.use_use_the_panel, ephemeral=True)
        except NameError:
            pass
        except nextcord.NotFound:
            pass

        try:
            vc.loop ^= True
        except Exception:
            setattr(vc, "loop", False)

        if vc.channel == interaction.user.voice.channel:
            if vc.loop:
                await interaction.send(embed=music_player_utils.loop_embed, delete_after=15)
            else:
                await interaction.send(embed=music_player_utils.unloop_embed, delete_after=15)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerLoopCommand(bot))