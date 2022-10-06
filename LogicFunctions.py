import hikari
import json
import requests

valorant_image_url = 'https://cdn.vox-cdn.com/thumbor/FJz0LeakZVB3NCy17LSHzeE8yX8=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19884649/VALORANT_Jett_Red_1_1.jpg'
lol_image_url = 'https://static.wikia.nocookie.net/leagueoflegends/images/7/7b/League_of_Legends_Cover.jpg/revision/latest?cb=20191018222445'
default_image_url = 'https://www.riotgames.com/darkroom/800/87521fcaeca5867538ae7f46ac152740:2f8144e17957078916e41d2410c111c3/002-rg-2021-full-lockup-offwhite.jpg'

riot_red = 'd22a36'
cs_yellow = 'de9b35'
ow_orange = 'f99e1a'
r6_white = 'ffffff'
rl_blue = '0060ff'
default_color = '1DB954'


# Section for API handling functions

# This will build a dictionary based on the URL given and JSON returned
def build_dict(url):
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 13tgKXTDBY-RKazKMm3RArrw-K5BDYOAwxBfTtC_yFgejoHieKU"
    }
    response = requests.get(url, headers=headers)
    working_dict = json.loads(response.text)
    print(working_dict)
    return working_dict


# This will create the API URL for running tournaments based on a search parameter if there is one
def tournament_url_builder(game, search_param):
    if search_param:
        url = "https://api.pandascore.co/" + game + "/tournaments/running?search[slug]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/" + game + "/tournaments/running?sort=&page=1&per_page=50"
    return url


# This will be the universal API URL builder.
def url_builder(game, context, search_param):
    if search_param:
        url = "https://api.pandascore.co/" + game + "/" + context + "?search[name]=" + search_param + "&sort=&page=1&per_page=50"
        return url
    url = "https://api.pandascore.co/" + game + "/players?sort=&page=1&per_page=50"
    return url


def color_picker(game):
    if game == 'valorant':
        image_url = valorant_image_url
        return riot_red
    elif game == 'lol':
        image_url = lol_image_url
        return riot_red
    elif game == 'ow':
        image_url = lol_image_url
        return ow_orange
    elif game == 'csgo':
        image_url = lol_image_url
        return cs_yellow
    elif game == 'r6siege':
        image_url = lol_image_url
        return r6_white
    elif game == 'rl':
        image_url = lol_image_url
        return rl_blue
    else:
        image_url = lol_image_url
        return default_color


def image_picker(game):
    if game == 'valorant':
        return valorant_image_url
    elif game == 'lol':
        return lol_image_url
    elif game == 'ow':
        return lol_image_url
    elif game == 'csgo':
        return lol_image_url
    elif game == 'r6siege':
        return lol_image_url
    elif game == 'rl':
        return lol_image_url
    else:
        return default_color


def create_player_embed(passed_dict, game):
    # Function will return a list of embeds
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for player in passed_dict:
            # Set all values to N/A
            game_name = "N/A"
            name = "N/A"
            current_team = "N/A"
            hometown = "N/A"
            nationality = "N/A"
            age = "N/A"
            birthday = "N/A"

            color = color_picker(game)
            image_url = image_picker(game)

            # Test each value from dictionary and fill variable if it is available
            if 'name' in player and player['name'] is not None:
                game_name = player['name']
            if 'first_name' in player and player['first_name'] is not None:
                name = player['first_name']
            if 'last_name' in player and player['last_name'] is not None:
                name += " " + player['last_name']
            if 'age' in player and player['age'] is not None:
                age = str(player['age'])
            if 'birthday' in player and player['birthday'] is not None:
                birthday = player['birthday']
            if 'current_team' in player and player['current_team'] is not None:
                current_team = player['current_team']['name']
            if 'hometown' in player and player['hometown'] is not None:
                hometown = player['hometown']
            if 'nationality' in player and player['nationality'] is not None:
                nationality = player['nationality']

            # print("\nGamer Name: " + game_name)
            # print("Name: " + name)
            # print("Age: " + age)
            # print("Birthday: " + birthday)
            # print("Team: " + current_team)
            # print("Hometown: " + hometown)
            # print("Nationality: " + nationality)

            # Try to get image of player
            if 'image_url' in player and player['image_url'] is not None:
                image_url = player['image_url']
            # If player image isn't available, get image of team instead
            elif 'current_team' in player and player['current_team'] is not None:
                if player['current_team']['image_url'] is not None:
                    image_url = player['current_team']['image_url']

            embed = hikari.Embed(title=game_name, colour=color)
            embed.add_field("Name", name, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Team", current_team, inline=True)
            embed.add_field('Age', age, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Birthday", birthday, inline=True)
            embed.add_field("Hometown", hometown, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Nationality", nationality, inline=True)
            embed.set_footer('N/A = Not Available')
            embed.set_thumbnail(image_url)
            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image_url)
        embed_list.append(embed)
        return embed_list

    return embed_list


def create_team_embed(passed_dict, game):
    # Function will return a list of embeds
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for team in passed_dict:
            # Set all values to N/A
            team_name = "N/A"
            location = "N/A"

            color = color_picker(game)
            image_url = image_picker(game)

            # Test each value from dictionary and fill variable if it is available
            if 'name' in team and team['name'] is not None:
                team_name = team['name']

            if 'location' in team and team['location'] is not None:
                location = team['location']

            # Try to get image of team
            if 'image_url' in team and team['image_url'] is not None:
                image_url = team['image_url']

            embed = hikari.Embed(title=team_name, colour='d22a36', description=("Based out of: " + location))
            embed.set_footer("For more player info, use Player Search command\nN/A = Not Available")
            embed.set_thumbnail(image_url)

            player_name = "N/A"
            player_real_name = "N/A"
            player_age = "N/A"
            counter = 0

            for player in team['players']:
                if 'name' in player and player['name'] is not None:
                    player_name = player['name']
                if 'first_name' in player and player['first_name'] is not None:
                    player_real_name = player['first_name']
                if 'last_name' in player and player['last_name'] is not None:
                    player_real_name += " " + player['last_name']
                if 'age' in player and player['age'] is not None:
                    player_age = str(player['age'])

                embed.add_field(player_name, (player_real_name + "\nAge: " + player_age), inline=True)

                # TODO: can this be replaced by using the index of a player within the team['players'] dict?
                counter += 1
                if counter % 2 != 0:
                    embed.add_field('\u200b', '\u200b', inline=True)

            embed_list.append(embed)


    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image_url)
        embed_list.append(embed)
        return embed_list

    return embed_list
