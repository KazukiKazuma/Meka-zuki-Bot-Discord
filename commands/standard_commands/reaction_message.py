import nextcord
from nextcord.ext import commands


class RegistrationMessage(commands.Cog):
    """Makes the bot send a message with buttons"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="registerroleplay")
    @commands.is_owner()
    async def registerroleplay(self, ctx):
        
        bot = self.bot
        
        guild = bot.get_guild(738510840042356857)
        role1 = guild.get_role(969492005577183253)
        role2 = guild.get_role(969560877860794389)
        role3 = guild.get_role(969561374688673812)
        role4 = guild.get_role(969562392927272980)
        role5 = guild.get_role(969561839333695509)
        role6 = guild.get_role(969562114983337995)
        role7 = guild.get_role(739174493850828973)
        role8 = guild.get_role(968305659588255824)
        bot_id = guild.get_member(bot.user.id)
        id_image_url = "https://i.imgur.com/4NkVgk1.png"
        
        reaction_registration = nextcord.Embed(
            title = "Registre se ID de Membro",
            description = f"caracterize-se um pouco para que a guilda saiba mais sobre você",
            color = 0xaacde0
        )
        
        reaction_registration.set_thumbnail(url=id_image_url)
        
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        reaction_registration.add_field(name="Humano 🎎", value='Sem muito segredo, o "bom" e velho humano', inline=False)
        reaction_registration.add_field(name="Elfo 🧝‍♂️", value='Orelhas pontudas, curte um misticismo e é posssivelmente capáz de explicar tudo com base no alinhamento de corpos celestes', inline=False)
        reaction_registration.add_field(name="Anão 👷‍♂️", value='Um inéxplicável impulso de acumular riquezas e uma insaciável sede por cerveja', inline=False)
        reaction_registration.add_field(name="Hobbit 👨‍🌾", value='Sua casa é seu palácio, adora a natureza e se impressiona com fogos de artifício', inline=False)
        reaction_registration.add_field(name="Kemono 🦊", value='Possiu orelhas, calda, focinho, mas ainda prefere se portar como um bípede', inline=False)
        reaction_registration.add_field(name="Sobrenatural 🌑", value='Um estranho impulso por beber sangue, ou uivar para a lua, atravessar portas sem abri-las, etc', inline=False)
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        reaction_registration.add_field(name="Maior de 🔞 anos", value='Se você já é Maior de Idade e assume responsabilidade pelos seus atos', inline=False)
        reaction_registration.add_field(name="Alicchia 🧩", value='Se você gostaria de ficar informado sobre nosso servidor de Minecraft', inline=False)
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        
        
        reaction_registration.set_footer(text="O primeiro grupo de cargos e denominações são puramente voltados ao Roleplay e não foram intencionados a serem levados a sério")
        
        message_to_react_to = await ctx.send(embed=reaction_registration)
        
        
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🎎")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🧝‍♂️")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="👷‍♂️")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="👨‍🌾")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🦊")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🌑")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🔞")
        await nextcord.Message.add_reaction(message_to_react_to, emoji="🧩")
        
        await bot_id.remove_roles(role1, role2, role3, role4, role5, role6, role7, role8)


def setup(bot):
    bot.add_cog(RegistrationMessage(bot))