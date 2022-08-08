import nextcord
from nextcord.ext import commands

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerPlayCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(description="Toque uma musica", guild_ids=guild_utils.guild_ids)
    async def play(
        self, 
        interaction: nextcord.Interaction, 
        searchit : str = nextcord.SlashOption(name="música", description="Procure por uma musica ou forneça um link do YouTube", required=True)
    ):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        check_is_playing : nextwave.Player = interaction.guild.voice_client
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            vc: nextwave.Player = await interaction.user.voice.channel.connect(cls=nextwave.Player)
        elif interaction.guild.voice_client and check_is_playing.channel != interaction.user.voice.channel and not check_is_playing.is_playing():
            await check_is_playing.disconnect()
            vc: nextwave.Player = await interaction.user.voice.channel.connect(cls=nextwave.Player)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
            

        await interaction.response.defer()
            
        if "spotify.com/track" in searchit:
            search = await spotify.SpotifyTrack.search(query=searchit, return_first=True)
        elif "spotify.com/playlist" in searchit:
            search = await spotify.SpotifyTrack.search(query=searchit)
        elif "&list=" in searchit:
            playlist = await vc.node.get_playlist(nextwave.YouTubePlaylist, searchit)
            search = playlist.tracks
        else:
            try:
                search = await nextwave.YouTubeTrack.search(query=searchit, return_first=True)
            except:
                search = await vc.node.get_tracks(nextwave.YouTubeTrack, searchit)

        if vc.channel == interaction.user.voice.channel: 
            if not vc.is_playing() and vc.queue.is_empty:
                await vc.set_volume(4)
                
                if type(search) == list:
                    await vc.play(search[0])
                    
                    for track in search[1:]:
                        await vc.queue.put_wait(track)
                        
                    playing_embed = nextcord.Embed(
                    title="Agora Tocando:",
                    description=f"[{search[0].title}]({search[0].uri})",
                    color=0x2494f4
                    )
                    playing_embed.add_field(name="\u200b", value=f"e mais `{len(search)-1}` músicas foram adicionadas na fila\n")
                    playing_embed.set_thumbnail(url=f"{search[0].mqthumbnail}")
                    playing_embed.set_footer(text=f"duração  {str(datetime.timedelta(seconds=search[0].length))}", icon_url="https://i.imgur.com/M6rbN5i.png")
                    
                else:
                    await vc.play(search)
                    playing_embed = nextcord.Embed(
                    title="Agora Tocando:",
                    description=f"[{search.title}]({search.uri})",
                    color=0x2494f4
                    )
                    playing_embed.set_thumbnail(url=f"{search.mqthumbnail}")
                    playing_embed.set_footer(text=f"duração  {str(datetime.timedelta(seconds=search.length))}", icon_url="https://i.imgur.com/M6rbN5i.png")
                
                try:
                    await ControlPanelHandler.handle_panel_edit(self, interaction=interaction)
                    await interaction.send(embed=music_player_utils.panel_embed_updated, delete_after=1)
                except Exception:
                    await interaction.send(embed=playing_embed, delete_after=25)
                
            else:
                if type(search) == list:
                    for track in search:
                        await vc.queue.put_wait(track)
                    
                    if len(search) == 1:
                        added_queue_embed = nextcord.Embed(
                        title="Adicionada à queue:",
                        description=f"[{search[0].title}]({search[0].uri})\n`{str(datetime.timedelta(seconds=search[0].length))}`",
                        color=0x2494f4
                        )
                        added_queue_embed.set_thumbnail(url=f"{search[0].mqthumbnail}")
                        
                        queue = vc.queue.copy()
                        song_count = 0
                        for song in queue:
                            song_count += 1
                            added_queue_embed.set_footer(text=f"Esta música foi adicionada na posição {song_count} da queue", icon_url="https://i.imgur.com/M6rbN5i.png")
                            
                    else: 
                        added_queue_embed = nextcord.Embed(
                        title="Adicionadas à queue:",
                        description=f"`{len(search)}` músicas foram adicionadas à queue",
                        color=0x2494f4
                        )
                    
                    try:
                        await ControlPanelHandler.handle_panel_added_tracks(self, interaction=interaction)
                    except Exception:
                        pass
                    
                else:
                    added_queue_embed = nextcord.Embed(
                    title="Adicionada à queue:",
                    description=f"[{search.title}]({search.uri})\n`{str(datetime.timedelta(seconds=search.length))}`",
                    color=0x2494f4
                    )
                    added_queue_embed.set_thumbnail(url=f"{search.mqthumbnail}")
                
                    await vc.queue.put_wait(search)
                    queue = vc.queue.copy()
                    song_count = 0
                    for song in queue:
                        song_count += 1
                        added_queue_embed.set_footer(text=f"Esta música foi adicionada na posição {song_count} da queue", icon_url="https://i.imgur.com/M6rbN5i.png")
                        
                    try:
                        await ControlPanelHandler.handle_panel_added_tracks(self, interaction=interaction)
                    except Exception:
                        pass
                    
                await interaction.send(embed=added_queue_embed, delete_after=10)

        else:
            await interaction.send(embed=music_player_utils.play_not_in_same_vc, ephemeral=True)

        vc.interaction = interaction
        try:
            if vc.loop: return
        except:
            setattr(vc, "loop", False)


def setup(bot):
    bot.add_cog(PlayerPlayCommand(bot))