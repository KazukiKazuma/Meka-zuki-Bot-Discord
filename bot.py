import _discord_bot_token_
import nextcord

from twitchAPI.twitch import Twitch
from twitchAPI import EventSub

from nextcord.ext import commands

from reaction_tasks.embed_roles.streamer_roles import ScocottaButtons
from reaction_tasks.role_buttons.reaction_buttons import VowButton



### Persist Views Overwrite ###
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:

            self.add_view(VowButton(bot))
            self.add_view(ScocottaButtons())

            self.persistent_views_added = True
######




# async def on_stream_online(data:dict):
#     print(data)
#     if "Scocotta" in data:
#         alert_channel = bot.get_channel(739162342314606622)
#         await alert_channel.send("Teste")

# twitch = Twitch(client_id, client_secret)
# twitch.authenticate_app([])

# hook = EventSub("", client_id, 8080, twitch)
# uuid = twitch.get_users(logins=["danisor"])
# user_id = uuid['data'][0]['id']
# hook.unsubscribe_all()
# hook.start()
# hook.listen_stream_online(user_id, on_stream_online)




### Intents setup ###
intents = nextcord.Intents.default()
intents.members=True
######


### Bot definitions ###
bot = Bot(command_prefix="!msr ", intents=intents)
######


### Commands ###
bot.load_extension("commands.slash_commands.slash_talks")
bot.load_extension("commands.slash_commands.slash_minecraft_server_status")
bot.load_extension("reaction_tasks.role_buttons.reaction_buttons")
bot.load_extension("reaction_tasks.embed_roles.streamer_roles")
bot.load_extension("events.on_join_server")
bot.load_extension("reaction_tasks.reaction_roles.registration")
#bot.load_extension("alerts.stream_alerts")
#######


### Manager ###
bot.load_extension("manager")
######


### Discord bot TOKEN ###
bot_token = _discord_bot_token_.token
bot.run(bot_token)
######