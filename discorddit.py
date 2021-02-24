import os, sys, random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.utils import get
import shutil
import requests
import urllib.request as req
import json
import praw
import asyncio
from settings import *

# BOT_PREFIX = '.'
# bot = commands.Bot(command_prefix = BOT_PREFIX)
# bot.remove_command('help')

TOKEN = getToken()
redditTrigger = 'https://www.reddit.com/r'

# LOG IN
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('reddit'))
	print(f'{bot.user} is online!')

mfgifs = ['https://tenor.com/tLAs.gif','https://tenor.com/QQTr.gif',
		'https://tenor.com/7AI6.gif','https://tenor.com/oX7z.gif',
		'https://tenor.com/bckT6.gif','https://tenor.com/4zAO.gif',
		'https://tenor.com/wlWG.gif','https://tenor.com/view/middle-finger-fuck-you-when-isee-my-ex-gif-4882889']

@bot.event
async def on_message(message):
	if redditTrigger in message.content:
		submissionUrl = message.content
		await message.delete()
		await betterEmbed(message, submissionUrl)
	# if 'help' in message.content:
	# 	randmfnum = random.randint(0,7)
	# 	await message.channel.send(str(mfgifs[randmfnum]))


@bot.command(pass_context=True, aliases=['dm'])
async def dank(ctx):
	await dank(ctx)


if __name__ == '__main__':
	bot.run(TOKEN)