import nextcord
from nextcord.ext import commands


class DeleteBotMessageCommand(commands.Cog):
    """
    With the ID of a message from the bot, the bot deletes the givem message.
    Usefull for deleting messages from DM channels. 
    """

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="limpar", description="Jogue uma rodada de Jokenpo com a Mashiro")
    async def delete_bot_message(self,
            interaction: nextcord.Interaction,
            message_id = nextcord.SlashOption(
                name="id-da-mensagem",
                description="Delete uma mensagem específica do bot",
                required=True,
            )
        ):

        message_deleted = nextcord.Embed(
            title="Mensagem deletada",
            color=0xe42a44
        )

        await interaction.user.create_dm()
        dm = interaction.user.dm_channel
        try:
            message = await dm.fetch_message(int(message_id))
            await nextcord.Message.delete(message)
        except:
            return

        await interaction.send(embed=message_deleted, delete_after=3)


def setup(bot):
    bot.add_cog(DeleteBotMessageCommand(bot))