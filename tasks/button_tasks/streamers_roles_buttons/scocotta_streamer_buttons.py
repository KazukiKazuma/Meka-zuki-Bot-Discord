import nextcord

class ScocottaButtons(nextcord.ui.View):
    """Creates a Button for the given objective"""

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
        scocotta_linkedin = nextcord.ui.Button(label="linktree", style=nextcord.ButtonStyle.gray, emoji="<:linktree:972542599485329458>", url="https://linktr.ee/scocotta")
        self.add_item(scocotta_linkedin)
        

    async def handle_click_scocotta_role(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id_scocotta = 967677571904970772
        role_scocotta = interaction.guild.get_role(role_id_scocotta)
        assert isinstance(role_scocotta, nextcord.Role)
        
        small_green_coin_url = "https://i.imgur.com/IOtUhEM.gif"
        small_red_coin_url = "https://i.imgur.com/7Xzd1Xs.gif"
        
        scocotta_role_embed_follow = nextcord.Embed(
            description = "Você agora **receberá** notificações relacionadas ao Scocotta!",
            color = 0x83b834
        )
        scocotta_role_embed_follow.set_thumbnail(url=small_green_coin_url)
        
        scocotta_role_embed_unfollow = nextcord.Embed(
            description = "Você **não receberá** mais notificações relacionadas ao Scocotta.",
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


    @nextcord.ui.button(label="Receba notificações sobre Scocotta", style=nextcord.ButtonStyle.danger, emoji="🤍", custom_id="scocotta_notify_me_button")
    async def scocotta_role_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_scocotta_role(button, interaction)
        self.value = 1