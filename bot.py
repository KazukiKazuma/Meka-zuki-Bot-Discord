import nextcord
from nextcord.ext import commands

from decouple import config

### Streamer Imports ###
from tasks.button_tasks.streamers_roles_buttons.scocotta_streamer_buttons import ScocottaButtons
from tasks.button_tasks.streamers_roles_buttons.daxlian_streamer_buttons import DaxlianButtons
######

from tasks.button_tasks.new_member_verification_button import VerificationButton
from music_player.player_control_panel.control_panel_butons import ControlPanelButtons

from config.bot_info.bot_prefix import BOT_PREFIX



### Persist Views Overwrite ###
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:

            self.add_view(VerificationButton(bot))
            self.add_view(ScocottaButtons())
            self.add_view(DaxlianButtons())
            self.add_view(ControlPanelButtons(bot))

            self.persistent_views_added = True
######


### Intents setup ###
intents = nextcord.Intents.default()
intents.members=True
######


### Bot definitions ###
bot = Bot(command_prefix=BOT_PREFIX, intents=intents)
######



### Modules ###
bot.load_extension("alerts.alerts_starter")
bot.load_extension("tasks.tasks_starter")
bot.load_extension("events.events_starter")
bot.load_extension("music_player.player_starter")
bot.load_extension("commands.commands_starter")
#######


### Manager ###
bot.load_extension("manager")
######



### Discord bot TOKEN  and RUN ###
BOT_TOKEN = config("BOT_TOKEN")
bot.run(BOT_TOKEN)
######