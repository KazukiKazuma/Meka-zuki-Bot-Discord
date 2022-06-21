import nextcord
from nextcord.ext import commands, tasks
from twitchAPI import Twitch, EventSub
import time
import _secrets_
from utils import streamers_gets, guild_utils
    
    
class StreamData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @tasks.loop(seconds=30)
    async def send_print(self):
        if streamers_gets.streamers == {}:
            return
        for streamer in streamers_gets.streamers:
            guild = self.bot.get_guild(guild_utils.guild_id)
            channel = guild.get_channel(guild_utils.twitch_alert_channel_id)
                
            if streamer in streamers_gets.streamer_alert_messages:
                try:
                    if time.time() - float(streamers_gets.streamer_alert_messages_timestamps[streamer]) < 600:
                        del streamers_gets.streamers[streamer]
                        return
                    
                    old_alert = await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                    await nextcord.Message.delete(old_alert)
                    
                    message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                    id = message.id
                    streamers_gets.streamer_alert_messages[streamer] = id
                    
                except Exception:
                    del streamers_gets.streamer_alert_messages[streamer]
                    
            else:
                message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                id = message.id
                streamers_gets.streamer_alert_messages[streamer] = id
                streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                    
            del streamers_gets.streamers[streamer]
            if streamers_gets.streamers == {}:
                break

    async def on_stream_online(data):
        streamer = data['event']['broadcaster_user_login']
        streamers_gets.streamers[streamer] = streamers_gets.streamers_embeds[streamer]
        
    
    client_id = _secrets_.t_client_id
    client_secret = _secrets_.t_client_secret
    webhook = _secrets_.webhook_redir
    port = _secrets_.webhook_port

    twitch = Twitch(client_id, client_secret)
    twitch.authenticate_app([])

    hook = EventSub(webhook, client_id, port, twitch)
    uuid = twitch.get_users(logins=streamers_gets.watchlist)
    hook.unsubscribe_all()
    hook.start()
    
    position = 0
    for user in uuid['data']:
        user_id = uuid['data'][position]['id']
        hook.listen_stream_online(user_id, on_stream_online)
        position += 1


 
def setup(bot):
    bot.add_cog(StreamData(bot))