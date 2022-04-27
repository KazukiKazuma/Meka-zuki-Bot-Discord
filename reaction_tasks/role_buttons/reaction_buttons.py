import nextcord
from nextcord.ext import commands


############################  Juramento  ###############################

class VowButton(nextcord.ui.View):
    """Creates a Button that does something"""

    def __init__(self, bot):
        super().__init__(timeout=None)
        self.value = None
        self.bot = bot


    #################  Interaction Handlers ###################

    async def handle_click_accept(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id_vowed = 966451164814139463
        role_vowed = interaction.guild.get_role(role_id_vowed)
        mabinogi_memberrole_id = 739293291752718426
        mabinogi_memberrole = interaction.guild.get_role(mabinogi_memberrole_id)
        mabinogi_civil_role_id = 967849474405838848
        mabinogi_civil_role = interaction.guild.get_role(mabinogi_civil_role_id)
        assert isinstance(role_vowed, nextcord.Role)
        
        green_crystal_image_url = "https://i.imgur.com/CG5XCxq.gif"
        
        accepted_vow_embed = nextcord.Embed(
            title = "Você fez seu Juramento!",
            description = f"Obrigado {interaction.user.display_name}, tendo **feito o juramento**, recebemos você agora de braços abertos como um **Membro da nossa Guilda**, boas vindas à Mabinogi!",
            color = 0x83b834
        )
        accepted_vow_embed.set_thumbnail(url=green_crystal_image_url)
        
        already_accepted_vow_embed = nextcord.Embed(
            title = "Você já fez seu juramento..",
            description = f"Apreciamos o entusiasmo {interaction.user.display_name}, mas você **já fez** seu Juramento e **é atualmente um Membro da Guilda**.",
            color = 0x83b834
        )
        already_accepted_vow_embed.set_thumbnail(url=green_crystal_image_url)
        
        #if user vows
        if role_vowed in interaction.user.roles:
            await interaction.response.send_message(embed=already_accepted_vow_embed, delete_after=5, ephemeral=True)

        else:
            await interaction.user.add_roles(role_vowed)
            await interaction.user.add_roles(mabinogi_memberrole)
            await interaction.user.remove_roles(mabinogi_civil_role)
            await interaction.response.send_message(embed=accepted_vow_embed, delete_after=5, ephemeral=True)


    async def handle_click_reject(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id_vowed = 966451164814139463
        role_vowed = interaction.guild.get_role(role_id_vowed)
        mabinogi_memberrole_id = 739293291752718426
        mabinogi_memberrole = interaction.guild.get_role(mabinogi_memberrole_id)
        mabinogi_civil_role_id = 967849474405838848
        mabinogi_civil_role = interaction.guild.get_role(mabinogi_civil_role_id)
        assert isinstance(role_vowed, nextcord.Role)
        
        red_crystal_image_url = "https://i.imgur.com/uRzApJn.gif"
        
        rejected_vow_embed = nextcord.Embed(
            title = "Você desfez seu seu Juramento",
            description = f"Sentimos muito que tenha decidido **desfazer** seu Juramento {interaction.user.display_name}, torcemos que eventualmente *mude de ideia*.",
            color = 0xe53b44
        )
        rejected_vow_embed.set_thumbnail(url=red_crystal_image_url)
        
        already_rejected_vow_embed = nextcord.Embed(
            title = "Sentimos muito...",
            description = f"A decisão é sua {interaction.user.display_name}, mas torcemos para que venha a fazer seu Juramento eventualmente.",
            color = 0xe53b44
        )
        already_rejected_vow_embed.set_thumbnail(url=red_crystal_image_url)
        
        #if user doesn't vows
        if role_vowed in interaction.user.roles:
            await interaction.user.remove_roles(role_vowed)
            await interaction.user.remove_roles(mabinogi_memberrole)
            await interaction.user.add_roles(mabinogi_civil_role)
            await interaction.response.send_message(embed=rejected_vow_embed, delete_after=5, ephemeral=True)

        else:
            await interaction.response.send_message(embed=already_rejected_vow_embed, delete_after=5, ephemeral=True)


    ##################  Buttons  #######################

    @nextcord.ui.button(label="Fazer o Juramento", style=nextcord.ButtonStyle.blurple, emoji="🏷", custom_id="i_sware_vow_button")
    async def guild_vow_accept(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_accept(button, interaction)
        
    @nextcord.ui.button(label="Pensando melhor...", style=nextcord.ButtonStyle.gray, custom_id="i_do_not_sware_vow_button")
    async def guild_vow_reject(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.handle_click_reject(button, interaction)

########################################################################



class ButtonInteraction(commands.Cog):
    """Makes the bot send a message with buttons"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vow")
    @commands.is_owner()
    async def vow(self, ctx):
        vow_button = VowButton(self)
        
        scroll_image_url = "https://i.imgur.com/rD1wSr8.png"
        
        embed_vow = nextcord.Embed(
            title = "Juramento da Guilda",
            description = f"Agora é com você, tudo que resta para **entrar para a Guilda** é declarar que entende e **aceita** o que está escrito no [Pergaminho da Boa Convivência](https://discord.com/channels/738510840042356857/739155463186415656/739318903817109575).",
            color = 0x5865f2
        )
        
        embed_vow.set_thumbnail(url=scroll_image_url)
        
        await ctx.send(embed=embed_vow, view=vow_button)



def setup(bot):
    bot.add_cog(ButtonInteraction(bot))