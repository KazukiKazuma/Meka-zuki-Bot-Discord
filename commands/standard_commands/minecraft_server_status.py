from nextcord.ext import commands
import nextcord


class MineServerStatus(commands.Cog):
    """Lets you talk to the bot in slash commands"""

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name="serveronline")
    @commands.is_owner()
    async def serveronline(self, ctx):
        
        guild = self.bot.get_guild(738510840042356857)
        channel = guild.get_channel(968295149102825522)
        
        online_image_url = "https://i.imgur.com/XVI5czX.gif"
        
        alicchia_online = nextcord.Embed(
        title="Alicchia está ONLINE!",
        description="Nosso servidor de minecraft está online e funcionando. Você pode se conectar e jogar agora mesmo!",
        color = 0x83b834
    )
        alicchia_online.set_thumbnail(url=online_image_url)
        
        await channel.purge(limit=2)
        await ctx.send(embed=alicchia_online)
        
    @commands.command(name="serveroffline")
    @commands.is_owner()
    async def serveroffline(self, ctx):
        
        guild = self.bot.get_guild(738510840042356857)
        channel = guild.get_channel(968295149102825522)
        
        offline_image_url = "https://i.imgur.com/frS9UZn.gif"
        
        alicchia_offline = nextcord.Embed(
        title = "Alicchia está OFFLINE",
        description = "Nosso servidor de Minecraft se encontra offline no momento, pedimos desculpas e que por favor aguarde mais um pouco.",
        color = 0xe53b44
    )
        alicchia_offline.set_thumbnail(url=offline_image_url)
        
        await channel.purge(limit=2)
        await ctx.send(embed=alicchia_offline)



def setup(bot):
    bot.add_cog(MineServerStatus(bot))