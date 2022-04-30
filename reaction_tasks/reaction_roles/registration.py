import nextcord

from nextcord.ext import commands


class RegisterRoles(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

        self.role_message_id = 969492407290847234
        self.emoji_to_role = {
            nextcord.PartialEmoji(name='🎎'): 969492005577183253,
             nextcord.PartialEmoji(name='🦊'): 969560877860794389,
            nextcord.PartialEmoji(name='🌑'): 969561374688673812,
            nextcord.PartialEmoji(name='🧝‍♂️'): 969562392927272980,
            nextcord.PartialEmoji(name='👷‍♂️'): 969561839333695509,
            nextcord.PartialEmoji(name='👨‍🌾'): 969562114983337995,
        }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        
        bot = self.bot
        
        if payload.message_id != self.role_message_id:
            return

        guild = bot.get_guild(738510840042356857)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        try:
            await payload.member.add_roles(role)
        except nextcord.HTTPException:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: nextcord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        
        bot = self.bot
        
        if payload.message_id != self.role_message_id:
            return

        guild = bot.get_guild(738510840042356857)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

        role = guild.get_role(role_id)
        if role is None:
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            return

        try:
            await member.remove_roles(role)
        except nextcord.HTTPException:
            pass


def setup(bot):
    bot.add_cog(RegisterRoles(bot))