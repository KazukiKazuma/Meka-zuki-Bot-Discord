# import nextcord
# import asyncio
# from twitchAPI.twitch import Twitch
# from twitchAPI import EventSub

@asyncio.coroutine
async def connect_to_twitch():

    twitch = Twitch(client_id, client_secret)
    twitch.authenticate_app([])

    TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/kraken/streams/{}"

    API_HEADERS = {
        'Client-ID' : client_id,
        'Accept' : 'application/vnd.twitchtv.v5+json',
    }

    hook = EventSub("", client_id, 8080, twitch)
    uuid = twitch.get_users(logins=["fabiob_rosa"])
    user_id = uuid['data'][0]['id']
    hook.unsubscribe_all()
    hook.start()
    hook.listen_stream_online(user_id, on_stream_online)


async def on_stream_online(data:dict):
    print(data)
    channel = bot.get_channel(739176859127775323)
    await channel.send("Teste")

    
asyncio.run(connect_to_twitch())