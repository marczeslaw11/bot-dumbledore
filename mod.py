import discord
from discord.ext import commands

class Mod:
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Mod(client))