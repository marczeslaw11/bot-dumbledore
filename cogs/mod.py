#This is the cog file for the bot's modding related functionality
import discord
from discord.ext import commands

class Mod:
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Mod(client))