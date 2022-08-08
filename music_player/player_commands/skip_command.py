import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerSkipCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Pula para a próxima música da queue", guild_ids=guild_utils.guild_ids)
    async def skip(self, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            try:
                await ControlPanelHandler.check_if_panel_exists(self, interaction=interaction)
                return await interaction.send(embed=music_player_utils.use_use_the_panel, ephemeral=True)
            except NameError:
                pass
            except nextcord.NotFound:
                pass
            if vc.loop:
                return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True)
            
            if not vc.is_playing(): 
                return await interaction.send("Não tem nada tocando no momento", ephemeral=True)

            if vc.queue.count != 0:

                next_playing_embed = nextcord.Embed(
                title="pulando para próxima música  <a:loading:747680523459231834> ..",
                color=0x2494f4
                )

                await interaction.send(embed=next_playing_embed, delete_after=5)
            else:
                await interaction.send(embed=music_player_utils.no_next_songs, ephemeral=True)

            try:
                await vc.stop()
            except:
                return

        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerSkipCommand(bot))