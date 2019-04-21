import discord
from discord.ext import commands
from discord.utils import get

class Reaction:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        
        def searching(msg, text):
            for let in range(len(msg)):
                if msg[let]==text[0]:
                    add=False
                    for check in range(len(text)):
                        try:
                            if msg[let+check]==text[check]:
                                add=True
                            else:
                                add=False
                                break
                        except IndexError:
                            break
            if add:
                emotes.append(triggers[text])

        channel = message.channel
        author = message.author
        lowercase = message.content.lower()
        triggers={'ps1hagrid':'PS1Hagrid', 'gay':'KappaPride', 'tedder':'DansGame', 'hp4':'DansGame', 'raman':'RamanEyes', 'cat':'CatFace', 'kurwa':["\U0001F1F0","\U0001F1FA","\U0001F1F7","\U0001F1FC","\U0001F1E6"], "lul":"LUL", "5rt":"5rt"}
        letter_trig=[]
        for trigger in triggers:
            letter_trig.append(trigger[0])
        emotes=[]

        if message.author!='Bot_Dumbledore&#352530':
            for letter in lowercase:
                for search in len(letter_trig):
                    if letter_trig[search]==letter:
                          searching(lowercase, list(triggers)[search])

        for react in emotes:
            if type(react)==str and message.author != 'Bot_Dumbledore&#352530':
                await self.client.add_reaction(message, get(self.client.get_all_emojis(), name=react))
            elif type(react)==list:
                for ele in react:
                     await self.client.add_reaction(message, get(self.client.get_all_emojis(), name=ele))       


def setup(client):
    client.add_cog(Reaction(client))
