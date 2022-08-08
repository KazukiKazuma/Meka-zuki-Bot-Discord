import nextcord
from nextcord.ext import commands
from tasks.button_tasks.new_member_verification_button import VerificationButton

class VerificationMessage(commands.Cog):
    """Gives a role to unlock the server to the user who presses the button"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vow")
    @commands.is_owner()
    async def vow(self, ctx):
        vow_button = VerificationButton(self)
        
        scroll_image_url = "https://i.imgur.com/rD1wSr8.png"
        
        embed_vow = nextcord.Embed(
            title = "Juramento da Guilda",
            description = f"Agora é com você, tudo que resta para **entrar para a Guilda** é declarar que entende e **aceita** o que está escrito no [Pergaminho da Boa Convivência](https://discord.com/channels/738510840042356857/739155463186415656/739318903817109575).",
            color = 0x5865f2
        )
        
        embed_vow.set_thumbnail(url=scroll_image_url)
        
        await ctx.send(embed=embed_vow, view=vow_button)



def setup(bot):
    bot.add_cog(VerificationMessage(bot))