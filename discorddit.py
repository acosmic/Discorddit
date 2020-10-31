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
import settings

BOT_PREFIX = '.'
bot = commands.Bot(command_prefix = BOT_PREFIX)
bot.remove_command('help')

TOKEN = settings.getToken()
redditTrigger = 'https://www.reddit.com/r'

# LOG IN
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
	print(f'{bot.user} is online!')

@bot.event
async def on_message(message):
	if redditTrigger in message.content:
		submissionUrl = message.content
		await message.delete()
		await settings.betterEmbed(message, submissionUrl)



@bot.command(pass_context=True, aliases=['dm'])
async def dank(ctx):
	await settings.dank(ctx)



bot.run(TOKEN)