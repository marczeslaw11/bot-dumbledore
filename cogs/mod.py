import discord
from discord.ext import commands

class Mod:
    def __init__(self, client):
        self.client = client

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