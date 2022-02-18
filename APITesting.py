import json
from urllib.request import urlopen, Request

# API Handling
baseURL = "https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/[ACTID]?size=200&startIndex=0&api_key=[APIKEY]"
currentActID = "573f53ac-41a5-3a7d-d9ce-d6a6298e5704"
APIKey = "RGAPI-e39e7fe1-1482-46c1-96c2-8988930487c9"
URL = baseURL.replace("[ACTID]", currentActID)
URL = URL.replace("[APIKEY]", APIKey)
print(URL)
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

# Functions
def playerSearch(passedPlayerName):
    for x in data['players']:
        if x.get('gameName') == passedPlayerName:
            return x
    print("Player not found")

def rankSearch(passedRank):
    for x in data['players']:
        if x.get('leaderboardRank') == passedRank:
            return x
    print("Player not found")

print(data)

while True:
    print("\n")
    passedPlayerName = input("Enter a player to search for:")
    print("You entered ", passedPlayerName, ", It is of type ", type(passedPlayerName))
    playerInfo = playerSearch(passedPlayerName)
    print(playerInfo)

    print("\n")
    passedPlayerRank = input("Enter a rank to search for:")
    print("You entered ", passedPlayerRank)
    playerInfo = rankSearch(int(passedPlayerRank))
    print(playerInfo)


