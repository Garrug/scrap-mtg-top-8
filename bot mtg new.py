from functools import reduce
import discord
import requests
from discord import guild
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import*
from discord.flags import Intents
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument
from discord.errors import Forbidden
from bs4 import BeautifulSoup   


#Prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "-",help_command=None,intents=intents)



#STATUT
@bot.event
async def on_ready():
    print("Le bot est prêt.")
    await bot.change_presence(activity=discord.Streaming(name="Mtg bot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))




@bot.command()
async def deck(ctx,*,arg):

    commander=arg


    url="https://mtgtop8.com/format?f=EDH"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    compteur=0

    for link in soup.find_all("a"):
    #    inner_text="{}".format(link.text)


        if "{}".format(link.text)==commander:
            url="{}".format(link.get("href"))


    url="https://mtgtop8.com/"+url

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    compteur=0

    for link in soup.find_all("a"):

        if "{}".format(link.text)==commander:
                
            if compteur>=1:
                
                await ctx.send("https://mtgtop8.com/{}".format(link.get("href")))


            compteur=1+compteur

            if compteur==4:
                break


@bot.command()
async def tournoi(ctx):

    url="https://mtgtop8.com/format?f=EDH"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup.prettify())

    compteur=0

    for link in soup.find_all("a"):
    #    inner_text="{}".format(link.text)

        if "event" in "{}".format(link.get("href")):
            
            await ctx.reply("Le dernier gros tournoi :\nhttps://mtgtop8.com/{}".format(link.get("href")))
            break
  
        

bot.run("OTM1MjIzMDYzMzI1MzQzNzk1.Ye7gWQ.6QzaOT3SZGh3n2tUkVv5lxggVfw")