import nextcord
from nextcord.ext import commands

from tasks.button_tasks.streamers_roles_buttons.daxlian_streamer_buttons import DaxlianButtons

class StreamerDaxlian(commands.Cog):
    """Lets you talk to the bot in slash commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="daxlian")
    @commands.is_owner()
    async def embed_scocotta(self, ctx):
        daxlian_embed_buttons = DaxlianButtons()
        
        image_daxlian = "https://i.imgur.com/5qm2mFa.png"
        icon_daxlian = "https://i.imgur.com/96wUbCg.jpg"
        
        daxlian_embed = nextcord.Embed(
            title = "Daxlian, a vampira da mecha branca",
            description = "e de gosto estético acertivo",
            color = 0x503f88
        )
        
        daxlian_embed.set_thumbnail(url=icon_daxlian)
        daxlian_embed.set_footer(text="Feito por " + self.bot.user.display_name, icon_url=self.bot.user.avatar)
        
        daxlian_embed.add_field(name="\u200b", value="\u200b")
        daxlian_embed.add_field(name="Nós te notificamos!", value=f"Ao clicar no botão vermelho, você receberá o cargo <@&972486314953945168>, que será usado para te notificar quando esta streamer estiver online na Twitch!", inline=False)
        
        daxlian_embed.set_image(url=image_daxlian)
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=daxlian_embed, view=daxlian_embed_buttons)
        
        
def setup(bot):
    bot.add_cog(StreamerDaxlian(bot))