import nextcord
import _secrets_

from nextcord.ext import commands

from reaction_tasks.embed_roles.streamer_roles import DaxlianButtons, ScocottaButtons
from reaction_tasks.role_buttons.reaction_buttons import VowButton
from music_player.youtube_player import ControlPanel



### Persist Views Overwrite ###
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:

            self.add_view(VowButton(bot))
            self.add_view(ScocottaButtons())
            self.add_view(DaxlianButtons())
            self.add_view(ControlPanel(bot))

            self.persistent_views_added = True
######


### Intents setup ###
intents = nextcord.Intents.default()
intents.members=True
######


### Bot definitions ###
bot = Bot(command_prefix=_secrets_.prefix, intents=intents)
######



### Commands ###
bot.load_extension("commands.slash_commands.slash_talks")
bot.load_extension("commands.slash_commands.jokenpo")
bot.load_extension("commands.standard_commands.minecraft_server_status")
bot.load_extension("reaction_tasks.role_buttons.reaction_buttons")
bot.load_extension("reaction_tasks.embed_roles.streamer_roles")
bot.load_extension("events.on_join_server")
bot.load_extension("reaction_tasks.reaction_roles.registration")
bot.load_extension("alerts.stream_alerts")
bot.load_extension("commands.standard_commands.reaction_message")
bot.load_extension("music_player.youtube_player")
bot.load_extension("commands.slash_commands.help_command")
bot.load_extension("commands.slash_commands.dice")
#######


### Manager ###
bot.load_extension("manager")
######



### Discord bot TOKEN  and RUN###
bot_token = _secrets_.bot_token
bot.run(bot_token)
######