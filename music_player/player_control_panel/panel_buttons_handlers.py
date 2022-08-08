import nextcord

import nextwave

from utils import music_player_utils



class PanelButtonsHandlers(nextcord.ui.View):
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
        elif interaction.user.voice == None:
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
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
        from music_player.player_handlers.control_panel_handler import ControlPanelHandler
        
        if not getattr(interaction.user.voice, "channel", None):
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif not interaction.guild.voice_client:
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        elif interaction.user.voice == None:
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
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
            await ControlPanelHandler.handle_panel_edit(self, interaction=interaction)

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
            if interaction.user.voice == None:
                return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
            if vc.channel == interaction.user.voice.channel:
                await interaction.message.delete()
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
        else:
            return await interaction.message.delete()