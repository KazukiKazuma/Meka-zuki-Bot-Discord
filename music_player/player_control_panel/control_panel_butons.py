import nextcord

import nextwave

from utils import music_player_utils
from music_player.player_control_panel.panel_buttons_handlers import PanelButtonsHandlers

from utils.commands_utils import command_modules, module_disabled_message





class ControlPanelButtons(nextcord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
    
    
    
    
    @nextcord.ui.button(emoji="<:pause_orange:980099882662625351>", style=nextcord.ButtonStyle.grey, custom_id="resume_and_pause_button")
    async def resume_and_pause_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        vc: nextwave.Player = interaction.guild.voice_client
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        elif interaction.user.voice == None and vc.is_playing():
            return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
        elif interaction.user.voice == None and not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if vc.channel == interaction.user.voice.channel:
                if not vc.is_paused():
                    button.style = nextcord.ButtonStyle.blurple
                    button.emoji = "<:play_gray:980100044801851413>"
                else:
                    button.style = nextcord.ButtonStyle.gray
                    button.emoji = "<:pause_orange:980099882662625351>"
                await PanelButtonsHandlers.handle_play_pause(self, button, interaction)
                await interaction.message.edit(view=self)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
    
    
    
    @nextcord.ui.button(emoji="<:skip_orange:980099944797061160>", style=nextcord.ButtonStyle.gray, custom_id="skip_button")
    async def skip_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        vc: nextwave.Player = interaction.guild.voice_client
        if vc.loop:
            return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True) 
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            await interaction.response.defer()
            await PanelButtonsHandlers.handle_skip(self, button, interaction)
    
    
    
    @nextcord.ui.button(emoji="<:stop_orange:980099927050952754>", style=nextcord.ButtonStyle.gray, custom_id="stop_button")
    async def stop_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        if vc.loop:
            return await interaction.send(embed=music_player_utils.music_is_looping, ephemeral=True) 
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            await PanelButtonsHandlers.handle_stop(self, button, interaction)

    
    
    @nextcord.ui.button(emoji="<:loop_one:980099967198847068>", style=nextcord.ButtonStyle.gray, custom_id="loop_button")
    async def loop_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return
        
        vc: nextwave.Player = interaction.guild.voice_client
        await interaction.response.defer()
        if not vc.is_playing():
            return await interaction.send(embed=music_player_utils.no_music_playing, ephemeral=True)
        else:
            if interaction.user.voice == None:
                return await interaction.send(embed=music_player_utils.connect_first, ephemeral=True)
            if vc.channel == interaction.user.voice.channel:
                if not vc.loop:
                    button.style = nextcord.ButtonStyle.blurple
                    button.emoji = "<:loop_one_gray:980100113965916161>"
                else:
                    button.style = nextcord.ButtonStyle.gray
                    button.emoji = "<:loop_one:980099967198847068>"
                await PanelButtonsHandlers.handle_loop(self, button, interaction)
                await interaction.message.edit(view=self)
            else:
                await interaction.send(embed=music_player_utils.command_not_in_same_vc, ephemeral=True)
    
    
    
    @nextcord.ui.button(emoji="✖", style=nextcord.ButtonStyle.red, custom_id="close_button")
    async def close_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await PanelButtonsHandlers.handle_close(self, button, interaction)