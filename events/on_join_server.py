from nextcord.ext import commands

class OnJoinedMember(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        role_join = ctx.guild.get_role(967849474405838848)
        role_join_separator_1 = ctx.guild.get_role(967693392433807420)
        role_join_separator_2 = ctx.guild.get_role(967677263430713344)
        role_join_separator_3 = ctx.guild.get_role(928409990589448212)
        await ctx.add_roles(role_join, role_join_separator_1, role_join_separator_2, role_join_separator_3)
        

def setup(bot):
    bot.add_cog(OnJoinedMember(bot))