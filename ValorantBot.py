import json
from urllib.request import urlopen, Request
import discord

# Functions
def playerSearch(passedPlayerName):
    for x in data['players']:
        if x.get('gameName') == passedPlayerName:
            print("Found", x.get('gameName'))
            print("Ranking: ", x.get('leaderboardRank'))
            print("Rating: ", x.get('rankedRating'))
            print("Number of wins: ", x.get('numberOfWins'))
            print("Competitive Tier: ", x.get('competitiveTier'))
            break


def rankSearch(passedRank):
    for x in data['players']:
        if x.get('leaderboardRank') == passedRank:
            print("Found rank #", x.get('leaderboardRank'))
            print("Name: ", x.get('gameName'))
            print("Rating: ", x.get('rankedRating'))
            print("Number of wins: ", x.get('numberOfWins'))
            print("Competitive Tier: ", x.get('competitiveTier'))
            break

# API Handling
baseURL = "https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/[ACTID]?size=200&startIndex=0&api_key=[APIKEY]"
currentActID = "a16955a5-4ad0-f761-5e9e-389df1c892fb"
APIKey = "RGAPI-b6568c06-c7df-4944-b1ff-1ad43e76a172"
URL = baseURL.replace("[ACTID]", currentActID)
URL = URL.replace("[APIKEY]", APIKey)

headers = {
    'Content-Type': 'application/json',
}
try:
    request = Request(URL, headers=headers)
    response_body = urlopen(request).read()
except:
    print("Error processing API request")

try:
    data = json.loads(response_body)
except:
    print("Error encountered")


# Discord Handling
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('HELLO WORLD')
    if message.content.startswith('$player'):
        await message.channel.send(playerSearch('100T Asuna'))

TOKEN = 'OTE1NzQzMTkxOTYwMDI3MTk2.YagCTg.bxv6slXEkiJUQZ-kATGUWmDe5fQ'
client.run(TOKEN)

# Based on command used in discord $p, $r, etc... a specific variable will be made to search against
# Using the code in console
# while True:
#     option = input("\nDo you want to search by 'player name' or 'rank', or 'exit: ")
#     option = option.lower()
#
#     if option == "player name" or option == "playername":
#         playerName = input("Enter a player name: ")
#         playerSearch(playerName)
#     elif option == "rank":
#         rank = input("Enter a player rank: ")
#         rankSearch(int(rank))
#     elif option == "exit":
#         exit(1)
#     else:
#         print("Input did not match either option")
