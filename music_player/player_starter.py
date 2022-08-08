from nextcord.ext import commands

from decouple import config

import nextwave
from nextwave.ext import spotify



class MusicPlayerStarter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.node_connect())
        
        PLAYER_COMMANDS_MODULES = [
            "leave_command",
            "loop_command",
            "music_url_on_dm_command",
            "now_playing_command",
            "panel_command",
            "pause_command",
            "play_command",
            "play_next_command",
            "queue_command",
            "remove_command",
            "resume_command",
            "skip_command",
            "stop_command"
        ]
        for module in PLAYER_COMMANDS_MODULES:
            bot.load_extension(f"music_player.player_commands.{module}")
            
        PLAYER_HANDLER_MODULES = [
            "control_panel_handler",
            "track_end_handler"
        ]
        for module in PLAYER_HANDLER_MODULES:
            bot.load_extension(f"music_player.player_handlers.{module}")

    
    
    async def node_connect(self):
        if config("LAVALINK_HTTPS").lower() == "true":
            ssl = True
        else:
            ssl = False
        
        BOT = self.bot
        HOST = config("LAVALINK_HOST")
        PORT = config("LAVALINK_PORT")
        PASSWORD = config("LAVALINK_PASSWORD")
        HTTPS = ssl
        SPOTIFY_ID =config("SPOTIFY_ID")
        SPOTIFY_SECRET = config("SPOTIFY_SECRET")
        
        await self.bot.wait_until_ready()
        await nextwave.NodePool.create_node(
        bot=BOT,
        host=HOST,
        port=PORT,
        password=PASSWORD,
        https=HTTPS,
        spotify_client=spotify.SpotifyClient(
            client_id=SPOTIFY_ID,
            client_secret=SPOTIFY_SECRET
        )
        )


    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: nextwave.Node):
        print(f"Node {node.identifier} connected and ready\n-------------------------\n")


def setup(bot):
    bot.add_cog(MusicPlayerStarter(bot))