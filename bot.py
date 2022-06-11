import _secrets_
import nextcord

from nextcord.ext import commands

# from twitchAPI import Twitch, EventSub

from reaction_tasks.embed_roles.streamer_roles import DaxlianButtons, ScocottaButtons
from reaction_tasks.role_buttons.reaction_buttons import VowButton
from music_player.youtube_player import ControlPanel
from utils import guild_utils



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
bot = Bot(command_prefix=guild_utils.prefix, intents=intents)
######



### Commands ###
bot.load_extension("commands.slash_commands.slash_talks")
bot.load_extension("commands.slash_commands.jokenpo")
bot.load_extension("commands.standard_commands.minecraft_server_status")
bot.load_extension("reaction_tasks.role_buttons.reaction_buttons")
bot.load_extension("reaction_tasks.embed_roles.streamer_roles")
bot.load_extension("events.on_join_server")
bot.load_extension("reaction_tasks.reaction_roles.registration")
# bot.load_extension("alerts._stream_alerts_")
bot.load_extension("commands.standard_commands.reaction_message")
bot.load_extension("music_player.youtube_player")
bot.load_extension("commands.slash_commands.help_command")
bot.load_extension("commands.slash_commands.dice")
#######



# async def send_print():
#     print(streamer)
    
#     guild = bot.get_guild(738510840042356857)
#     channel = guild.get_channel(739176859127775323)
    
#     print(channel)
    
#     await channel.send("O Kazuki está online mas esse é apenas um teste.")

# async def on_stream_online(data):
#     print("It worked until here")
#     global streamer
#     streamer = data['event']['broadcaster_user_login']
    
#     guild = bot.get_guild(738510840042356857)
#     channel = guild.get_channel(739176859127775323)
    
#     await channel.send("O Kazuki está online mas esse é apenas um teste.")
    
#     await send_print()
   
# client_id = _secrets_.t_client_id
# client_secret = _secrets_.t_client_secret

# twitch = Twitch(client_id, client_secret)
# twitch.authenticate_app([])

# hook = EventSub(_secrets_.https_redir, client_id, 8080, twitch)
# uuid = twitch.get_users(logins=["kazukikazuma"])
# user_id = uuid['data'][0]['id']
# hook.unsubscribe_all()
# hook.start()
# hook.listen_stream_online(user_id, on_stream_online)



### Manager ###
bot.load_extension("manager")
######


### Discord bot TOKEN ###
bot_token = _secrets_.bot_token
bot.run(bot_token)
######