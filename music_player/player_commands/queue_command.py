import nextcord
from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify

import datetime

from utils import music_player_utils, guild_utils
from music_player.player_handlers.control_panel_handler import ControlPanelHandler
from utils.commands_utils import command_modules, module_disabled_message



class PlayerQueueCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @nextcord.slash_command(description="Mostra a lista de músicas atualmente na queue", guild_ids=guild_utils.guild_ids)
    async def queue(self, interaction: nextcord.Interaction):
        if command_modules['Music Player'] == "Off":
            await interaction.send(embed=module_disabled_message)
            return

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


def setup(bot):
    bot.add_cog(PlayerQueueCommand(bot))