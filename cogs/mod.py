import discord
from discord.ext import commands

class Mod:
    def __init__(self, client):
        self.client = client

    @commands.has_role("🛡️Prefect")
    @commands.command(pass_context=True)
    async def timeout(self, ctx, user: discord.Member):
        server = ctx.message.author.server
        role = discord.utils.get(user.server.roles, name='Timeout')
        name = user.name
        if role not in user.roles:
            await self.client.add_roles(user, role)
            await self.client.say("%s has been muted." % (name))
        else:
            await self.client.say("This person is already muted.")

    @commands.has_role("🛡️Prefect")
    @commands.command(pass_context=True)
    async def untimeout(self, ctx, user: discord.Member):
        server = ctx.message.author.server
        role = discord.utils.get(user.server.roles, name='Timeout')
        name = user.name
        if role in user.roles:
            await self.client.remove_roles(user, role)
            await self.client.say("The timeout of %s has been removed." % (name))
        else:
            await self.client.say("This person is not currently muted.")




'''user: discord.Member = None'''
'''@client.command(pass_context=True)
@commands.has_role("🛡️Prefect")
async def clear(ctx, *args):
    author = ctx.message.author
    channel = ctx.message.channel
    messages = []


    if args[0].isdigit() == True:
        amount = args[0]
        users = args[1:]
        print('true')
    else:
        amount = 1
        users = args
        print('else')

    async for message in client.logs_from(channel, limit=int(amount) + 1):
        for user in users:
            user_id = re.sub(r'\D', "", user)
            if user_id == message.author.id:
                messages.append(message)
    await client.delete_messages(messages)'''

def setup(client):
    client.add_cog(Mod(client))