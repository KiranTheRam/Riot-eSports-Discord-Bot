import json

import requests


# This will build a dictionary based on the URL given and JSON returned
def build_dict(url):
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 13tgKXTDBY-RKazKMm3RArrw-K5BDYOAwxBfTtC_yFgejoHieKU"
    }
    response = requests.get(url, headers=headers)
    working_dict = json.loads(response.text)
    return working_dict


# This will create the API URL for running tournaments based on a search parameter if there is one
def val_tournament_url_builder(search_param):
    if search_param:
        url = "https://api.pandascore.co/valorant/tournaments/running?search[slug]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/valorant/tournaments/running?sort=&page=1&per_page=50"
    return url


# This will create the API URL for getting team information. Can have a search parameter
# TODO: Add search parameter functionality
def val_team_url_builder(search_param):
    if search_param:
        url = "https://api.pandascore.co/valorant/teams?search[name]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/valorant/teams?sort=&page=1&per_page=50"
    return url

# This will create the API URL for getting team information. Can have a search parameter
# TODO: Add search parameter functionality
def val_player_url_builder(search_param):
    if search_param:
        url = "https://api.pandascore.co/valorant/players?search[name]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/valorant/players?sort=&page=1&per_page=50"
    return url


# Displays all the players. Can search for a specific player.
# TODO: Replace name and functionality for clarity. This function can get all information abut a tournament, not just teams in a tournament
def get_valorant_player():
    search_param = input("Enter a player to search for.\nLeave blank to see all players:  ")
    url = val_player_url_builder(search_param)
    val_players_dict = build_dict(url)

    for player in val_players_dict:
        print("     ", player['name'], ": ", player['first_name'], player['last_name'], "| Team: ", player['current_team']['name'], "| Age: ", player['age'],
              "| Hometown: ", player['hometown'], "| Nationality : ", player['nationality'])


# Displays all the teams participating in tournaments. Can search for a specific tournament.
# TODO: Replace name and functionality for clarity. This function can get all information abut a tournament, not just teams in a tournament
def get_team_for_tournament():
    search_param = input("Enter a tournament to search for.\nLeave blank to see all currently running tournaments:  ")
    url = val_tournament_url_builder(search_param)
    val_tournaments_dict = build_dict(url)

    for tournament in val_tournaments_dict:
        # TODO: Replace this print with something for the bot
        print("\n\nTournament: ", tournament['slug'], tournament['league']['image_url'], "\nParticipating Teams: ")

        for team in tournament['teams']:
            # TODO: Replace this print with something for the bot
            print("     ", team['name'], ": ", team['image_url'])



# Displays all information about teams
def get_team():
    search_param = input("Enter a team to search for.\nLeave blank to see all currently active teams:  ")
    url = val_team_url_builder(search_param)
    val_teams_dict = build_dict(url)

    for team in val_teams_dict:
        # TODO: Replace this print with something for the bot
        if team['acronym'] == None:
            print("\n\nTeam: ", team['name'], "| Image: ", team['image_url'],
                  "\nBased out of: ", team['location'])
        else:
            print("\n\nTeam: ", team['name'], "(", team['acronym'], ")", "Image: ", team['image_url'], "\nBased out of: ", team['location'])


        for player in team['players']:
            # TODO: Replace this print with something for the bot
            print("     ", player['name'], ": ", player['first_name'], player['last_name'], "| Age: ", player['age'], "| Hometown: ", player['hometown'], "| Nationality : ", player['nationality'])


if __name__ == '__main__':
    # Testing getting tournament info
    while 0 != 1:
        # get_team_for_tournament()
        get_valorant_player()
#     Testing API for players
#     get_team()

# Testing
# print("League Name: ", ValTournamentsDict[0]['league']['name'])
# print("Full Name Tournament Name: ",ValTournamentsDict[0]['slug'])
# print("Section of the Series: ",ValTournamentsDict[0]['name'])
