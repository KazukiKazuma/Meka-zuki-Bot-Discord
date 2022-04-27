from nextcord.ext import commands
import nextcord


class ScocottaButtons(nextcord.ui.View):
    """Creates a Button that does something"""

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    async def handle_click_scocotta_role(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id_scocotta = 967677571904970772
        role_scocotta = interaction.guild.get_role(role_id_scocotta)
        assert isinstance(role_scocotta, nextcord.Role)
        
        small_green_coin_url = "https://i.imgur.com/IOtUhEM.gif"
        small_red_coin_url = "https://i.imgur.com/7Xzd1Xs.gif"
        
        scocotta_role_embed_follow = nextcord.Embed(
            description = "Você agora receberá notificações relacionadas ao Scocotta!",
            color = 0x83b834
        )
        scocotta_role_embed_follow.set_thumbnail(url=small_green_coin_url)
        
        scocotta_role_embed_unfollow = nextcord.Embed(
            description = "Você não receberá mais notificações relacionadas ao Scocotta.",
            color = 0xe53b44
        )
        scocotta_role_embed_unfollow.set_thumbnail(url=small_red_coin_url)
        
        #when interacted with the red "follow" button
        if role_scocotta in interaction.user.roles:
            await interaction.user.remove_roles(role_scocotta)
            await interaction.response.send_message(embed=scocotta_role_embed_unfollow, ephemeral=True)

        else:
            await interaction.user.add_roles(role_scocotta)
            await interaction.response.send_message(embed=scocotta_role_embed_follow, ephemeral=True)


    async def handle_click_scocotta_social_medias(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            await interaction.response.send_message(f"Twitch do Scotta aqui", ephemeral=True)


    @nextcord.ui.button(label="Receba notificações sobre mim", style=nextcord.ButtonStyle.danger, emoji="🤍", custom_id="scocotta_notify_me_button")
    async def scocotta_role_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_scocotta_role(button, interaction)
        self.value = 1
        
    @nextcord.ui.button(label="Twitch", style=nextcord.ButtonStyle.gray, custom_id="scocotta_social_media_button")
    async def scocotta_social_medias_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_scocotta_social_medias(button, interaction)
        self.value = 2


class EmbedStramersRoles(commands.Cog):
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
            description = "e mais amado da twitch",
            color = 0x9ede3e
        )
        
        scocotta_embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar)
        scocotta_embed.set_thumbnail(url=icon_scocotta)
        scocotta_embed.set_footer(text="Feito por " + self.bot.user.display_name, icon_url=self.bot.user.avatar)
        
        scocotta_embed.add_field(name="Dê follow no Scocotta", value="A twitch dele é muito dahora", inline=False)
        
        scocotta_embed.set_image(url=image_scocotta)
        
        
        await ctx.send(embed=scocotta_embed, view=scocotta_embed_buttons)



def setup(bot):
    bot.add_cog(EmbedStramersRoles(bot))