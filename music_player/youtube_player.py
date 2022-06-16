import nextcord
from nextcord.ext import commands
import nextwave
from nextwave.ext import spotify
import datetime
from utils import music_player_utils, guild_utils
import _secrets_



class ControlPanel(nextcord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot



    async def handle_play_pause(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.is_paused():
            await interaction.response.defer()
            await vc.resume()
        elif vc.is_playing():
            await interaction.response.defer()
            await vc.pause()


    async def handle_skip(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            
            if not vc.is_playing(): 
                return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)

            if vc.queue.count != 0:
                try:
                    await vc.stop()
                except:
                    return
            else:
                await interaction.send(embed=music_player_utils.no_next_songs, ephemeral=True)

        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    async def handle_stop(self, button:nextcord.ui.Button, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            
            if vc.is_playing() or vc.is_paused():
                if vc.queue.is_empty:
                    await vc.stop()
                else:
                    vc.queue.clear()
                    await vc.stop()
            else:
                await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
            await self.handle_panel_embed(interaction)

        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    async def handle_loop(self, button:nextcord.ui.Button, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        try:
            vc.loop ^= True
        except Exception:
            setattr(vc, "loop", False)


    async def handle_close(self, button:nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if vc is None:
            return await interaction.message.delete()
        elif vc.is_playing():
            if vc.channel == interaction.user.voice.channel:
                await interaction.message.delete()
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
        else:
            return await interaction.message.delete()




    @nextcord.ui.button(emoji="<:pause_orange:980099882662625351>", style=nextcord.ButtonStyle.grey, custom_id="resume_and_pause_button")
    async def resume_and_pause_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if vc.channel == interaction.user.voice.channel:
                if not vc.is_paused():
                    button.style = nextcord.ButtonStyle.blurple
                    button.emoji = "<:play_gray:980100044801851413>"
                else:
                    button.style = nextcord.ButtonStyle.gray
                    button.emoji = "<:pause_orange:980099882662625351>"
                await self.handle_play_pause(button, interaction)
                await interaction.message.edit(view=self)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)

    @nextcord.ui.button(emoji="<:skip_orange:980099944797061160>", style=nextcord.ButtonStyle.gray, custom_id="skip_button")
    async def skip_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if vc.loop:
            return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True) 
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            await interaction.response.defer()
            await self.handle_skip(button, interaction)

    @nextcord.ui.button(emoji="<:stop_orange:980099927050952754>", style=nextcord.ButtonStyle.gray, custom_id="stop_button")
    async def stop_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if vc.loop:
            return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True) 
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            await self.handle_stop(button, interaction)

    @nextcord.ui.button(emoji="<:loop_one:980099967198847068>", style=nextcord.ButtonStyle.gray, custom_id="loop_button")
    async def loop_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        await interaction.response.defer()
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if vc.channel == interaction.user.voice.channel:
                if not vc.loop:
                    button.style = nextcord.ButtonStyle.blurple
                    button.emoji = "<:loop_one_gray:980100113965916161>"
                else:
                    button.style = nextcord.ButtonStyle.gray
                    button.emoji = "<:loop_one:980099967198847068>"
                await self.handle_loop(button, interaction)
                await interaction.message.edit(view=self)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)

    @nextcord.ui.button(emoji="✖", style=nextcord.ButtonStyle.red, custom_id="close_button")
    async def close_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_close(button, interaction)


    async def handle_panel_embed(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        
        if vc.loop:
            return
        else:
            if vc.is_playing():
                music_player_utils.panel_embed.set_image(url=vc.source.thumbnail)
                music_player_utils.panel_embed.set_field_at(index=0, name=f"Música tocando no momento:", value=f"[{vc.source.title}]({vc.source.uri})\nduração  `{str(datetime.timedelta(seconds=vc.source.length))}`", inline=False)
                if vc.queue.count > 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"{vc.queue.count} músicas na fila para serem tocadas em seguida", inline=False)
                elif vc.queue.count == 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"1 música na fila para ser tocada em seguida", inline=False)
                else:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"nenhuma música na fila para ser tocada em seguida", inline=False)
            else:
                music_player_utils.panel_embed.set_field_at(index=0, name=f"ㅤ", value="Nenhuma música está sendo reproduzida e a queue se encontra vazia no momento.  <:paimon_sleep:980047195279605800>", inline=False)
                music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"use o comando `/play` para adicionar uma música", inline=False)
                music_player_utils.panel_embed.set_image(url="https://i.imgur.com/9Vm7dJ2.gif")
            await interaction.message.edit(embed=music_player_utils.panel_embed, view=self)
        



##############################################################################################################################################################################
##############################################################################################################################################################################




class YTPlayerCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.node_connect())

    async def node_connect(self):
        await self.bot.wait_until_ready()
        await nextwave.NodePool.create_node(bot=self.bot,
        host=_secrets_.lavalink_host,
        port=_secrets_.lavalink_port,
        password=_secrets_.lavalink_password,
        https=_secrets_.lavalink_https,
        spotify_client=spotify.SpotifyClient(
            client_id= _secrets_.spotify_id,
            client_secret= _secrets_.spotify_secret
        )
    )


    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: nextwave.Node):
        print(f"Node {node.identifier} connected and ready\n-------------------------\n")


    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: nextwave.Player, track: nextwave.YouTubeTrack, reason):
        interaction = player.interaction
        vc: player = interaction.guild.voice_client

        if vc.loop:
            if vc.is_paused():
                return
            return await vc.play(track)


        try:
            next_song = vc.queue.get()
        except nextwave.QueueEmpty:
            try:
                return await self.handle_panel_edit(interaction)
            except Exception:
                return
            
        if next_song is not None:
            await vc.play(next_song)

        try:
            await self.handle_panel_edit(interaction)
        except Exception:
            try:
                next_playing_embed = nextcord.Embed(
                title="Agora Tocando:",
                description=f"[{next_song.title}]({next_song.uri})",
                color=0x2494f4
                )
                next_playing_embed.set_thumbnail(url=f"{next_song.mqthumbnail}")
                next_playing_embed.set_footer(text=f"duração  {str(datetime.timedelta(seconds=next_song.length))}", icon_url="https://i.imgur.com/M6rbN5i.png")
                
                await interaction.send(embed=next_playing_embed, delete_after=25)
            except:
                guild = self.bot.get_guild(guild_utils.guild_id)
                channel = guild.get_channel(guild_utils.music_channel_id)
                await channel.send(embed=next_playing_embed, delete_after=25)
        
        


    @nextcord.slash_command(name="painel", description="Envia um painel de controle da música no canal de texto", guild_ids=guild_utils.guild_ids)
    async def panel(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if vc.channel == interaction.user.voice.channel:
                
                if vc.is_playing():
                    try:
                        await self.check_if_panel_exists(interaction)
                        await self.delete_old_panel(interaction)
                    except NameError:
                        pass
                    except nextcord.NotFound:
                        pass
                    except SyntaxError:
                        pass
                    
                    await self.handle_panel_start(interaction)
                    
                else:
                    await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)

    async def handle_panel_start(self, interaction:nextcord.Interaction):
        panel_buttons = ControlPanel(self)
        vc: nextwave.Player = interaction.guild.voice_client
            
        music_player_utils.panel_embed.set_image(url=vc.source.thumbnail)
        music_player_utils.panel_embed.clear_fields()
        music_player_utils.panel_embed.add_field(name=f"Música tocando no momento:", value=f"[{vc.source.title}]({vc.source.uri})\nduração  `{str(datetime.timedelta(seconds=vc.source.length))}`", inline=False)
        music_player_utils.panel_embed.set_footer(text="no caso de dúvidas use /help", icon_url=self.bot.user.display_avatar)
        if vc.queue.count > 1:
            music_player_utils.panel_embed.add_field(name="ㅤ", value=f"{vc.queue.count} músicas na fila para serem tocadas", inline=False)
        elif vc.queue.count == 1:
            music_player_utils.panel_embed.add_field(name="ㅤ", value=f"1 música na fila para ser tocada em seguida", inline=False)
        else:
            music_player_utils.panel_embed.add_field(name="ㅤ", value=f"nenhuma música na fila para ser tocada", inline=False)
        await interaction.send(embed=music_player_utils.panel_embed, view=panel_buttons)
        panel = await interaction.original_message()
        global first_music_panel_message_message
        first_music_panel_message_message = panel.id

    async def handle_panel_added_tracks(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        channel = interaction.channel
        edit_panel = channel.get_partial_message(first_music_panel_message_message)
        
        if vc.queue.count > 1:
            music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"{vc.queue.count} músicas na fila para serem tocadas em seguida", inline=False)
        elif vc.queue.count == 1:
            music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"1 música na fila para ser tocada em seguida", inline=False)
        else:
            music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"nenhuma música na fila para ser tocada em seguida", inline=False)
        await edit_panel.edit(embed=music_player_utils.panel_embed)
        
    async def handle_panel_edit(self, interaction:nextcord.Interaction):
        panel_buttons = ControlPanel(self)
        vc: nextwave.Player = interaction.guild.voice_client
        channel = interaction.channel
        edit_panel = channel.get_partial_message(first_music_panel_message_message)

        if vc.loop :
            return
        else:
            if vc.is_playing():
                music_player_utils.panel_embed.set_image(url=vc.source.thumbnail)
                music_player_utils.panel_embed.set_field_at(index=0, name=f"Música tocando no momento:", value=f"[{vc.source.title}]({vc.source.uri})\nduração  `{str(datetime.timedelta(seconds=vc.source.length))}`", inline=False)
                if vc.queue.count > 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"{vc.queue.count} músicas na fila para serem tocadas em seguida", inline=False)
                elif vc.queue.count == 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"1 música na fila para ser tocada em seguida", inline=False)
                else:
                    music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"nenhuma música na fila para ser tocada em seguida", inline=False)
            else:
                music_player_utils.panel_embed.set_field_at(index=0, name=f"ㅤ", value="Nenhuma música está sendo reproduzida e a queue se encontra vazia no momento.  <:paimon_sleep:980047195279605800>", inline=False)
                music_player_utils.panel_embed.set_field_at(index=1, name="ㅤ", value=f"use o comando `/play` para adicionar uma música", inline=False)
                music_player_utils.panel_embed.set_image(url="https://i.imgur.com/9Vm7dJ2.gif")
            await edit_panel.edit(embed=music_player_utils.panel_embed, view=panel_buttons)
            
    async def delete_old_panel(self, interaction:nextcord.Interaction):
        channel = interaction.channel
        old_panel = channel.get_partial_message(first_music_panel_message_message)
        await nextcord.Message.delete(old_panel)
        
    async def check_if_panel_exists(self, interaction:nextcord.Interaction):
        channel = interaction.channel
        edit_panel = channel.get_partial_message(first_music_panel_message_message)
        music_player_utils.panel_embed.set_footer(text="no caso de dúvidas use /help", icon_url=self.bot.user.display_avatar)
        await edit_panel.edit(embed=music_player_utils.panel_embed)
            
            


    @nextcord.slash_command(description="Toque uma musica", guild_ids=guild_utils.guild_ids)
    async def play(
        self, 
        interaction: nextcord.Interaction, 
        searchit : str = nextcord.SlashOption(name="música", description="Procure por uma musica ou forneça um link do YouTube", required=True)
    ):
        
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
                    await self.handle_panel_edit(interaction)
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
                        await self.handle_panel_added_tracks(interaction)
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
                        await self.handle_panel_added_tracks(interaction)
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


    @nextcord.slash_command(description="Remove uma música especificada(por nome ou posição na queue) da queue")
    async def remove(self, interaction: nextcord.Interaction,
            remove = nextcord.SlashOption(
                name="música",
                description="Nome da música que quer remover ou a posição dela na queue",
                required=True
            )
        ):
        
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
                description="Não existe **nenhuma** música na queue para ser removida."
                )
                return await interaction.send(embed=empty_queue, ephemeral=True)
            
            try:
                remove_as_int = int(remove)
                removed_embed_index = nextcord.Embed(
                color=0xffb11a,
                description=f"A música `{vc.queue.__getitem__(remove_as_int-1)}` foi removida da queue."
                )
                vc.queue.__delitem__(remove_as_int-1)
                return await interaction.send(embed=removed_embed_index, delete_after=7)
            except Exception:
                try:
                    new_list = [song.title.replace("'","") for song in vc.queue]
                    song_index = new_list.index(playable.title)
                    removed_embed = nextcord.Embed(
                    color=0xffb11a,
                    description=f"A música `{playable.title}` foi removida da queue."
                    )
                    vc.queue.__delitem__(song_index)
                    return await interaction.send(embed=removed_embed, delete_after=7)
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
            
            
    @nextcord.slash_command(description="Move a música especificada(por nome ou por posição na queue) para a primeira posição da fila")
    async def play_next(self, interaction: nextcord.Interaction,
            remove = nextcord.SlashOption(
                name="música",
                description="Nome da música que quer mover para a primeira posição da file",
                required=True
            )
        ):
        
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


    @nextcord.slash_command(description="Pausa a música tocando", guild_ids=guild_utils.guild_ids)
    async def pause(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            try:
                await self.check_if_panel_exists(interaction)
                return await interaction.send(embed=music_player_utils.use_use_the_panel, ephemeral=True)
            except NameError:
                pass
            except nextcord.NotFound:
                pass
            if vc.is_playing():
                await vc.pause()
                await interaction.send(embed=music_player_utils.pause_embed, delete_after=15)
            else:
                await interaction.send(embed=music_player_utils.music_already_paused, ephemeral=True)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Despausa a música ques está pausada", guild_ids=guild_utils.guild_ids)
    async def resume(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            try:
                await self.check_if_panel_exists(interaction)
                return await interaction.send(embed=music_player_utils.use_use_the_panel, ephemeral=True)
            except NameError:
                pass
            except nextcord.NotFound:
                pass
            if vc.is_paused():
                await vc.resume()
                await interaction.send(embed=music_player_utils.resume_embed, delete_after=15)
            else:
                await interaction.send(embed=music_player_utils.music_already_playing, ephemeral=True)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Para de tocar música e limpa a queue", guild_ids=guild_utils.guild_ids)
    async def stop(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            try:
                await self.check_if_panel_exists(interaction)
                return await interaction.send(embed=music_player_utils.use_use_the_panel, ephemeral=True)
            except NameError:
                pass
            except nextcord.NotFound:
                pass
            if vc.loop:
                return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True)
            if vc.is_playing() or vc.is_paused():
                if vc.queue.is_empty:
                    await vc.stop()
                else:
                    vc.queue.clear()
                    await vc.stop()
                await interaction.send(embed=music_player_utils.stop_embed, delete_after=15)
            else:
                await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True) 

        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Faz com que o bot saia do canal de voz que está conectado", guild_ids=guild_utils.guild_ids)
    async def leave(self, interaction: nextcord.Interaction):

        leave_embed = nextcord.Embed(
            title="Saindo do canal",
            description="até a próxima !",
            color=0xd43b3d
        )

        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel or not vc.is_playing():
            await interaction.send(embed=leave_embed, delete_after=5)
            await vc.disconnect()
            try:
                channel = interaction.channel
                old_panel = channel.get_partial_message(first_music_panel_message_message)
                await nextcord.Message.delete(old_panel)
            except AttributeError:
                pass
            except:
                pass
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Repete ou Para de Repetir a música atual", guild_ids=guild_utils.guild_ids)
    async def loop(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
            
        try:
            await self.check_if_panel_exists(interaction)
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


    @nextcord.slash_command(description="Pula para a próxima música da queue", guild_ids=guild_utils.guild_ids)
    async def skip(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            try:
                await self.check_if_panel_exists(interaction)
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



    @nextcord.slash_command(description="Veja qual música está tocando no momento", guild_ids=guild_utils.guild_ids)
    async def nowplaying(self, interaction: nextcord.Interaction):
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


    @nextcord.slash_command(description="Mostra a lista de músicas atualmente na queue", guild_ids=guild_utils.guild_ids)
    async def queue(self, interaction: nextcord.Interaction):

        empty_queue_embed = nextcord.Embed(
            title="A queue está vazia",
            color=0xe3e3e3,
            description="use o comando **/play** para adicionar mais músicas novas à queue."
        )
        empty_queue_embed.set_thumbnail(url="https://i.imgur.com/ITgTV2i.png")

        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.queue.is_empty:
            return await interaction.send(embed=empty_queue_embed, ephemeral=True)

        queue_embed = nextcord.Embed(
            title="Queue",
            color=0xc1ccdd
        )
        queue_embed.set_thumbnail(url="https://i.imgur.com/t7BkUjV.png")

        queue = vc.queue.copy()
        song_count = 0
        for song in queue:
            song_count += 1
            if song_count == 1:
                queue_embed.add_field(name=f"Próxima a tocar", value=f"[{song.title}]({song.uri})\n`{str(datetime.timedelta(seconds=song.length))}`", inline=False)
            elif song_count <= 10:
                queue_embed.add_field(name=f"Posição {song_count}", value=f"[{song.title}]({song.uri})\n`{str(datetime.timedelta(seconds=song.length))}`", inline=False)
            elif len(queue) > 10:
                queue_embed.add_field(name=f"\n... e mais *{queue.count-song_count+1}* outras músicas", value="\u200b", inline=False)
                break

        await interaction.send(embed=queue_embed, ephemeral=True)


    @nextcord.slash_command(description="Envia o link da música atual no seu privado caso queira guardar para não perder", guild_ids=guild_utils.guild_ids)
    async def link_da_musica_no_pv(self, interaction: nextcord.Interaction):
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
        dm_currently_playing_embed.add_field(name="ㅤ", value=f"duração  `{str(datetime.timedelta(seconds=vc.track.length))}`")
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


    @nextcord.slash_command(name="limpar", description="Jogue uma rodada de Jokenpo com a Mashiro")
    async def limpar(self,
            interaction: nextcord.Interaction,
            message_id = nextcord.SlashOption(
                name="id-da-mensagem",
                description="Delete uma mensagem específica do bot",
                required=True,
            )
        ):

        message_deleted = nextcord.Embed(
            title="Mensagem deletada",
            color=0xe42a44
        )

        await interaction.user.create_dm()
        dm = interaction.user.dm_channel
        try:
            message = await dm.fetch_message(int(message_id))
            await nextcord.Message.delete(message)
        except:
            return

        await interaction.send(embed=message_deleted, delete_after=3)



def setup(bot):
    bot.add_cog(YTPlayerCog(bot))