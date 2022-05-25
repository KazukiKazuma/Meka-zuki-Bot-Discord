import nextcord
from nextcord.ext import commands
import nextwave
import datetime
from utils import music_player_utils
import _secrets_

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
        https=_secrets_.lavalink_https
    )


    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: nextwave.Node):
        print(f"Node {node.identifier} connected and ready\n-------------------------\n")


    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: nextwave.Player, track: nextwave.YouTubeTrack, reason):
        interaction = player.interaction
        vc: player = interaction.guild.voice_client

        if vc.loop:
            return await vc.play(track)
        
        try:
            next_song = vc.queue.get()
        except:
            return
        
        next_playing_embed = nextcord.Embed(
            title="Agora Tocando:",
            description=f"[{next_song.title}]({next_song.uri})",
            color=0x2494f4
        )
        next_playing_embed.set_thumbnail(url=f"{next_song.thumbnail}")
        next_playing_embed.set_footer(text=f"duração  {str(datetime.timedelta(seconds=next_song.length))}", icon_url="https://i.imgur.com/M6rbN5i.png")
        
        await vc.play(next_song)
        await interaction.send(embed=next_playing_embed, delete_after=25)


    @nextcord.slash_command(description="Toque uma musica")
    async def play(
        self, 
        interaction: nextcord.Interaction, 
        searchit : str = nextcord.SlashOption(name="música", description="Procure por uma musica ou forneça um link do YouTube", required=True)
    ):
        search = await nextwave.YouTubeTrack.search(query=searchit, return_first=True)
        
        playing_embed = nextcord.Embed(
            title="Agora Tocando:",
            description=f"[{search.title}]({search.uri})",
            color=0x2494f4
        )
        playing_embed.set_thumbnail(url=f"{search.thumbnail}")
        playing_embed.set_footer(text=f"duração  {str(datetime.timedelta(seconds=search.length))}", icon_url="https://i.imgur.com/M6rbN5i.png")
        
        added_queue_embed = nextcord.Embed(
            title="Agora Tocando:",
            description=f"[{search.title}]({search.uri})",
            color=0x2494f4
        )
        added_queue_embed.set_thumbnail(url=f"{search.thumbnail}")
        check_is_playing : nextwave.Player = interaction.guild.voice_client
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            vc: nextwave.Player = await interaction.user.voice.channel.connect(cls=nextwave.Player)
        elif interaction.guild.voice_client and check_is_playing.channel != interaction.user.voice.channel and not check_is_playing.is_playing():
            await nextwave.Player.disconnect()
            vc: nextwave.Player = await interaction.user.voice.channel.connect(cls=nextwave.Player)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
        
        if vc.channel == interaction.user.voice.channel:
            if not vc.is_playing() and vc.queue.is_empty and vc.channel == interaction.user.voice.channel:
                await vc.play(search)
                await interaction.send(embed=playing_embed, delete_after=25)
            elif vc.is_paused() and vc.channel == interaction.user.voice.channel:
                await vc.queue.put_wait(search)
                pause_added_queue_embed = nextcord.Embed(
                title="Adicionada à queue:",
                description=f"[{search.title}]({search.uri})\n`{str(datetime.timedelta(seconds=search.length))}`",
                color=0x2494f4
                )
                pause_added_queue_embed.set_thumbnail(url=f"{search.thumbnail}")
                pause_added_queue_embed.add_field(name="lembrete", value="a música está pausada, para despausar basta usar o comando `/resume`")
            
                await vc.queue.put_wait(search)
                queue = vc.queue.copy()
                song_count = 0
                for song in queue:
                    song_count += 1
                    pause_added_queue_embed.set_footer(text=f"Esta música foi adicionada na posição {song_count} da queue", icon_url="https://i.imgur.com/M6rbN5i.png")
                await interaction.send(embed=pause_added_queue_embed, delete_after=20)
            elif vc.is_playing() and vc.channel == interaction.user.voice.channel:
                added_queue_embed = nextcord.Embed(
                title="Adicionada à queue:",
                description=f"[{search.title}]({search.uri})\n`{str(datetime.timedelta(seconds=search.length))}`",
                color=0x2494f4
                )
                added_queue_embed.set_thumbnail(url=f"{search.thumbnail}")
            
                await vc.queue.put_wait(search)
                queue = vc.queue.copy()
                song_count = 0
                for song in queue:
                    song_count += 1
                    added_queue_embed.set_footer(text=f"Esta música foi adicionada na posição {song_count} da queue", icon_url="https://i.imgur.com/M6rbN5i.png")
                await interaction.send(embed=added_queue_embed, delete_after=20)
        else:
            await interaction.send(embed=music_player_utils.play_not_in_same_vc, ephemeral=True)

        vc.interaction = interaction
        try:
            if vc.loop: return
        except:
            setattr(vc, "loop", False)


    @nextcord.slash_command(description="Pausa a música tocando")
    async def pause(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
        
        if vc.channel == interaction.user.voice.channel:
            await vc.pause()
            await interaction.send(embed=music_player_utils.pause_embed, delete_after=15)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Despausa a música ques está pausada")
    async def resume(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
        
        if vc.channel == interaction.user.voice.channel:
            await vc.resume()
            await interaction.send(embed=music_player_utils.resume_embed, delete_after=15)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Para de tocar música e limpa a queue")
    async def stop(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client

        if vc.channel == interaction.user.voice.channel:
            if vc.queue.is_empty:
                await vc.stop()
            else:
                vc.queue.clear()
                if vc.queue.is_empty:
                    await vc.stop()
            await interaction.send(embed=music_player_utils.stop_embed, delete_after=15)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Faz com que o bot saia do canal de voz que está conectado")
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
            await vc.disconnect()
            await interaction.send(embed=leave_embed, delete_after=5)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Repete ou Para de Repetir a música atual")
    async def loop(self, interaction: nextcord.Interaction):
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

        if vc.channel == interaction.user.voice.channel:
            if vc.loop:
                return await interaction.send(embed=music_player_utils.loop_embed, delete_after=15)
            else:
                return await interaction.send(embed=music_player_utils.unloop_embed, delete_after=15)
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)


    @nextcord.slash_command(description="Pula para a próxima música da queue")
    async def skip(self, interaction: nextcord.Interaction):
        
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
            
        if vc.channel == interaction.user.voice.channel:
            if not vc.is_playing(): 
                return await interaction.send("Não tem nada tocando no momento", ephemeral=True)
        
            if vc.queue.count != 0:

                next_playing_embed = nextcord.Embed(
                title="pulando para próxima música  <a:loading:747680523459231834> ..",
                color=0x2494f4
                )
            
                await interaction.send(embed=next_playing_embed, delete_after=5)
            else:
                return await interaction.send(embed=empty_queue_embed, ephemeral=True)
            await vc.stop()
            
        else:
            await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
        
        
        
    @nextcord.slash_command(description="Veja qual música está tocando no momento")
    async def nowplaying(self, interaction: nextcord.Interaction):
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            vc: nextwave.Player = interaction.guild.voice_client
            
        if not vc.is_playing(): 
            return await interaction.send("Nada está tocando no momento", ephemeral=True)
        
        currently_playing_embed = nextcord.Embed(
        title=f"Tocando neste momento:", 
        description=f"[{vc.track.title}]({vc.track.uri})",
        color=0x2494f4
        )
        currently_playing_embed.add_field(name="ㅤ", value=f"duração  `{str(datetime.timedelta(seconds=vc.track.length))}`")
        currently_playing_embed.set_image(url=f"{vc.track.thumbnail}")
        return await interaction.send(embed=currently_playing_embed, ephemeral=True)
    
          
    @nextcord.slash_command(description="Mostra a lista de músicas atualmente na queue")
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
            return await interaction.send("Não estou tocando nenhuma música no momento", ephemeral=True)
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
            elif song_count > 10:
                queue_embed.add_field(name=f"... e mais *{song_count}* outras músicas", inline=False)
            else:
                queue_embed.add_field(name=f"Posição {song_count}", value=f"[{song.title}]({song.uri})\n`{str(datetime.timedelta(seconds=song.length))}`", inline=False)
            
        return await interaction.send(embed=queue_embed, ephemeral=True)
    
    
    # @nextcord.slash_command(description="Mude volume que o bot está tocando a música")
    # async def volume(self,
    #     interaction: nextcord.Interaction,
    #     volume: int = nextcord.SlashOption(name="volume", description="Especifique o volume que quer que o bot toque a música", required=True)
    # ):
        
    #     if not getattr(interaction.user.voice, "channel", None):
    #         return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
    #     elif not interaction.guild.voice_client:
    #         return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
    #     else:
    #         vc: nextwave.Player = interaction.guild.voice_client
            
    #     if volume > 100:
    #         return await interaction.send("Não faça isso com seus tímpanos.. eles agradecem")
    #     elif volume < 0:
    #         return await interaction.send("Você tem certeza que colocou o número certo ?")
    #     await interaction.send(f"O volume foi alterado para {volume}%")
    #     await vc.set_volume(volume)
        
        

def setup(bot):
    bot.add_cog(YTPlayerCog(bot))