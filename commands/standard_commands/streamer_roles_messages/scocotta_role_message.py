import nextcord
from nextcord.ext import commands

from tasks.button_tasks.streamers_roles_buttons.scocotta_streamer_buttons import ScocottaButtons


class StreamerScocotta(commands.Cog):
    """Lets you talk to the bot in slash commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="scocotta")
    @commands.is_owner()
    async def embed_scocotta(self, ctx):
        scocotta_embed_buttons = ScocottaButtons()
        
        image_scocotta = "https://i.ibb.co/m8Z0Dqr/scocotta-20200926-180429-120116042-702630010356895-7364293873797302914-n.jpg"
        icon_scocotta = "https://static-cdn.jtvnw.net/jtv_user_pictures/9b5670cf-25ad-445a-81f7-88e3546ada46-profile_image-300x300.png"
        
        scocotta_embed = nextcord.Embed(
            title = "Scocotta, o mais temido dos sete mares",
            description = "e mais gente boa da twitch",
            color = 0x9ede3e
        )

        scocotta_embed.set_thumbnail(url=icon_scocotta)
        scocotta_embed.set_footer(text="Feito por " + self.bot.user.display_name, icon_url=self.bot.user.avatar)
        
        scocotta_embed.add_field(name="\u200b", value="\u200b")
        scocotta_embed.add_field(name="Nós te notificamos!", value=f"Ao clicar no botão vermelho, você receberá o cargo <@&967677571904970772>, que será usado para te notificar quando este streamer estiver online na Twitch!", inline=False)
        
        scocotta_embed.set_image(url=image_scocotta)
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=scocotta_embed, view=scocotta_embed_buttons)
        
        
def setup(bot):
    bot.add_cog(StreamerScocotta(bot))