import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerNowPlayingCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Veja qual música está tocando no momento", guild_ids=guild_utils.guild_ids)
    async def nowplaying(self, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
            
        if not vc.is_playing(): 
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)

        currently_playing_embed = nextcord.Embed(
        title=f"Tocando neste momento:", 
        description=f"[{vc.track.title}]({vc.track.uri})",
        color=0x2494f4
        )
        currently_playing_embed.add_field(name="ㅤ", value=f"duração  `{str(datetime.timedelta(seconds=vc.track.length))}`")
        currently_playing_embed.set_image(url=f"{vc.track.thumbnail}")
        await interaction.send(embed=currently_playing_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerNowPlayingCommand(bot))