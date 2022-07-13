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


############################################################################################################
# These functions format urls for the api

# This will create the API URL for running tournaments based on a search parameter if there is one
def tournament_url_builder(game, search_param):
    if search_param:
        url = "https://api.pandascore.co/" + game + "/tournaments/running?search[slug]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/" + game + "/tournaments/running?sort=&page=1&per_page=50"
    return url


# This will create the API URL for getting team information. Can have a search parameter
# def team_url_builder(game, search_param):
#     if search_param:
#         url = "https://api.pandascore.co/" + game + "/teams?search[name]=" + search_param + "&sort=&page=1&per_page=50"
#         return url
#     url = "https://api.pandascore.co/" + game + "/teams?sort=&page=1&per_page=50"
#     return url


# This will create the API URL for getting player information. Can have a search parameter
# def player_url_builder(game, search_param):
#     if search_param:
#         url = "https://api.pandascore.co/" + game + "/players?search[name]=" + search_param + "&sort=&page=1&per_page=50"
#         return url
#     url = "https://api.pandascore.co/" + game + "/players?sort=&page=1&per_page=50"
#     return url


# This will be the universal API URL builder.
def url_builder(game, context, search_param):
    if search_param:
        url = "https://api.pandascore.co/" + game + "/" + context + "?search[name]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/" + game + "/players?sort=&page=1&per_page=50"
    return url


###########################################################################################################
# These functions format and print out the info from dictionaries


# Displays all the players. Can search for a specific player.
def get_player_info():
    game = input("Enter the game to search for: ")
    context = 'players'
    search_param = input("Enter a player to search for.\nLeave blank to see all players:  ")
    # url = player_url_builder(game, search_param)
    url = url_builder(game, context, search_param)
    players_dict = build_dict(url)

    for player in players_dict:
        print("\n", player['name'], ": ", player['first_name'], player['last_name'])
        if player['current_team'] is not None:
            print("| Team: " + player['current_team']['name'])
        if player['hometown'] is not None:
            print("| Hometown: ", player['hometown'])
        if player['nationality'] is not None:
            print("| Nationality : ", player['nationality'])
        if player['image_url'] is not None:
            print("| Image : ", player['image_url'])


# Displays all the teams participating in tournaments. Can search for a specific tournament.
# TODO: Replace name and functionality for clarity. This function can get all information abut a tournament, not just teams in a tournament
def get_tournament_info():
    game = input("Enter the game to search for: ")
    # context = input("Enter the context to search for: ")
    search_param = input("Enter a tournament to search for.\nLeave blank to see all currently running tournaments:  ")
    url = tournament_url_builder(game, search_param)
    # url = url_builder(game, context, search_param)
    tournaments_dict = build_dict(url)

    print(tournaments_dict)

    for tournament in tournaments_dict:
        # TODO: Replace this print with something for the bot
        print("\n\nTournament: ", tournament['league']['name'], tournament['league']['image_url'],
              "\nParticipating Teams: ")

        for team in tournament['teams']:
            # TODO: Replace this print with something for the bot
            print("     ", team['name'], ": ", team['image_url'])


# Displays all information about teams
def get_team_info():
    game = input("Enter the game to search for: ")
    context = 'teams'
    search_param = input("Enter a team to search for.\nLeave blank to see all currently active teams:  ")
    url = url_builder(game, context, search_param)
    teams_dict = build_dict(url)

    for team in teams_dict:
        # TODO: Replace this print with something for the bot
        if team['acronym'] == None:
            print("\n\nTeam: ", team['name'], "| Image: ", team['image_url'],
                  "\nBased out of: ", team['location'])
        else:
            print("\n\nTeam: ", team['name'], "(", team['acronym'], ")", "Image: ", team['image_url'],
                  "\nBased out of: ", team['location'])

        for player in team['players']:
            # TODO: Replace this print with something for the bot
            print("     ", player['name'], ": ", player['first_name'], player['last_name'], "| Age: ", player['age'],
                  "| Hometown: ", player['hometown'], "| Nationality : ", player['nationality'])


if __name__ == '__main__':
    # Testing getting tournament info
    # while 0 != 1:
    #     get_tournament_info()
    #     get_team_info()
    #     get_player_info()

    # get_tournament_info()
    # get_team_info()
    get_player_info()
