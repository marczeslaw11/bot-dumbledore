import discord
from discord.ext import commands
import requests
import json
import random

lyrics_root = "https://api.musixmatch.com/ws/1.1/"
lyrics_api = "1f4f14fb6b297b2a1aa077c24179856d"

cat_root = "https://cat-fact.herokuapp.com/facts"

cat_response = requests.get(cat_root).json()
cat_fact_list = cat_response["all"]

class Fun_api:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def lyrics(self, ctx, track, artist):
        url = lyrics_root + "track.search?q_track=" + track + "&q_artist=" + artist +"&apikey=" + lyrics_api
        response = requests.get(url).json()
        print(url)
        has_lyrics = response["message"]["body"]["track_list"][0]["track"]["has_lyrics"]
        if has_lyrics == 1:
            track_id = response["message"]["body"]["track_list"][0]["track"]["track_id"]
            lyrics_url = lyrics_root + "track.lyrics.get?track_id=" + str(track_id) + "&apikey=" + lyrics_api
            lyrics_resp = requests.get(lyrics_url).json()
            lyrics_body = lyrics_resp["message"]["body"]["lyrics"]["lyrics_body"]
            await self.client.say(lyrics_body)
        else:
            await self.client.say("No lyrics found, sorry! :(")

    @commands.command(pass_context=True)
    async def catfact(self):
        random_fact = random.choice(cat_fact_list)
        await self.client.say(random_fact["text"])

    @commands.command(pass_context=True)
    async def country(self, ctx, country):
        if len(country) < 4:
            base = "https://restcountries.eu/rest/v2/alpha/"
            search_by_name = False
        elif len(country) >= 4:
            search_by_name = True
            base = "https://restcountries.eu/rest/v2/name/"
        country_url = base + country
        country_data = requests.get(country_url).json()
        if search_by_name == True:
            country_data = country_data[0]
        name = country_data["name"]
        flag_url_base = "https://www.countryflags.io/"
        flag = flag_url_base + country_data["alpha2Code"] + "/shiny/64.png"
        print(flag)
        japanese = country_data["translations"]["ja"]
        population = "%i people" % (country_data["population"])
        area = "%i km2" % (country_data["area"])
        if len(country_data["borders"]) > 1:
            borders = ", ".join(country_data["borders"])
        elif len(country_data["borders"]) == 0:
            borders = "No bordering countries."
        else:
            borders = country_data["borders"][0]
        if len(country_data["timezones"]) > 1:
            timezones = ', '.join(country_data["timezones"])
        else:
            timezones = country_data["timezones"][0]

        embed=discord.Embed(title=name, color=0x6b93ed)
        embed.set_thumbnail(url=flag)
        embed.add_field(name="Population:", value=population, inline=True)
        embed.add_field(name="Area:", value=area, inline=True)
        embed.add_field(name="Timezones:", value=timezones, inline=True)
        embed.add_field(name="Japanese name:", value=japanese, inline=True)
        embed.add_field(name="Bordering countries:", value=borders, inline=True)
        await self.client.say(embed=embed)



def setup(client):
    client.add_cog(Fun_api(client))