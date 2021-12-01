# import requests
import json
from urllib.request import urlopen, Request

# These 2 were only ever pulling Asuna's info
# def playerSearch(playerName):
#     if [x for x in data['players'] if x.get('gameName') == playerName]:
#         print("Found", playerName)
#         print("-------\n", data['players']['gameName'], "\n-------")
#         player = data['players']['gameName' == playerName]
#         print("Ranking: ", player['leaderboardRank'])
#         print("Rating: ", player['rankedRating'])
#         print("Number of wins: ", player['numberOfWins'])
#         print("Competitive Tier: ", player['competitiveTier'])
#     else:
#         print("Not Found")
#
# def rankSearch(rank):
#     if [x for x in data['players'] if x.get('leaderboardRank') == rank]:
#         print("Found")
#         player = data['players']['leaderboardRank' == rank]
#         print("Ranking: ", player['leaderboardRank'])
#         print("Rating: ", player['rankedRating'])
#         print("Number of wins: ", player['numberOfWins'])
#         print("Competitive Tier: ", player['competitiveTier'])
#     else:
#         print("Not Found")

def playerSearch(playerName):
    for x in data['players']:
        if x.get('gameName') == playerName:
            print("Found", x.get('gameName'))
            print("Ranking: ", x.get('leaderboardRank'))
            print("Type for rank object: ", type(x.get('leaderboardRank')))
            print("Rating: ", x.get('rankedRating'))
            print("Number of wins: ", x.get('numberOfWins'))
            print("Competitive Tier: ", x.get('competitiveTier'))
            break

def rankSearch(rank):
    for x in data['players']:
        if x.get('leaderboardRank') == rank:
            print("Found rank #", x.get('leaderboardRank'))
            print("Name: ", x.get('gameName'))
            print("Rating: ", x.get('rankedRating'))
            print("Number of wins: ", x.get('numberOfWins'))
            print("Competitive Tier: ", x.get('competitiveTier'))
            break




baseURL = "https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/[ACTID]?size=200&startIndex=0&api_key=[APIKEY]"
currentActID = "a16955a5-4ad0-f761-5e9e-389df1c892fb"
APIKey = "RGAPI-7d0c3d5f-452f-4f63-859d-b56e5bc7e927"
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

# print(data)
# print("\n\n", data['players'][0])

# Based on command used in discord $p, $r, etc... a specific variable will be made to search against

# TESTING - Creating a sub-dict for an individual player
# player = data['players']['gameName' == "100T Asuna"]
# print(player)
# print(type(player))
# print(player['leaderboardRank'])

# WORKING
while True:
    option = input("Do you want to search by 'player name' or 'rank', or 'exit: ")
    option = option.lower()

    if option == "player name" or option == "playername":
        playerName = input("Enter a player name: ")
        # playerSearch(playerName)
        playerSearch(playerName)
    elif option == "rank":
        rank = input("Enter a player rank: ")
        rankSearch(rank)
    elif option == "exit":
        exit(1)
    else:
        print("Input did not match either option")

# Not Used
# print(any(sd['gameName']=='100T Asuna' for sd in data['players']))
