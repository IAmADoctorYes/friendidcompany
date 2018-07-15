##FriendsBot for the WVU Camp Discord server.
##Contributors:
## - Connor Herfurth (Programming)
## - Cameron (Ideas)
##Usage is granted to anybody on the WVU Camp Discord server.

version = "v.1.17"

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix = "|")

@bot.event
async def on_ready(): ##Sees when the bot is ready
    print("FriendsBot, version " + version + " is now ready on all servers.")

@bot.command(pass_context = True) ##Test command that I don't have the heart to remove because I already released it to the discord.
async def ding(ctx):
    await bot.say("dong")
    print("Command Ding Ran Successfully.") 

@bot.command(pass_context = True)
async def friendid(ctx, test): ##Gives data depending on FriendID.  Uses ID as 'test' because i forgot to fix it and I'm lazy.
    if test=="1":
        await bot.say("```Friend 1 \n Name: Cameron \n Date Added: 7/14/2018 \n Age: 15 \n Rank: E L I T E N U M B E R```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="2":
        await bot.say("```Friend 2 \n Name: Connor \n Date Added: 7/15/2018 \n Age: 15 \n SteamID: Netherman555 \n Rank: E L I T E N U M B E R```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="3":
        await bot.say("```Friend 3 \n Name: Landon \n Date Added: 7/15/2018 \n Age: [Unknown] \n Rank: Top5```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="4":
        await bot.say("```Friend 4 \n Name: Hayden \n Date Added: 7/15/2018 \n Age: [Unknown] \n Rank: Top5```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="5":
        await bot.say("```Friend 5 \n Name: Zach \n Date Added: 7/15/2018 \n Age: 15 \n Rank: Top5```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="6":
        await bot.say("```Friend 6 \n Name: Jack \n Date Added: 7/15/2018 \n Age: [UNKNOWN] \n  Rank: Top10```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="7":
        await bot.say("```Friend 7 \n Name: Slava \n Date Added: 7/15/2018 \n Age: 16 \n Rank: BANOS```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="8":
        await bot.say("```Friend 8 \n Name: Nicole \n Date Added: 7/15/2018 \n Age: 15 \n Rank: Top10```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="9":
        await bot.say("```Friend 9 \n Name: Jacob \n Date Added: 7/15/2018 \n Age: [UNKNOWN] \n Rank: Memelord```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="10":
        await bot.say("```Friend 10 \n Name: [UNKOWN] \n Date Added: 7/15/2018 \n Age: [UNKNOWN] \n Rank: Top10```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="11":
        await bot.say("```Friend 11 \n Name: Robert \n Date Added: 7/15/2018 \n Age: [UNKNOWN] \n Rank: Autism```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="12":
        await bot.say("```Friend 12 \n Name: Riggy \n Date Added: 7/15/2018 \n Age: [UNKOWN] \n Rank: Top15```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="13":
        await bot.say("```Friend 13 \n Name: Sully \n Date Added: 7/15/2018 \n Age: 16 \n SteamID: Long Boi <3 \n Rank: EdgeLord```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="14":
        await bot.say("```Friend 14 \n Name: Will \n Date Added: 7/15/2018 \n Age: [UNKOWN] \n Rank: Top15```")
        print("Command FriendID " + test + " ran successfully.")
    elif test=="15":
        await bot.say("```Friend 15 \n Name: Natalija \n Date Added: 7/15/2018 \n Age: [UNKNOWN] \n Rank: Newbie```")
        print("Command FriendID " + test + " ran successfully.")
    else:
        await bot.say("That's not a valid FriendID.  If you're Friend 13 and are doing this specifically to screw with us, fuck you!")
        print("Command Invalid FriendID ran successfully.")

@bot.command(pass_context = True)
async def getversion(ctx):
    await bot.say(version)

bot.run("NDY3ODQyNDc1NjQ2Nzc5Mzk0.DiwhQg.HIPFCNROgiRjQyNN9kAC0_W5T14") ##Runs bot (obviously).  Argument may need to change in case the token changes.
    
