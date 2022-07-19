import nextcord


watchlist = [
    "kazukikazuma",
    "scocotta"
]


######################################   EMBEDS   ######################################

kazukikazuma_embed = nextcord.Embed(
    title="Kazuki is Online",
    description="mas é só um teste",
    color=0xe2fecf
)
kazukikazuma_embed.set_thumbnail(url="https://c.tenor.com/C3fD3dTgaPcAAAAC/kazuma-konosuba.gif")
kazukikazuma_embed.set_image(url="https://c.tenor.com/AeMs5ZptdRUAAAAC/world-series-my-body-is-ready.gif")

##

scocotta_embed = nextcord.Embed(
    title="O Scocotta está online galera",
    description="Venham assistir à cocotta guerreirinha e seus delírios."
)

########################################################################################


streamers_embeds = {
    "kazukikazuma":kazukikazuma_embed,
    "scocotta":scocotta_embed,
}

streamers_channels = {
    "kazukikazuma":"https://www.twitch.tv/kazukikazuma",
    "scocotta":"https://www.twitch.tv/scocotta"
}

streamer_roles = {
    "kazukikazuma":"<@&841216624891789332>",
    "scocotta":"<@&967677571904970772>",
}


### DO NOT CHANGE THESE ###
streamers = {}
streamer_alert_messages = {}
streamer_alert_messages_timestamps = {}
streamer_channel_to_update = {}
channels_info = {}
###########################