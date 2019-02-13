import discord
from discord.ext import commands
import re

class Meta:
    def __init__(self, client):
        self.client = client

    '''async def on_message_delete(self, message):
        await self.client.send_message(message.channel, 'Message deleted.')'''

    @commands.command()
    async def ping(self):
        await self.client.say('Pong!')

    @commands.command(pass_context=True)
    async def roles(self, ctx):
        roles = ctx.message.author.roles
        output = ''
        for role in roles:
            output += role.name
            output += ' (id: '
            output += role.id
            output += ')\n'
        output = re.sub('[@]', '', output)
        embed=discord.Embed(title="List of your roles:", description=output, color=0x6464db)
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Meta(client))