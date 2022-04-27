#from nextcord.ext import commands
#import nextcord
#
#from bot import Bot
#
#class StreamAlert(nextcord.Streaming):
#    """Creates a Button that does something"""
#
#    def __init__(self, bot):
#        super().__init__(timeout=None, name="test", url="test")
#        self.value = None
#        self.bot = bot
#        
#    async def announce_online_on_twitch(self, streaming: nextcord.Streaming):
#        return
#    
#    
#class StreamAlert(commands.Cog):
#    """Creates a Button that does something"""
#
#    def __init__(self, bot):
#        self.bot = bot
#        
#    test_alert = StreamAlert(Bot)
#    
#    async def alert_test_message(self, ctx):
#        await ctx.send_message("Teste Alerta")
#
#
#def setup(bot):
#    bot.add_cog(StreamAlert(bot))