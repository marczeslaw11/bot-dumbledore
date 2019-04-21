import discord
from discord.ext import commands
from discord.utils import get

class Reaction:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        channel = message.channel
        author = message.author
        lowercase = message.content.lower()

        if ':PS1Hagrid:' in message.content and message.author != 'Bot_Dumbledore&#352530':
            hagrid = get(self.client.get_all_emojis(), name='PS1Hagrid')
            await self.client.add_reaction(message, hagrid)

        if 'gay' in lowercase and message.author != 'Bot_Dumbledore&#352530':
            kappa_pride = get(self.client.get_all_emojis(), name='KappaPride')
            await self.client.add_reaction(message, kappa_pride)

        if 'tedder' in lowercase and message.author != 'Bot_Dumbledore&#352530':
            dans_game = get(self.client.get_all_emojis(), name='DansGame')
            await self.client.add_reaction(message, dans_game)

        if 'hp4' in lowercase and message.author != 'Bot_Dumbledore&#352530':
            dans_game = get(self.client.get_all_emojis(), name='DansGame')
            await self.client.add_reaction(message, dans_game)

        if 'raman' in lowercase and message.author != 'Bot_Dumbledore&#352530':
            ramaneyes = get(self.client.get_all_emojis(), name='RamanEyes')
            await self.client.add_reaction(message, ramaneyes)

        if 'cat' in lowercase and message.author != 'Bot_Dumbledore&#352530':
            cat = get(self.client.get_all_emojis(), name='CatFace')
            await self.client.add_reaction(message, cat)

        if 'kurwa' in lowercase:
            letter_k = "\U0001F1F0"
            letter_u = "\U0001F1FA"
            letter_r = "\U0001F1F7"
            letter_w = "\U0001F1FC"
            letter_a = "\U0001F1E6"

            await self.client.add_reaction(message, letter_k)
            await self.client.add_reaction(message, letter_u)
            await self.client.add_reaction(message, letter_r)
            await self.client.add_reaction(message, letter_w)
            await self.client.add_reaction(message, letter_a)

        if ':LUL:' in message.content:
            lul = get(self.client.get_all_emojis(), name='LUL')
            await self.client.add_reaction(message, lul)

        if ':5rt:' in message.content:
            fivert = get(self.client.get_all_emojis(), name='5rt')
            await self.client.add_reaction(message, fivert)

def setup(client):
    client.add_cog(Reaction(client))