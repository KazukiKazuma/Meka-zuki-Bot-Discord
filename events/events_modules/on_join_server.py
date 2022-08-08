from nextcord.ext import commands
from config.server import new_server_member_standard_roles

class GiveRoleOnJoin(commands.Cog):
    '''Will give roles from the config file >new_server_member_standard_roles< to newly joined members of the server'''
    
    def __init__ (self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        for role in new_server_member_standard_roles.roles_ids:
            get_role = ctx.guild.get_role(role)
            await ctx.add_roles(get_role)
        

def setup(bot):
    bot.add_cog(GiveRoleOnJoin(bot))