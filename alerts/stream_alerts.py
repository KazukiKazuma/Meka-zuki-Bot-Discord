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
    async def send_alert_message(self):
        ###print(f"ONLINE: {streamers_gets.streamers}")
        ###print(f"MESSAGES: {streamers_gets.streamer_alert_messages}")
        ###print(f"UPDATE: {streamers_gets.streamer_channel_to_update}")
        ###print(f"TIME: {streamers_gets.streamer_alert_messages_timestamps}")
        if streamers_gets.streamers == {}:
            return
        
        guild = self.bot.get_guild(guild_utils.guild_id)
        channel = guild.get_channel(guild_utils.twitch_alert_channel_id)
        
        for streamer in streamers_gets.streamers:     
            if streamer in streamers_gets.streamer_alert_messages:
                if time.time() - float(streamers_gets.streamer_alert_messages_timestamps[streamer]) < 720:
                    ###print("too soon")
                    del streamers_gets.streamers[streamer]
                    return
                
                try:
                    old_alert = await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                    await nextcord.Message.delete(old_alert)
                    
                    streamers_gets.streamers_embeds[streamer].clear_fields()
                    streamers_gets.streamers_embeds[streamer].add_field(name=f"\u200b\n{streamers_gets.channels_info[streamer]['data'][0]['title']}", value=f"`Transmitindo: {streamers_gets.channels_info[streamer]['data'][0]['game_name']}`", inline=True)
                    streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=streamers_gets.streamers_channels[streamer], inline=False)
                    if streamers_gets.channels_info[streamer]['data'][0]['is_mature'] == "True":
                        streamers_gets.streamers_embeds[streamer].set_footer(text="Este streamer classificou o próprio conteúdo como não recomendado para menores de idade", icon_url="https://i.imgur.com/y99xu8H.png")
                    else:
                        try:
                            streamers_gets.streamers_embeds[streamer].remove_footer()
                        except Exception:
                            pass
                    
                    message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                    await message.publish()
                    id = message.id
                    streamers_gets.streamer_alert_messages[streamer] = id
                    streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                    ###print("time changed on_stream_online resend")
                    
                except Exception:
                    ###print("something went wrong")
                    del streamers_gets.streamer_alert_messages[streamer]
                    
            else:
                streamers_gets.streamers_embeds[streamer].clear_fields()
                streamers_gets.streamers_embeds[streamer].add_field(name=f"\u200b\n{streamers_gets.channels_info[streamer]['data'][0]['title']}", value=f"`Transmitindo: {streamers_gets.channels_info[streamer]['data'][0]['game_name']}`", inline=True)
                streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=streamers_gets.streamers_channels[streamer], inline=False)
                if streamers_gets.channels_info[streamer]['data'][0]['is_mature'] == True:
                    streamers_gets.streamers_embeds[streamer].set_footer(text="Este streamer classificou o próprio conteúdo como não recomendado para menores de idade", icon_url="https://i.imgur.com/y99xu8H.png")
                else:
                    try:
                        streamers_gets.streamers_embeds[streamer].remove_footer()
                    except Exception:
                        pass
                
                message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                await message.publish()
                id = message.id
                streamers_gets.streamer_alert_messages[streamer] = id
                streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                ###print("time set on_stream_online send")
                    
            del streamers_gets.streamers[streamer]
            if streamers_gets.streamers == {}:
                break
            
    @tasks.loop(seconds=60)
    async def update_alert_message(self):
        if streamers_gets.streamer_channel_to_update == {}:
            return
        
        guild = self.bot.get_guild(guild_utils.guild_id)
        channel = guild.get_channel(guild_utils.twitch_alert_channel_id)
        
        for streamer in streamers_gets.streamer_channel_to_update:
            streamers_gets.streamers_embeds[streamer].set_field_at(index=0, name=f"\u200b\n{streamers_gets.streamer_channel_to_update[streamer]['event']['title']}", value=f"`Transmitindo: {streamers_gets.streamer_channel_to_update[streamer]['event']['category_name']}`", inline=True)
            
            if streamers_gets.streamer_channel_to_update[streamer]['event']['is_mature'] == True:
                streamers_gets.streamers_embeds[streamer].set_footer(text="Este streamer classificou o próprio conteúdo como não recomendado para menores de idade", icon_url="https://i.imgur.com/y99xu8H.png")
            else:
                try:
                    streamers_gets.streamers_embeds[streamer].remove_footer()
                except Exception:
                    pass
            
            try:
                message = await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                await message.edit(embed=streamers_gets.streamers_embeds[streamer])
            except Exception:
                streamers_gets.streamers_embeds[streamer].clear_fields()
                streamers_gets.streamers_embeds[streamer].add_field(name=f"\u200b\n{streamers_gets.channels_info[streamer]['data'][0]['title']}", value=f"`Transmitindo: {streamers_gets.channels_info[streamer]['data'][0]['game_name']}`", inline=True)
                streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=streamers_gets.streamers_channels[streamer], inline=False)
                if streamers_gets.channels_info[streamer]['data'][0]['is_mature'] == True:
                    streamers_gets.streamers_embeds[streamer].set_footer(text="Este streamer classificou o próprio conteúdo como não recomendado para menores de idade", icon_url="https://i.imgur.com/y99xu8H.png")
                else:
                    try:
                        streamers_gets.streamers_embeds[streamer].remove_footer()
                    except Exception:
                        pass
                message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                await message.publish()
                id = message.id
                streamers_gets.streamer_alert_messages[streamer] = id
                streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                ###print("time changed on_channel_update")
                
            del streamers_gets.streamer_channel_to_update[streamer]
            if streamers_gets.streamer_channel_to_update == {}:
                break
            
    

    async def on_stream_online(data):
        streamer = data['event']['broadcaster_user_login']
        ###print(f"{streamer} online")
        
        streamers_gets.channels_info[streamer] = twitch.get_streams(user_id=data['event']['broadcaster_user_id'])   
        streamers_gets.streamers[streamer] = streamers_gets.streamers_embeds[streamer]
        
    async def on_channel_update(data):
        streamer = data['event']['broadcaster_user_login']
        ###print(f"{streamer} updated")
        
        if streamer not in streamers_gets.streamer_alert_messages:
            return
        else:
            streamers_gets.streamer_channel_to_update[streamer] = data



    client_id = _secrets_.t_client_id
    client_secret = _secrets_.t_client_secret
    webhook = _secrets_.webhook_redir
    port = _secrets_.webhook_port

    global twitch
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
        hook.listen_channel_update(user_id, on_channel_update)
        position += 1

 
def setup(bot):
    bot.add_cog(StreamData(bot))