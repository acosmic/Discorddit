import os, sys, random
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.utils import get
import praw
import requests
import urllib.request as req

BOT_PREFIX = '.'
bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')


def getToken():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')  # Discorddit
    return TOKEN


def getReddit():
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.getenv('client_id_env'),
        client_secret=os.getenv('client_secret_env'),
        user_agent=os.getenv('user_agent_env'),
        username=os.getenv('username_env '),
        password=os.getenv('password_env'))
    return reddit


reddit = getReddit()


async def dank(ctx):
    sub = reddit.subreddit('dankmemes')
    hot = [post for post in sub.hot(limit=20)]
    random_post_number = random.randint(1, 19)
    random_post = hot[random_post_number]
    memetitle = random_post.title
    memeurl = random_post.url
    memeups = random_post.ups
    subicon = sub.icon_img
    body = random_post.selftext
    perma = "(https://www.reddit.com" + random_post.permalink + ")"
    permatitle = "[" + memetitle + "]" + perma
    perma_embed = "[See on Reddit](" + perma + ")"
    subid = random_post.id
    score = random_post.score
    author = random_post.author
    is_video = random_post.is_video
    over_18 = random_post.over_18
    shortlink = random_post.shortlink
    subreddit_type = random_post.subreddit_type
    subreddit_subscribers = random_post.subreddit_subscribers
    thumbnail = random_post.thumbnail
    if memeurl.find(".gifv") != -1 or memeurl.find("youtub") != -1 or memeurl.find("gfycat") != -1 or memeurl.find(
            "v.redd.it") != -1:
        dank_embed = discord.Embed(
            colour=discord.Colour(0x190125),
            # title= memetitle,
            # description=
        )
        dank_embed.set_author(name="r/" + str(sub), icon_url=subicon)
        # dank_embed.set_image(url=memeurl)
        dank_embed.set_footer(text=str(memeups) + ' Up Votes')
        # dank_embed.set_thumbnail(url=subicon)
        dank_embed.add_field(name='\u200b', value=permatitle)
        await ctx.send(embed=dank_embed)
        await ctx.send(memeurl)
    elif 'https://www.reddit.com/r/' in memeurl is True:
        dank_embed = discord.Embed(
            colour=discord.Colour(0x190125),
            title=memetitle,
            description=body
        )
        dank_embed.set_author(name="r/" + str(sub), icon_url=subicon)
        dank_embed.set_footer(text=str(memeups) + ' Up Votes')
        dank_embed.add_field(name='\u200b', value=permatitle)
        await ctx.send(embed=dank_embed)
    else:
        dank_embed = discord.Embed(
            colour=discord.Colour(0x190125),
            # title= memetitle,
            # description=
        )
        dank_embed.set_author(name="r/" + str(sub), icon_url=subicon)

        dank_embed.set_footer(text=str(memeups) + ' Up Votes')
        # dank_embed.set_thumbnail(url=subicon)
        dank_embed.set_image(url=memeurl)
        dank_embed.add_field(name='\u200b', value=permatitle)
        await ctx.send(embed=dank_embed)



async def betterEmbed(messsage, submissionUrl):
    emojis = ['👍','👎','😂',]
    post = reddit.submission(url=submissionUrl)
    subtext = submissionUrl.split('/')[-5]
    sub = reddit.subreddit(str(subtext))
    posttitle = post.title
    posturl = post.url
    upvotes = post.ups
    numComments = post.num_comments
    subicon = sub.icon_img
    body = (post.selftext[:2045] + '...') if len(post.selftext) > 2045 else post.selftext
    perma = "(https://www.reddit.com" + post.permalink + ")"
    permatitle = "[" + posttitle + "]" + perma
    perma_embed = "[See on Reddit](" + perma + ")"
    subid = post.id
    score = post.score
    author = post.author
    is_video = post.is_video
    over_18 = post.over_18
    shortlink = post.shortlink
    subreddit_type = post.subreddit_type
    subreddit_subscribers = post.subreddit_subscribers
    thumbnail = post.thumbnail
    if posturl.find(".gifv") != -1 or posturl.find("youtub") != -1 or posturl.find("gfycat") != -1 or posturl.find(
            "v.redd.it") != -1:
        dank_embed = discord.Embed(
            colour=discord.Colour(0x190125),
            title= posttitle,
            url=posturl,
            # description=
        )
        dank_embed.set_author(name= str(messsage.author), icon_url= messsage.author.avatar_url)
        dank_embed.set_image(url=thumbnail)
        dank_embed.set_footer(text=str(upvotes) + ' Up Votes and ' + str(numComments) + ' Comments')
        # dank_embed.set_thumbnail(url=thumbnail)
        msg = await messsage.channel.send(embed=dank_embed)
        # await messsage.channel.send(posturl)
        for i in emojis:
            await msg.add_reaction(i)
    else:
        dank_embed = discord.Embed(
            colour=discord.Colour(0x190125),
            title= posttitle,
            url= posturl,
            description= body
        )
        dank_embed.set_author(name= str(messsage.author), icon_url= messsage.author.avatar_url)
        dank_embed.set_footer(text="r/" + str(sub) +" - " +str(upvotes) + ' Up Votes and ' + str(numComments) + ' Comments', icon_url=subicon)
        # dank_embed.set_thumbnail(url=messsage.author.avatar_url)
        dank_embed.set_image(url=posturl)
        msg = await messsage.channel.send(embed=dank_embed)
        for i in emojis:
            await msg.add_reaction(i)

    
