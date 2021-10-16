#!/usr/bin python3
import os
import time
import json
import random
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

default_prefix = '^'
async def determine_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return commands.when_mentioned_or(prefixes[str(message.guild.id)])(bot, message)

bot = commands.Bot(command_prefix=determine_prefix, intents=intents)

for file in os.listdir("./cogs"): # lists all the cog files inside the cog folder.
    if file.endswith(".py"): # It gets all the cogs that ends with a ".py".
        name = file[:-3] # It gets the name of the file removing the ".py"
        bot.load_extension(f"cogs.{name}") # This loads the cog.


@bot.event
async def on_ready():
    print(f'// bot logged in, but cooler\n\n')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = default_prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)




bot.run("ODI5MDQzNTk4ODU4MjU2NDE0.YGyZBA.Uh_LrA_Va5pcmW-46cMcBFKGxW0")