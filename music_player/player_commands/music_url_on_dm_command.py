import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerMusicURLOnDMCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(name="link_da_música_no_pv", description="Envia o link da música atual no seu privado caso queira guardar para não perder", guild_ids=guild_utils.guild_ids)
    async def music_url_on_dm(self, interaction: nextcord.Interaction):
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
        elif vc.is_paused(): 
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)

        dm_currently_playing_embed = nextcord.Embed(
        title=f"Você pediu e aqui está:", 
        description=f"Esta é a música que estava tocando na `Guilda` quando você pediu para que eu te enviasse ela no privado:\n\n[{vc.track.title}]({vc.track.uri})",
        color=0x2494f4
        )
        dm_currently_playing_embed.set_thumbnail(url=interaction.guild.icon)
        dm_currently_playing_embed.add_field(name="\u200b", value=f"duração  `{str(datetime.timedelta(seconds=vc.track.length))}`")
        dm_currently_playing_embed.set_image(url=f"{vc.track.thumbnail}")

        await interaction.user.create_dm()
        dm = interaction.user.dm_channel

        message_for_id = await dm.send(embed=dm_currently_playing_embed)
        if dm is not None:
            id = message_for_id.id
            await message_for_id.edit(embed=dm_currently_playing_embed.set_footer(
                text=f"para deletar esta mensagem use /limpar com o seguinte ID: {id}"
            ))
        await interaction.send(embed=music_player_utils.check_your_dm, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerMusicURLOnDMCommand(bot))