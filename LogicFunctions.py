import hikari
import json
import requests

default_image = 'images/default.jpg'
valorant_image = 'images/valorant.png'
lol_image = 'images/league.png'
ow_image = 'images/ow.jpg'
csgo_image = 'images/csgo.jpg'
r6s_image = 'images/r6s.jpg'
rl_image = 'images/rl.jpg'

riot_red = 'd22a36'
cs_yellow = 'de9b35'
ow_orange = 'f99e1a'
r6_white = 'ffffff'
rl_blue = '0060ff'
default_color = '1DB954'


# This will build a dictionary based on the URL given and JSON returned
def build_dict(url):
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 13tgKXTDBY-RKazKMm3RArrw-K5BDYOAwxBfTtC_yFgejoHieKU"
    }
    response = requests.get(url, headers=headers)
    working_dict = json.loads(response.text)
    return working_dict


def url_builder(game, context, search_param):
    url = "https://api.pandascore.co/" + game + "/" + context + "?search[name]=" + search_param + "&sort=&page=1&per_page=50"
    return url


def tournament_url_builder(game, search_param):
    url = "https://api.pandascore.co/" + game + "/tournaments/running?search[slug]=" + search_param + "&sort=&page=1&per_page=50"
    return url


def color_picker(game):
    if game == 'valorant':
        return riot_red
    elif game == 'lol':
        return riot_red
    elif game == 'ow':
        return ow_orange
    elif game == 'csgo':
        return cs_yellow
    elif game == 'r6siege':
        return r6_white
    elif game == 'rl':
        return rl_blue
    else:
        return default_color


def image_picker(game):
    if game == 'valorant':
        return valorant_image
    elif game == 'lol':
        return lol_image
    elif game == 'ow':
        return ow_image
    elif game == 'csgo':
        return csgo_image
    elif game == 'r6siege':
        return r6s_image
    elif game == 'rl':
        return rl_image
    else:
        return default_image


def create_player_embed_all(passed_dict, game, search_term):
    # Function will return a list of embeds
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for player in passed_dict:
            # Set all values to N/A
            game_name = "N/A"
            name = "N/A"
            current_team = "N/A"
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
            # if 'hometown' in player and player['hometown'] is not None:
            #     hometown = player['hometown']
            if 'nationality' in player and player['nationality'] is not None:
                nationality = player['nationality']

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
            embed.add_field("Nationality", nationality, inline=True)
            embed.set_footer("Searched for: " + search_term + "\nN/A = Not Available")
            embed.set_thumbnail(image_url)
            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image)
        embed_list.append(embed)
        return embed_list

    return embed_list


def create_player_embed_partial(passed_dict, game, search_term):
    # Function will return a list of embeds
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for player in passed_dict:
            # Set all values to N/A
            game_name = "N/A"
            name = "N/A"
            current_team = "N/A"
            nationality = "N/A"

            color = color_picker(game)
            image_url = image_picker(game)

            # Test each value from dictionary and fill variable if it is available
            if 'name' in player and player['name'] is not None:
                game_name = player['name']
            if 'first_name' in player and player['first_name'] is not None:
                name = player['first_name']
            if 'last_name' in player and player['last_name'] is not None:
                name += " " + player['last_name']
            if 'current_team' in player and player['current_team'] is not None:
                current_team = player['current_team']['name']
            if 'nationality' in player and player['nationality'] is not None:
                nationality = player['nationality']

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
            embed.add_field("Nationality", nationality, inline=True)
            embed.set_footer("Searched for: " + search_term + " \nN/A = Not Available")
            embed.set_thumbnail(image_url)
            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image)
        embed_list.append(embed)
        return embed_list

    return embed_list


def create_player_role(passed_dict, game, search_term):
    # Function will return a list of embeds
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for player in passed_dict:
            # Set all values to N/A
            game_name = "N/A"
            name = "N/A"
            current_team = "N/A"
            role = "N/A"
            nationality = "N/A"

            color = color_picker(game)
            image_url = image_picker(game)

            # Test each value from dictionary and fill variable if it is available
            if 'name' in player and player['name'] is not None:
                game_name = player['name']
            if 'first_name' in player and player['first_name'] is not None:
                name = player['first_name']
            if 'last_name' in player and player['last_name'] is not None:
                name += " " + player['last_name']
            if 'current_team' in player and player['current_team'] is not None:
                current_team = player['current_team']['name']
            if 'role' in player and player['role'] is not None:
                role = player['role']
            if 'nationality' in player and player['nationality'] is not None:
                nationality = player['nationality']

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
            embed.add_field("Role", role, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Nationality", nationality, inline=True)
            embed.set_footer("Searched for: " + search_term + " \nN/A = Not Available")
            embed.set_thumbnail(image_url)
            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image)
        embed_list.append(embed)
        return embed_list

    return embed_list


def create_team_embed(passed_dict, game, search_term):
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

            embed = hikari.Embed(title=team_name, colour=color, description=("Based out of: " + location))
            embed.set_footer("Searched for: " + search_term + " \nN/A = Not Available")
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
                counter += 1
                if counter % 2 != 0:
                    embed.add_field('\u200b', '\u200b', inline=True)

            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image)
        embed_list.append(embed)
        return embed_list

    return embed_list


def create_tournament_embed(passed_dict, game, search_term):
    embed_list = []

    if passed_dict:  # if the dictionary is NOT empty
        for tournament in passed_dict:
            color = color_picker(game)
            image_url = image_picker(game)

            # Test each value from dictionary and fill variable if it is available
            if 'name' in tournament['serie'] is not None:
                tournament_name = tournament['serie']['full_name']

            match_list = []

            for match in tournament['matches']:
                name = match['name']
                status = match['status']
                date = match['scheduled_at']
                match_list.append(
                    name + "\u1CBC | \u1CBC" + status + "\u1CBC | \u1CBC" + date[:10])

            list_str = '\n\n'.join(match_list)
            embed = hikari.Embed(title=tournament_name, colour=color, description=list_str)
            embed.set_footer("Searched for: " + search_term + " \nN/A = Not Available")
            embed.set_thumbnail(image_url)
            match_list.clear()
            embed_list.append(embed)

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(default_image)
        embed_list.append(embed)
        return embed_list

    return embed_list
