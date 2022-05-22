import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from random import choice


load_dotenv(dotenv_path=".env")


intents = discord.Intents.default()
intents.members = True
chocolatine = commands.Bot(command_prefix=">", intents=intents)


@chocolatine.event
async def on_ready():
    print("Bot {0.user.display_name} is logged in.".format(chocolatine))


@chocolatine.command(pass_context=True)
async def breakfast(ctx):
  members = get_all_guild_members_mentions(ctx.guild)
  print(members)
  await ctx.send("This week, **{}** and **{}** will bring us a nice breakfast!\n_PLEASE screenshot this message_".format(choice(members), choice(members)))


def get_all_guild_members_mentions(guild):
  members_mentions = []
  for member in guild.members:
    # Add any member's ID that is not the bot ...
    if member.id != chocolatine.user.id and does_member_has_breakfast_role(member):
      members_mentions.append(member.mention)
  return members_mentions


def does_member_has_breakfast_role(member):
  for role in member.roles:
    if role.name == "Breakfast":
      return True
  return False

chocolatine.run(os.getenv("TOKEN"))
