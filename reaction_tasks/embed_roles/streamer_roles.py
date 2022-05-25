from nextcord.ext import commands
import nextcord




###                      ###
###   Streamer Buttons   ###
###                      ###


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






###                      ###
###   Streamer Commands  ###
###                      ###


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
        
        scocotta_embed.add_field(name="ㅤ", value="ㅤ")
        scocotta_embed.add_field(name="Nós te notificamos!", value=f"Ao clicar no botão vermelho, você receberá o cargo <@&967677571904970772>, que será usado para te notificar quando este streamer estiver online na Twitch!", inline=False)
        
        scocotta_embed.set_image(url=image_scocotta)
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=scocotta_embed, view=scocotta_embed_buttons)
        

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
        
        daxlian_embed.add_field(name="ㅤ", value="ㅤ")
        daxlian_embed.add_field(name="Nós te notificamos!", value=f"Ao clicar no botão vermelho, você receberá o cargo <@&972486314953945168>, que será usado para te notificar quando esta streamer estiver online na Twitch!", inline=False)
        
        daxlian_embed.set_image(url=image_daxlian)
        
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=daxlian_embed, view=daxlian_embed_buttons)
    



def setup(bot):
    bot.add_cog(StreamerScocotta(bot))
    bot.add_cog(StreamerDaxlian(bot))