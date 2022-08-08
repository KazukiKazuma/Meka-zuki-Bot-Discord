from nextcord.ext import commands
import nextcord
import random
from utils.commands_utils import command_modules, module_disabled_message


class DiceCog(commands.Cog):
    """Lets you roll a dice or combination of dices"""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="rolagem", description="Faça uma rolagem de dados")
    async def dice(self,
            interaction: nextcord.Interaction,
            quantity : int = nextcord.SlashOption(
                name="quantidade",
                description="Escolha quantos dados quer jogar",
                required=True,
            ),
            type = nextcord.SlashOption(
                name="tipo",
                description="Escolha qual tipo de dado quer jogar",
                required=True,
                choices=["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
            ),
            bonus_quantity : int = nextcord.SlashOption(
                name="quantidade-de-dados-bônus",
                description="Escolha quantos dados quer jogar e adicionar o resultado à sua rolagem base",
                required=False,
            ),
            bonus_type = nextcord.SlashOption(
                name="tipo-do-dado-bônus",
                description="Escolha qual tipo de dado quer jogar para sua rolagem bônus",
                required=False,
                choices=["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
            )
            ):
        
        
        
        if quantity== 0 or bonus_quantity==0:
            response_message = nextcord.Embed(
                color=0xe42a44,
                description="Este comando não aceita `0` no campo de quantidade para os dados. Por favor tente outro número."
            )
            return await interaction.send(embed=response_message, ephemeral=True)
        
        try:
            if quantity>100 or bonus_quantity>100:
                response_message = nextcord.Embed(
                    color=0xe42a44,
                    description="Sinto muito, mas meu limite de dados são `100` de cada."
                )
                return await interaction.send(embed=response_message, ephemeral=True)
        except Exception:
            pass
        
        
        await interaction.response.defer()
        
        
        if quantity == 1 and bonus_quantity is None:
            result_message = nextcord.Embed(
                title="Este foi o resultado:",
                color=0xf192a8
            )
        else:
            result_message = nextcord.Embed(
                title="Estes foram os resultados:",
                color=0xf192a8
            )
            
        if bonus_type is not None:
            result_message.set_author(name=f"{interaction.user.display_name} fez uma rolagem de |{quantity}x {type}| com |{bonus_quantity}x {bonus_type}| de bônus", icon_url=interaction.user.display_avatar)
        else:
            result_message.set_author(name=f"{interaction.user.display_name} fez uma rolagem de |{quantity}x {type}|", icon_url=interaction.user.display_avatar)
        
        
        result = 0
        roll_number = 0
        
        if type == "d4":
            for _ in range(quantity):
                resultd4 = random.randint(1,4)
                result += resultd4
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d4:984685302775947324> Rolagem base: `{resultd4}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d4:984685302775947324>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d4:984685302775947324>: `{resultd4}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*4}`, e você conseguiu `{result}`", inline=False)
        
        elif type == "d6":
            for _ in range(quantity):
                resultd6 = random.randint(1,6)
                result += resultd6
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d6:984685322778587136> Rolagem base: `{resultd6}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d6:984685322778587136>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d6:984685322778587136>: `{resultd6}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*6}`, e você conseguiu `{result}`", inline=False)
        
        elif type == "d8":
            for _ in range(quantity):
                resultd8 = random.randint(1,8)
                result += resultd8
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d8:984685335738990602> Rolagem base: `{resultd8}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d8:984685335738990602>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d8:984685335738990602>: `{resultd8}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*8}`, e você conseguiu `{result}`", inline=False)
        
        elif type == "d10":
            for _ in range(quantity):
                resultd10 = random.randint(1,10)
                result += resultd10
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d10:984685347625660426> Rolagem base: `{resultd10}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d10:984685347625660426>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d10:984685347625660426>: `{resultd10}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*10}`, e você conseguiu `{result}`", inline=False)
        
        elif type == "d12":
            for _ in range(quantity):
                resultd12 = random.randint(1,12)
                result += resultd12
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d12:984685367737327627> Rolagem base: `{resultd12}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d12:984685367737327627>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d12:984685367737327627>: `{resultd12}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*12}`, e você conseguiu `{result}`", inline=False)
                
        elif type == "d20":
            for _ in range(quantity):
                resultd20 = random.randint(1,20)
                result += resultd20
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"<:d20:984685380198629429> Rolagem base: `{resultd20}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"<:d20:984685380198629429>**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado <:d20:984685380198629429>: `{resultd20}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*20}`, e você conseguiu `{result}`", inline=False)
                
        elif type == "d100":
            for _ in range(quantity):
                resultd100 = random.randint(1,100)
                result += resultd100
                roll_number += 1
                if quantity == 1:
                    if bonus_quantity is not None:
                        result_message.add_field(name="\u200b", value=f"??? Rolagem base: `{resultd100}`")
                    else:
                        result_message.add_field(name="\u200b", value=f"???**:**ㅤ`{result}`")
                elif quantity <= 12:
                    result_message.add_field(name="\u200b", value=f"*{roll_number}*º Dado ???: `{resultd100}`  **|**ㅤ")
            if quantity > 12:
                result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{quantity*100}`, e você conseguiu `{result}`", inline=False)
        
        
        
        if bonus_type is not None:
            if bonus_quantity > 1:
                result_message.add_field(name="\u200b", value="Dados de rolagem **bônus**:", inline=False)
            
            bonus_result = 0
            bonus_roll_number = 0
            
            if bonus_type == "d4":
                for _ in range(bonus_quantity):
                    bonus_resultd4 = random.randint(1,4)
                    bonus_result += bonus_resultd4
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d4:984685302775947324> Rolagem bônus: `{bonus_resultd4}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d4:984685302775947324>: `{bonus_resultd4}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem bônus, o máximo resultado possível seria `{bonus_quantity*4}`, e você conseguiu `{bonus_result}`", inline=False)
        
            elif bonus_type == "d6":
                for _ in range(bonus_quantity):
                    bonus_resultd6 = random.randint(1,6)
                    bonus_result += bonus_resultd6
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d6:984685322778587136> Rolagem bônus: `{bonus_resultd6}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d6:984685322778587136>: `{bonus_resultd6}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem bônus, o máximo resultado possível seria `{bonus_quantity*6}`, e você conseguiu `{bonus_result}`", inline=False)
            
            elif bonus_type == "d8":
                for _ in range(bonus_quantity):
                    bonus_resultd8 = random.randint(1,8)
                    bonus_result += bonus_resultd8
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d8:984685335738990602> Rolagem bônus: `{bonus_resultd8}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d8:984685335738990602>: `{bonus_resultd8}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{bonus_quantity*8}`, e você conseguiu `{bonus_result}`", inline=False)
            
            elif bonus_type == "d10":
                for _ in range(bonus_quantity):
                    bonus_resultd10 = random.randint(1,10)
                    bonus_result += bonus_resultd10
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d10:984685347625660426> Rolagem bônus: `{bonus_resultd10}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d10:984685347625660426>: `{bonus_resultd10}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{bonus_quantity*10}`, e você conseguiu `{bonus_result}`", inline=False)
            
            elif bonus_type == "d12":
                for _ in range(bonus_quantity):
                    bonus_resultd12 = random.randint(1,12)
                    bonus_result += bonus_resultd12
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d12:984685367737327627> Rolagem bônus: `{bonus_resultd12}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d12:984685367737327627>: `{bonus_resultd12}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{bonus_quantity*12}`, e você conseguiu `{bonus_result}`", inline=False)
                    
            elif bonus_type == "d20":
                for _ in range(bonus_quantity):
                    bonus_resultd20 = random.randint(1,20)
                    bonus_result += resultd20
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"<:d20:984685380198629429> Rolagem bônus: `{bonus_resultd20}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado <:d20:984685380198629429>: `{bonus_resultd20}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{bonus_quantity*20}`, e você conseguiu `{bonus_result}`", inline=False)
                    
            elif bonus_type == "d100":
                for _ in range(bonus_quantity):
                    bonus_resultd100 = random.randint(1,100)
                    bonus_result += bonus_resultd100
                    bonus_roll_number += 1
                    if bonus_quantity == 1:
                        result_message.add_field(name="\u200b", value=f"??? Rolagem bônus: `{bonus_resultd100}`")
                    elif bonus_quantity <= 6:
                        result_message.add_field(name="\u200b", value=f"*{bonus_roll_number}*º Dado ???: `{bonus_resultd100}`  **|**ㅤ")
                if bonus_quantity > 6:
                    result_message.add_field(name="\u200b", value=f"Nesta rolagem, o máximo resultado possível seria `{bonus_quantity*100}`, e você conseguiu `{bonus_result}`", inline=False)
        
        
        if bonus_type is not None:
            result_message.add_field(name="\u200b", value=f"**Resultado final:**ㅤ{result} + {bonus_result} = `{result + bonus_result}`", inline=False)
        elif quantity > 1:
            result_message.add_field(name="\u200b", value=f"**Resultado final:**ㅤ`{result}`", inline=False)
            
        try:
            if quantity>12 or bonus_quantity>6:
                result_message.add_field(name="\u200b", value="___", inline=False)
                result_message.set_footer(text="Peço perdão, mas não consegui mostrar todos os resultados individuais dessa rolagem devida a alta quantidade de dados", icon_url=self.bot.user.display_avatar)
        except Exception:
            pass
        
        
        
        await interaction.send(embed=result_message, delete_after=10800)


def setup(bot):
    bot.add_cog(DiceCog(bot))