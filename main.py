# import requests
import json
from urllib.request import urlopen, Request


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


baseURL = "https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/[ACTID]?size=200&startIndex=0&api_key=[APIKEY]"
currentActID = "a16955a5-4ad0-f761-5e9e-389df1c892fb"
APIKey = "Enter your own key scrub"
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

# Based on command used in discord $p, $r, etc... a specific variable will be made to search against
# WORKING
while True:
    option = input("Do you want to search by 'player name' or 'rank', or 'exit: ")
    option = option.lower()

    if option == "player name" or option == "playername":
        playerName = input("Enter a player name: ")
        playerSearch(playerName)
    elif option == "rank":
        rank = input("Enter a player rank: ")
        rankSearch(int(rank))
    elif option == "exit":
        exit(1)
    else:
        print("Input did not match either option")
