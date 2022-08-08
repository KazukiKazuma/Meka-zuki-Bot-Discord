import nextcord
from nextcord.ext import commands

import nextwave

import datetime

from utils import music_player_utils

from music_player.player_control_panel.control_panel_butons import ControlPanelButtons
from music_player.player_utils.player_panel_message_id import panel_message_id



class ControlPanelHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    async def handle_panel_start(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        
        music_player_utils.panel_embed.set_image(url=vc.source.thumbnail)
        music_player_utils.panel_embed.clear_fields()
        music_player_utils.panel_embed.add_field(name=f"Música tocando no momento:", value=f"[{vc.source.title}]({vc.source.uri})\nduração  `{str(datetime.timedelta(seconds=vc.source.length))}`", inline=False)
        music_player_utils.panel_embed.set_footer(text="no caso de dúvidas use /help", icon_url=self.bot.user.display_avatar)
        if vc.queue.count > 1:
            music_player_utils.panel_embed.add_field(name="\u200b", value=f"{vc.queue.count} músicas na fila para serem tocadas", inline=False)
        elif vc.queue.count == 1:
            music_player_utils.panel_embed.add_field(name="\u200b", value=f"1 música na fila para ser tocada em seguida", inline=False)
        else:
            music_player_utils.panel_embed.add_field(name="\u200b", value=f"nenhuma música na fila para ser tocada", inline=False)
        await interaction.send(embed=music_player_utils.panel_embed, view=ControlPanelButtons(self))
        panel = await interaction.original_message()
        panel_message_id["id"] = panel.id
    
    
    
    async def handle_panel_added_tracks(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        channel = interaction.channel
        edit_panel = channel.get_partial_message(panel_message_id["id"])
        
        if vc.queue.count > 1:
            music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"{vc.queue.count} músicas na fila para serem tocadas em seguida", inline=False)
        elif vc.queue.count == 1:
            music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"1 música na fila para ser tocada em seguida", inline=False)
        else:
            music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"nenhuma música na fila para ser tocada em seguida", inline=False)
        await edit_panel.edit(embed=music_player_utils.panel_embed)
        
    
    async def handle_panel_edit(self, interaction:nextcord.Interaction):
        vc: nextwave.Player = interaction.guild.voice_client
        channel = interaction.channel
        edit_panel = channel.get_partial_message(panel_message_id["id"])

        if vc.loop :
            return
        else:
            if vc.is_playing():
                music_player_utils.panel_embed.set_image(url=vc.source.thumbnail)
                music_player_utils.panel_embed.set_field_at(index=0, name=f"Música tocando no momento:", value=f"[{vc.source.title}]({vc.source.uri})\nduração  `{str(datetime.timedelta(seconds=vc.source.length))}`", inline=False)
                if vc.queue.count > 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"{vc.queue.count} músicas na fila para serem tocadas em seguida", inline=False)
                elif vc.queue.count == 1:
                    music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"1 música na fila para ser tocada em seguida", inline=False)
                else:
                    music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"nenhuma música na fila para ser tocada em seguida", inline=False)
            else:
                music_player_utils.panel_embed.set_field_at(index=0, name=f"\u200b", value="Nenhuma música está sendo reproduzida e a queue se encontra vazia no momento.  <:paimon_sleep:980047195279605800>", inline=False)
                music_player_utils.panel_embed.set_field_at(index=1, name="\u200b", value=f"use o comando `/play` para adicionar uma música", inline=False)
                music_player_utils.panel_embed.set_image(url="https://i.imgur.com/9Vm7dJ2.gif")
            await edit_panel.edit(embed=music_player_utils.panel_embed, view=ControlPanelButtons(self))
            
            
    async def check_if_panel_exists(self, interaction:nextcord.Interaction):
        channel = interaction.channel
        edit_panel = channel.get_partial_message(panel_message_id["id"])
        music_player_utils.panel_embed.set_footer(text="no caso de dúvidas use /help", icon_url=self.bot.user.display_avatar)
        await edit_panel.edit(embed=music_player_utils.panel_embed)
        
    
    async def delete_old_panel(self, interaction:nextcord.Interaction):
        channel = interaction.channel
        old_panel = channel.get_partial_message(panel_message_id["id"])
        await nextcord.Message.delete(old_panel)


def setup(bot):
    bot.add_cog(ControlPanelHandler(bot))