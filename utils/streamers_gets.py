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
kazukikazuma_embed.add_field(name="\u200b", value="https://www.twitch.tv/kazukikazuma")
kazukikazuma_embed.set_image(url="https://c.tenor.com/AeMs5ZptdRUAAAAC/world-series-my-body-is-ready.gif")

##

scocotta_embed = nextcord.Embed(
    title="O Scocotta está online galera",
    description="Cola mais no canal dele para aproveitar"
)

########################################################################################


streamers_embeds = {
    "kazukikazuma":kazukikazuma_embed,
    "scocotta":scocotta_embed,
}

streamers = {}

streamer_roles = {
    "scocotta":"<@&967677571904970772>",
    "kazukikazuma":"<@&841216624891789332>",
}

streamer_alert_messages = {}

streamer_alert_messages_timestamps = {}