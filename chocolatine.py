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
    print(f"Bot {chocolatine.user.display_name} is logged in.")


@chocolatine.command(
    pass_context=True
)  # pass_context is no longer necesary, context is always passed automatically
async def breakfast(ctx):
    members = get_all_guild_members_mentions(ctx.guild)
    print(members)
    await ctx.send(
        f"This week, **{choice(members)}** and **{choice(members)}** will bring us a nice breakfast!\n_PLEASE screenshot this message_"
    )


def get_all_guild_members_mentions(guild):
    return [
        member.mention
        for member in filter(does_member_has_breakfast_role, guild.members)
    ]


def does_member_has_breakfast_role(member):
    roles = [role.name for role in member.roles]
    return "Breakfast" in roles


chocolatine.run(os.getenv("TOKEN"))
