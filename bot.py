import _discord_bot_token_
import nextcord

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
        

intents = nextcord.Intents.default()
intents.members=True

### Bot definitions ###

bot = Bot(command_prefix="!mkzk ", intents=intents)
######


### Gives Basic Roles to New Members ###
@bot.event
async def on_member_join(ctx):
    role_join = ctx.guild.get_role(967849474405838848)
    role_join_separator_1 = ctx.guild.get_role(967693392433807420)
    role_join_separator_2 = ctx.guild.get_role(967677263430713344)
    role_join_separator_3 = ctx.guild.get_role(928409990589448212)
    await ctx.add_roles(role_join, role_join_separator_1, role_join_separator_2, role_join_separator_3)
######


### Path Definitions ###
print("------")
######


### Commands ###
bot.load_extension("commands.slash_commands.slash_talks")
bot.load_extension("reaction_tasks.role_buttons.reaction_buttons")
bot.load_extension("reaction_tasks.embed_roles.streamer_roles")
#bot.load_extension("alerts.stream_alerts")
#######


### Manager ###
bot.load_extension("manager")
######


### Discord bot TOKEN ###
bot_token = _discord_bot_token_.token
bot.run(bot_token)
######