import nextcord
from nextcord.ext import commands


class RegistrationMessage(commands.Cog):
    """Makes the bot send a message with buttons"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="registerroleplay")
    @commands.is_owner()
    async def registerroleplay(self, ctx):
        
        guild = self.bot.get_guild(738510840042356857)
        
        roles = [
            969492005577183253,
            969560877860794389,
            969561374688673812,
            969562392927272980,
            969561839333695509,
            969562114983337995,
            739174493850828973,
            968305659588255824
        ]

        bot_id = guild.get_member(self.bot.user.id)
        id_image_url = "https://i.imgur.com/4NkVgk1.png"
        
        reaction_registration = nextcord.Embed(
            title = "Registre seu ID de Membro",
            description = f"caracterize-se um pouco para que a guilda saiba mais sobre você",
            color = 0xaacde0
        )
        
        reaction_registration.set_thumbnail(url=id_image_url)
        
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        reaction_registration.add_field(name="Humano 🎎", value='Sem muito segredo, o "bom" e velho humano', inline=False)
        reaction_registration.add_field(name="Elfo 🧝‍♂️", value='Orelhas pontudas, curte um misticismo e é posssivelmente capáz de explicar tudo com base no alinhamento de corpos celestes', inline=False)
        reaction_registration.add_field(name="Anão 👷‍♂️", value='Um inéxplicável predisposição por acumular riquezas e uma insaciável sede por cerveja', inline=False)
        reaction_registration.add_field(name="Hobbit 👨‍🌾", value='Sua casa é seu palácio, adora a natureza e se impressiona com fogos de artifício', inline=False)
        reaction_registration.add_field(name="Kemono 🦊", value='Possiu orelhas de animal, calda, mas prefere se portar como um bípede', inline=False)
        reaction_registration.add_field(name="Sobrenatural 🌑", value='Um estranho impulso por beber sangue, ou uivar para a lua, atravessar portas sem abri-las, etc', inline=False)
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        reaction_registration.add_field(name="Maior de 🔞 anos", value='Se você já é Maior de Idade e assume responsabilidade pelos seus atos', inline=False)
        reaction_registration.add_field(name="Alicchia 🧩", value='Se você gostaria de se manter informado sobre nosso servidor de Minecraft', inline=False)
        reaction_registration.add_field(name="ㅤ", value='ㅤ')
        
        
        reaction_registration.set_footer(text="O primeiro grupo de cargos e denominações são puramente voltados ao Roleplay e não foram intencionados a serem levados a sério")
        
        message_to_react_to = await ctx.send(embed=reaction_registration)
        
        emojis = ["🎎","🧝‍♂️","👷‍♂️","👨‍🌾","🦊","🌑","🔞","🧩"]
        
        for emoji in emojis:
            await nextcord.Message.add_reaction(message_to_react_to, emoji=emoji)
        
        for role in roles:
            await bot_id.remove_roles(guild.get_role(role))


def setup(bot):
    bot.add_cog(RegistrationMessage(bot))