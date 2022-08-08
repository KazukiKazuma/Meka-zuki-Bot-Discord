import nextcord

class DaxlianButtons(nextcord.ui.View):
    """Creates a Button for the given objective"""

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
        daxlian_linkedin = nextcord.ui.Button(label="linktree", style=nextcord.ButtonStyle.gray, emoji="<:linktree:972542599485329458>", url="https://www.instagram.com/daxlian/")
        self.add_item(daxlian_linkedin)

    async def handle_click_daxlian_role(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id_daxlian = 972486314953945168
        role_daxlian = interaction.guild.get_role(role_id_daxlian)
        assert isinstance(role_daxlian, nextcord.Role)
        
        small_green_coin_url = "https://i.imgur.com/IOtUhEM.gif"
        small_red_coin_url = "https://i.imgur.com/7Xzd1Xs.gif"
        
        daxlian_role_embed_follow = nextcord.Embed(
            description = "Você agora **receberá** notificações relacionadas à Daxlian!",
            color = 0x83b834
        )
        daxlian_role_embed_follow.set_thumbnail(url=small_green_coin_url)
        
        daxlian_role_embed_unfollow = nextcord.Embed(
            description = "Você **não receberá** mais notificações relacionadas à Daxlian.",
            color = 0xe53b44
        )
        daxlian_role_embed_unfollow.set_thumbnail(url=small_red_coin_url)
        
        #when interacted with the red "follow" button
        if role_daxlian in interaction.user.roles:
            await interaction.user.remove_roles(role_daxlian)
            await interaction.response.send_message(embed=daxlian_role_embed_unfollow, ephemeral=True)

        else:
            await interaction.user.add_roles(role_daxlian)
            await interaction.response.send_message(embed=daxlian_role_embed_follow, ephemeral=True)


    @nextcord.ui.button(label="Receba notificações sobre Daxlian", style=nextcord.ButtonStyle.danger, emoji="🤍", custom_id="daxlian_notify_me_button")
    async def scocotta_role_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_daxlian_role(button, interaction)
        self.value = 1