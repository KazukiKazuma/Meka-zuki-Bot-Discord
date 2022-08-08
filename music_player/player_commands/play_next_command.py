import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerPlayNextCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Move a música especificada(por nome ou por posição na queue) para a primeira posição da fila")
    async def play_next(self, interaction: nextcord.Interaction,
            remove = nextcord.SlashOption(
                name="música",
                description="Nome da música que quer mover para a primeira posição da file",
                required=True
            )
        ):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        playable = await nextwave.YouTubeTrack.search(query=remove, return_first=True)
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
        
        if vc.channel == interaction.user.voice.channel:
            if vc.queue.is_empty:
                empty_queue = nextcord.Embed(
                color=0xe42a44,
                description="Não existe **nenhuma** música na queue para ser movida."
                )
                return await interaction.send(embed=empty_queue, ephemeral=True)
            
            try:
                move_as_int = int(remove)
                indexed_music = vc.queue.__getitem__(move_as_int-1)
                moved_embed_index = nextcord.Embed(
                    color=0xffb11a,
                    description=f"A música `{indexed_music}` foi movida para a primeira posição da fila e tocará em seguida."
                )
                vc.queue.__delitem__(move_as_int-1)
                vc.queue.put_at_front(indexed_music)
                if move_as_int == 1:
                    already_next = nextcord.Embed(
                        color=0xe42a44,
                        description="Esta música já é a próxima na fila."
                    )
                    return await interaction.send(embed=already_next, ephemeral=True)
                return await interaction.send(embed=moved_embed_index, delete_after=7)
            except Exception:
                try:
                    new_list = [song.title.replace("'","") for song in vc.queue]
                    named_music = playable.title
                    song_index = new_list.index(playable.title)
                    moved_embed = nextcord.Embed(
                        color=0xffb11a,
                        description=f"A música `{named_music}` foi movida para a primeira posição da fila e tocará em seguida.."
                    )
                    vc.queue.__delitem__(song_index)
                    vc.queue.put_at_front(playable)
                    if song_index == 0:
                        already_next = nextcord.Embed(
                            color=0xe42a44,
                            description="Esta música já é a próxima na fila."
                        )
                        return await interaction.send(embed=already_next, ephemeral=True)
                    return await interaction.send(embed=moved_embed, delete_after=7)
                except Exception:
                    try:
                        song_position = int(remove)
                        not_found_embed = nextcord.Embed(
                            title="Ops...",
                            description=f"Não consegui encontrar nenhuma música na posição `{song_position}` da queue.",
                            color=0xe42a44
                        )
                    except Exception:
                        not_found_embed = nextcord.Embed(
                            title="Ops...",
                            description=f"Não consegui encontrar nenhuma música com o nome `{playable.title}` na queue.",
                            color=0xe42a44
                        )
                    return await interaction.send(embed=not_found_embed, ephemeral=True)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


def setup(bot):
    bot.add_cog(PlayerPlayNextCommand(bot))