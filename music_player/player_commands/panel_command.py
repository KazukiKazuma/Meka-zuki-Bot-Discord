import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerPanelCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(name="painel", description="Envia um painel de controle da música no canal de texto", guild_ids=guild_utils.guild_ids)
    async def panel(self, interaction:nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        vc: nextwave.Player = interaction.guild.voice_client
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if vc.channel == interaction.user.voice.channel:
                
                if vc.is_playing():
                    try:
                        await ControlPanelHandler.check_if_panel_exists(self, interaction=interaction)
                        await ControlPanelHandler.delete_old_panel(self, interaction=interaction)
                    except NameError:
                        pass
                    except nextcord.NotFound:
                        pass
                    except SyntaxError:
                        pass
                    
                    await ControlPanelHandler.handle_panel_start(self, interaction=interaction)
                    
                else:
                    await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerPanelCommand(bot))