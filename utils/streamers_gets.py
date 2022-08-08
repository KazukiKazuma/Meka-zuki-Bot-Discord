import nextcord


watchlist = [
    "kazukikazuma",
    "scocotta"
]


######################################   CUSTOM EMBEDS   ##################################

kazukikazuma_embed = nextcord.Embed(
    title="Kazuki está Online",
    description="Sinta-se a vontade para vir à live e trocar uma ideia",
    color=0xb87341
)
kazukikazuma_embed.set_thumbnail(url="https://i.imgur.com/37jlYoS.jpg")
kazukikazuma_embed.set_image(url="https://i.imgur.com/QeMME1K.gif")

##

scocotta_embed = nextcord.Embed(
    title="Live do Scocotta começando!",
    description="Venham assistir as lives e aprender como nao se deve jogar!",
    color=0x83b834
)
scocotta_embed.set_thumbnail(url="https://i.imgur.com/65CinUN.png")
scocotta_embed.set_image(url="https://i.imgur.com/lBwH69L.jpg")

###########################################################################################


streamers_embeds = {
    "kazukikazuma":kazukikazuma_embed,
    "scocotta":scocotta_embed,
}

streamers_channels = {
    "kazukikazuma":"https://www.twitch.tv/kazukikazuma",
    "scocotta":"https://www.twitch.tv/scocotta",
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