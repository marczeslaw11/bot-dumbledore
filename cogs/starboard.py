#Cog file for the upcoming starboard functionality

import discord
from discord.ext import commands

class Starboard:
    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(Starboard(client))