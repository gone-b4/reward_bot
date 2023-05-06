#!/usr/bin/env python3

import os
import discord
import argparse
from dotenv import load_dotenv
from discord.ext import commands
from SpinToWin import SpinToWin

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="?", description="Spin for a chance to win a reward", intents=intents)

@bot.event
async def on_ready():
    print(f"Reward bot has logged in as {bot.user}")

@bot.command()
async def spin(ctx):
    """Spin for a reward"""
    reward = spin2win.spin()
    msg = str()
    msg += "```"
    msg += f"Reward: {reward}"
    msg += "```"
    await ctx.send(msg)

@bot.command()
async def listRewards(ctx):
    """List available rewards and their weights"""
    rewards = spin2win.getRewards()
    max_len = max(len(reward) for reward in rewards.keys())

    msg = str()
    msg += "```"
    msg += "{:<{}}   {}\n".format("Reward", max_len, "Weight")
    msg += "{:<{}}   {}\n".format("=" * max_len, max_len, "=" * max_len)
    for reward, weight in rewards.items():
        msg += "{:<{}}   {}\n".format(reward, max_len, weight)
    msg += "```"

    await ctx.send(msg)

@bot.command()
async def updateReward(ctx, reward: str, weight: str):
    """Update a rewards weight"""
    return

def init()-> argparse.Namespace:
    import argparse
    parser = argparse.ArgumentParser(prog="main.py", description="")
    parser.add_argument("-r", "--rewards", required=True, help="CSV containing rewards. No header needed.")
    args = parser.parse_args()

    return args


args = init()
spin2win = SpinToWin()
spin2win.loadWheel(args.rewards)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if (not DISCORD_TOKEN):
    raise ValueError("Require discord token in '.env'. Please refer to https://discordpy.readthedocs.io/en/stable/index.html")


bot.run(DISCORD_TOKEN)