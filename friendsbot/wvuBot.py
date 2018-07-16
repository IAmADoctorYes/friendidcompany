##FriendsBot for the WVU Camp Discord server.
##Contributors:
## - Connor Herfurth (Programming)
## - Sullivan Steele (Also Programming but better OWO, jk luv ya bud)
## - Cameron (Ideas)
##Usage is granted to anybody on the WVU Camp Discord server.

version = "v.1.22"

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix = "|")
friends = [{'name':'Cameron','Age':'15','Rank':'','SteamID':''},{'name':'Connor','Age':'15','Rank':'','SteamID':''},
            {'name':'Landon','Age':'14','Rank':'','SteamID':''},{'name':'Hayden','Age':'14','Rank':'','SteamID':''},
            {'name':'Zach','Age':'15','Rank':'','SteamID':''},{'name':'Jack','Age':'14','Rank':'','SteamID':''},
            {'name':'Slava','Age':'16','Rank':'','SteamID':''},{'name':'Nicole','Age':'15','Rank':'','SteamID':''},
            {'name':'Jacob','Age':'15','Rank':'','SteamID':''},{'name':'Na','Age':'Na','Rank':'','SteamID':''},
            {'name':'Robert','Age':'14','Rank':'','SteamID':''},{'name':'Riggi','Age':'16','Rank':'','SteamID':''},
            {'name':'Sully','Age':'16','Rank':'','SteamID':''},{'name':'Will','Age':'16','Rank':'','SteamID':''}
            ,{'name':'Natalija','Age':'17','Rank':'','SteamID':''}]

@bot.event
async def on_ready(): ##Sees when the bot is ready
    print("FriendsBot, version " + version + " is now ready on all servers.")

@bot.command(pass_context = True)
async def friendid(ctx, id): ##Gives data depending on FriendID.
    try:
        await bot.say("```Friend {} \n Name: {} \n Age: {} \n Rank: {} \n SteamID: {}```".format(id,friends[int(id)-1]['name'],friends[int(id)-1]['Age'],friends[int(id)-1]['Rank'],friends[int(id)-1]['SteamID']))
    except:
        print("Hey that's not a valid ID buddy Owo you wanna die?")

@bot.command(pass_context = True)
async def getversion(ctx):
    await bot.say(version)

@bot.command(pass_context = True)
async def roll(ctx, num, die):
    iterator = 1
    while iterator <= int(num):
         await bot.say(str(random.randint(1, int(die))))
         iterator = iterator + 1

@bot.command(pass_context = True)
async def b(msg):
    str=''
    arr = msg.split()
    for word in arr:
        for letter in word:
            if letter == ' ':
                str+=letter
            else:
                str += ':regional_indicator_{}: '.format(letter.lower())
    Bify(str[2::])

bot.run("NDY3ODQyNDc1NjQ2Nzc5Mzk0.DiwhQg.HIPFCNROgiRjQyNN9kAC0_W5T14") ##Runs bot (obviously).  Argument may need to change in case the token changes.
