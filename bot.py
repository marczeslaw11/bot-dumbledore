#main bot file
import configparser
import discord
import re
import random
from discord.utils import get
from discord.ext import commands
import asyncio
from itertools import cycle
import json
import time

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

TOKEN = config['LOGIN']['token']

client = commands.Bot(command_prefix = '/')
client.remove_command('help')
extensions = ['meta', 'hp_api', 'housecup', 'reaction', 'srdc']

status = ['with your minds', 'with your hearts', 'with your bodies', 'with your nerves']
hp_mod_commands = ['give', 'add', 'set', 'subtract', 'remove']
dumbledore_positive = ['Yes, you are the headmaster! Nice beard.', 'Yep. You are Dumbledore. A mirror would be much simpler though. I don\'t recommend the Mirror of Erised.', 'Yes, you are the headmaster but be careful, with great power come great memes.', 'Yeah, you are the headmaster, now let\'s go and give some random points.']
dumbledore_negative = ['No, *I* am Dumbledore.', 'You might be Spartacus, but you are not Dumbledore.', 'Stop checking this, you fool.', 'You might be Jude Law but that doesn\'t mean that you are Dumbledore.', 'Nah, you are not Dumbledore. Git gud.']

def point_mng(house, command, amount):
    if amount < 0:
        return "Don't play with negatives, boy!"
    with open('points.json', 'r') as f:
        points = json.load(f)
        if command in hp_mod_commands:
            if command == "give" or command == "add":
                points[house] += amount
                message = "%s has recieved %d point(s). They have %d point(s) now." % (house, amount, points[house])

            if command == "remove" or command == "subtract":
                points[house] -= amount
                message = "%s has %d point(s) less now. They have %d point(s) now." % (house, amount, points[house])
            if command == "set":
                points[house] = amount
                message = "%s has %d point(s) now." % (house, points[house])
        else:
            return "That's not how this works."
        with open('points.json', 'w') as outfile:
            json.dump(points, outfile)
        return message

def point_log(house, command, amount, reason, point_giver):
    reason_string = " ".join(reason)
    date = time.asctime( time.localtime(time.time()) )
    with open("point_log.txt", "a") as myfile:
        myfile.write("House: %s | action: %s | %d points | Given by: %s | Reason: %s | %s \n" % (house, command, amount, point_giver, reason_string, date))

def find_winner_color(points):
    winner = max(zip(points.values(), points.keys()))
    if winner[1] == "Slytherin":
        return 0x00c400
    elif winner[1] == "Gryffindor":
        return 0xae0001
    elif winner[1] == "Ravenclaw":
        return 0x222f5b
    elif winner[1] == "Hufflepuff":
        return 0xecb939

@client.event
async def on_ready():
    print('The bot is ready to serve!')
    await client.change_presence(game=discord.Game(name='with your nerves'))

@client.command()
@commands.has_role("dumbledore")
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
@commands.has_role("dumbledore")
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

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

@client.command()
async def points(year=None):
    if year is None:
        with open('points.json', 'r') as f:
            points = json.load(f)
    elif year == '2018':
        with open('points2018.json', 'r') as f:
            points = json.load(f)

    winner_color = find_winner_color(points)
    embed=discord.Embed(description="Current Standing of The House Cup", color=winner_color)
    embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/model-hogwarts/images/d/dc/House_Cup.png/revision/latest?cb=20171021204608")
    embed.add_field(name="Gryffindor", value=points["Gryffindor"], inline=True)
    embed.add_field(name="Slytherin", value=points["Slytherin"], inline=True)
    embed.add_field(name="Hufflepuff", value=points["Hufflepuff"], inline=True)
    embed.add_field(name="Ravenclaw", value=points["Ravenclaw"], inline=True)

    await client.say(embed=embed)
    #await client.say("Gryffindor: %d points\nRavenclaw: %d points\nSlytherin: %d points\nHufflepuff: %d points" % (, , points["slytherin"], points["hufflepuff"]))

@client.command(name="gryffindor", pass_context=True, aliases=['g'])
@commands.has_role("dumbledore")
async def gryffindor(ctx, command: str, amount: int, *reason):
    point_log("Gryffindor", command, amount, reason, ctx.message.author.name)
    await client.say(point_mng("Gryffindor", command, amount))

@client.command(name="slytherin", pass_context=True, aliases=['s'])
@commands.has_role("dumbledore")
async def gryffindor(ctx, command: str, amount: int, *reason):
    point_log("Slytherin", command, amount, reason, ctx.message.author.name)
    await client.say(point_mng("Slytherin", command, amount))

@client.command(name="hufflepuff", pass_context=True, aliases=['h'])
@commands.has_role("dumbledore")
async def gryffindor(ctx, command: str, amount: int, *reason):
    point_log("Hufflepuff", command, amount, reason, ctx.message.author.name)
    await client.say(point_mng("Hufflepuff", command, amount))

@client.command(name="ravenclaw", pass_context=True, aliases=['r'])
@commands.has_role("dumbledore")
async def gryffindor(ctx, command: str, amount: int, *reason):
    point_log("Ravenclaw", command, amount, reason, ctx.message.author.name)
    await client.say(point_mng("Ravenclaw", command, amount))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    generic=discord.Embed(color=0x6464db)
    generic.set_author(name="Generic server commands")
    generic.add_field(name='/ping', value='Ping the bot to see if it\'s alive.', inline=False)
    generic.add_field(name='/roles', value='List your roles on the server', inline=False)

    house=discord.Embed(color=0x6464db)
    house.set_author(name="House Cup Commands")
    house.add_field(name='/sortinghat', value='The Sorting Hat recommends a house for you if you can\'t make up your mind.', inline=False)
    house.add_field(name='/points', value='Check the standing of the House Cup.', inline=False)
    house.add_field(name='/dumbledore', value='Check whether you have the rights to manage points or not.', inline=False)

    house_mng=discord.Embed(color=0x6464db)
    house_mng.set_author(name="House Cup Management Commands (Dumbledore only!)")
    house_mng.add_field(name='/gryffindor or /g', value='Manage the points of Gryffindor. Usage: /g give|add|set|subtract|remove [points]', inline=False)
    house_mng.add_field(name='/slytherin or /s', value='Manage the points of Syltherin. Usage: /g give|add|set|subtract|remove [points]', inline=False)
    house_mng.add_field(name='/hufflepuff or /h', value='Manage the points of Hufflepuff. Usage: /g give|add|set|subtract|remove [points]', inline=False)
    house_mng.add_field(name='/ravenclaw or /r', value='Manage the points of Ravenclaw. Usage: /g give|add|set|subtract|remove [points]', inline=False)

    hp=discord.Embed(color=0x6464db)
    hp.set_author(name="Harry Potter related commands")
    hp.add_field(name='/spells', value='List all the available spells.', inline=False)
    hp.add_field(name='/spell [spell name]', value='Get information about a specific spell from the spell list.', inline=False)
    hp.add_field(name='/hpwikia [search term]', value='Search the Harry Potter wikia for a specific search term.', inline=False)
    hp.add_field(name='/quote', value='Get a great Dumbledore quote.', inline=False)

    await client.say("I've sent you a DM with some guidance, my friend!")
    await client.send_message(author, embed=generic)
    await client.send_message(author, embed=house)
    await client.send_message(author, embed=house_mng)
    await client.send_message(author, embed=hp)


client.run(TOKEN, bot=True, reconnect=True)