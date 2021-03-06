import discord
from discord.ext import commands
import srcomapi, srcomapi.datatypes as dt
import json

with open('srdc.json', 'r') as f:
    speedgames = json.load(f)

games = list(speedgames.keys())
api = srcomapi.SpeedrunCom(); api.debug = 1

class Srdc:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def wr(self, ctx, game:str, category:str):
        if game in games:
            category_list = api.get_game(speedgames.get(game)).categories
            for cat in category_list:
                print(cat.name)
        else:
            return


def setup(client):
    client.add_cog(Srdc(client))