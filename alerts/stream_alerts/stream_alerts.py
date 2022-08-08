import nextcord
from nextcord.ext import commands, tasks

from decouple import config

from twitchAPI import Twitch, EventSub

import time

from utils import streamers_gets, guild_utils

from utils.commands_utils import command_modules, module_disabled_message

from config.bot_info import bot_language
from language import languages

code_language = languages.languages[bot_language.CHOSEN_LANGUAGE]

    
    
class StreamAlert(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @tasks.loop(seconds=30)
    async def send_alert_message(self):
        if command_modules['Stream Alerts'] == "Off":
            return
        
        ### print("looping")
        ### print(f"ONLINE: {streamers_gets.streamers}")
        ### print(f"MESSAGES: {streamers_gets.streamer_alert_messages}")
        ### print(f"UPDATE: {streamers_gets.streamer_channel_to_update}")
        ### print(f"TIME: {streamers_gets.streamer_alert_messages_timestamps}")
        if streamers_gets.streamers == {}:
            return
        
        guild = self.bot.get_guild(guild_utils.guild_id)
        channel = guild.get_channel(guild_utils.twitch_alert_channel_id)
        
        temp_streamer_list = streamers_gets.streamers
        
        for streamer in temp_streamer_list:
            ### print(streamers_gets.channels_info)
            
            if streamer in streamers_gets.streamer_alert_messages:
                try:
                    await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                except Exception:
                    del streamers_gets.streamer_alert_messages_timestamps[streamer]
                    
                try:
                    if time.time() - float(streamers_gets.streamer_alert_messages_timestamps[streamer]) < 720:
                        ### print("too soon")
                        del streamers_gets.streamers[streamer]
                        return
                    else:
                        pass
                except Exception:
                    pass
                
                try:
                    old_alert = await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                    await nextcord.Message.delete(old_alert)
                    
                    if streamer in streamers_gets.streamers_embeds:
                        streamers_gets.streamers_embeds[streamer].clear_fields()
                        streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=f">>> [**{streamers_gets.channels_info[streamer]['data'][0]['title']}**]({streamers_gets.streamers_channels[streamer]})\n{code_language.stream_alerts['Streaming']}: {streamers_gets.channels_info[streamer]['data'][0]['game_name']}", inline=False)
                        streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=f"[{code_language.stream_alerts['Watch the stream here']}]({streamers_gets.streamers_channels[streamer]})", inline=False)
                        if streamers_gets.channels_info[streamer]['data'][0]['is_mature'] == True:
                            streamers_gets.streamers_embeds[streamer].set_footer(text=code_language.stream_alerts["This streamer has classified their content as recommended for a mature audience"], icon_url="https://i.imgur.com/4jWXm42.png")
                        else:
                            try:
                                streamers_gets.streamers_embeds[streamer].remove_footer()
                            except Exception:
                                pass
                            
                    else:
                        print(f"<<> Could not find {streamer} in the embed messages list <>>")
                    
                    message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                    # await message.publish()
                    id = message.id
                    streamers_gets.streamer_alert_messages[streamer] = id
                    streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                    
                    del streamers_gets.streamers[streamer]
                    if streamers_gets.streamers == {}:
                        break
                    ### print("time changed on_stream_online resend")
                    
                except Exception:
                    ### print("something went wrong")
                    del streamers_gets.streamer_alert_messages[streamer]
                    
            else:
                if streamer in streamers_gets.streamers_embeds:
                    streamers_gets.streamers_embeds[streamer].clear_fields()
                    streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=f">>> [**{streamers_gets.channels_info[streamer]['data'][0]['title']}**]({streamers_gets.streamers_channels[streamer]})\n{code_language.stream_alerts['Streaming']}: {streamers_gets.channels_info[streamer]['data'][0]['game_name']}", inline=False)
                    streamers_gets.streamers_embeds[streamer].add_field(name="\u200b", value=f"[{code_language.stream_alerts['Watch the stream here']}]({streamers_gets.streamers_channels[streamer]})", inline=False)
                    if streamers_gets.channels_info[streamer]['data'][0]['is_mature'] == True:
                        streamers_gets.streamers_embeds[streamer].set_footer(text=code_language.stream_alerts["This streamer has classified their content as recommended for a mature audience"], icon_url="https://i.imgur.com/4jWXm42.png")
                    else:
                        try:
                            streamers_gets.streamers_embeds[streamer].remove_footer()
                        except Exception:
                            pass
                
                    message = await channel.send(content=streamers_gets.streamer_roles[streamer], embed=streamers_gets.streamers[streamer], delete_after=86300)
                    # await message.publish()
                    id = message.id
                    
                    streamers_gets.streamer_alert_messages[streamer] = id
                    streamers_gets.streamer_alert_messages_timestamps[streamer] = time.time()
                    ### print("time set on_stream_online send")
                else:
                    print(f"<<> Could not find {streamer} in the embed messages list <>>")
                    
                del streamers_gets.streamers[streamer]
                if streamers_gets.streamers == {}:
                    break
            
    @tasks.loop(seconds=60)
    async def update_alert_message(self):
        if command_modules['Stream Alerts'] == "Off":
            return
        
        ### print("looping")
        
        if streamers_gets.streamer_channel_to_update == {}:
            return
        
        ### print(streamers_gets.channels_info)
        
        guild = self.bot.get_guild(guild_utils.guild_id)
        channel = guild.get_channel(guild_utils.twitch_alert_channel_id)
        
        temp_update_list = streamers_gets.streamer_channel_to_update
        
        for streamer in temp_update_list:
            
            if streamer in streamers_gets.streamers_embeds:
                streamers_gets.streamers_embeds[streamer].set_field_at(index=0, name="\u200b", value=f">>> [**{streamers_gets.streamer_channel_to_update[streamer]['event']['title']}**]({streamers_gets.streamers_channels[streamer]})\n{code_language.stream_alerts['Streaming']}: {streamers_gets.streamer_channel_to_update[streamer]['event']['category_name']}", inline=False)
                
                if streamers_gets.streamer_channel_to_update[streamer]['event']['is_mature'] == True:
                    streamers_gets.streamers_embeds[streamer].set_footer(text=code_language.stream_alerts["This streamer has classified their content as recommended for a mature audience"], icon_url="https://i.imgur.com/4jWXm42.png")
                else:
                    try:
                        streamers_gets.streamers_embeds[streamer].remove_footer()
                    except Exception:
                        pass
                
                if streamer in streamers_gets.streamer_alert_messages:
                    try:
                        message = await channel.fetch_message(streamers_gets.streamer_alert_messages[streamer])
                        await message.edit(embed=streamers_gets.streamers_embeds[streamer])
                    except Exception:
                        pass
            
            else:
                print(f"<<> Could not find {streamer} in the embed messages list <>>")
                
            del streamers_gets.streamer_channel_to_update[streamer]
            if streamers_gets.streamer_channel_to_update == {}:
                break
            
    
    async def on_stream_online(data):
        if command_modules['Stream Alerts'] == "Off":
            return
        
        streamer = data['event']['broadcaster_user_login']
        print(f"{streamer} went online at {time.asctime()}")
        
        streamers_gets.channels_info[streamer] = twitch.get_streams(user_id=data['event']['broadcaster_user_id'])   
        streamers_gets.streamers[streamer] = streamers_gets.streamers_embeds[streamer]
    
    async def on_channel_update(data):
        if command_modules['Stream Alerts'] == "Off":
            return
        
        streamer = data['event']['broadcaster_user_login']
        print(f"{streamer} updated at {time.asctime()}")
        
        if streamer not in streamers_gets.streamer_alert_messages:
            return
        else:
            streamers_gets.streamer_channel_to_update[streamer] = data



    CLIENT_ID = config("TWITCH_CLIENT_ID")
    CLIENT_SECRET = config("TWITCH_CLIENT_SECRET")
    WEBHOOK = config("TWITCH_WEBROOK")
    PORT = config("TWITCH_WEBHOOK_PORT")

    global twitch
    twitch = Twitch(CLIENT_ID, CLIENT_SECRET)
    twitch.authenticate_app([])

    global hook
    hook = EventSub(WEBHOOK, CLIENT_ID, PORT, twitch)
    global uuid
    uuid = twitch.get_users(logins=streamers_gets.watchlist)
    hook.unsubscribe_all()
    hook.unsubscribe_on_stop = False
    
    if command_modules['Stream Alerts'] == "On":
        hook.start()
    
    position = 0
    for _ in uuid['data']:
            user_id = uuid['data'][position]['id']
            hook.listen_stream_online(user_id, on_stream_online)
            hook.listen_channel_update(user_id, on_channel_update)
            position += 1
    
    
    
    if command_modules['Stream Alerts'] == "On":
        print(f"-------------------------\nTwitch Webhook connection ESTABLISHED succesfully")
    elif command_modules['Stream Alerts'] == "Off":
        print(f"-------------------------\nTwitch Webhook connection is DISABLED in the modules")
        
    
    async def turn_on_stream_alerts(self):
        hook.start()
        print(f"-------------------------\nTwitch Webhook connection ESTABLISHED succesfully\n-------------------------")
        
    async def turn_off_stream_alerts(self):
        hook.stop()
        print(f"-------------------------\nTwitch Webhook connection ENDED succesfully\n-------------------------")
        
    

    
 
def setup(bot):
    bot.add_cog(StreamAlert(bot))