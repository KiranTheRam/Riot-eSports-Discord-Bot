# import requests
import json
from urllib.request import urlopen, Request


def playerSearch(playerName):
    if [x for x in data['players'] if x.get('gameName') == playerName]:
        print("Found")
    else:
        print("Not Found")


baseURL = "https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/[ACTID]?size=200&startIndex=0&api_key=[APIKEY]"
currentActID = "a16955a5-4ad0-f761-5e9e-389df1c892fb"
APIKey = "YOUR KEY HERE"
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
nameOrRank = input("Do you want to search by 'player name' or 'rank': ")
nameOrRank = nameOrRank.lower()

if nameOrRank == ("player name" or "playername"):
    playerName = input("Enter a player name: ")
    playerSearch(playerName)
elif nameOrRank == "rank":
    rank = input("Enter a player rank")
else:
    print("Input did not match either option")

# print(any(sd['gameName']=='100T Asuna' for sd in data['players']))
