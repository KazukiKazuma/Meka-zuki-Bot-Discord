import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class TrackEndHandler(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
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
                return await ControlPanelHandler.handle_panel_edit(self, interaction=interaction)
            except Exception:
                return
            
        if next_song is not None:
            await vc.play(next_song)

        try:
            await ControlPanelHandler.handle_panel_edit(self, interaction=interaction)
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


def setup(bot):
    bot.add_cog(TrackEndHandler(bot))