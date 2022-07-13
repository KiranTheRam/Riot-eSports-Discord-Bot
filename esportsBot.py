import hikari
import lightbulb
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
_token = os.getenv('TOKEN')
_guild_id = os.getenv('DEFAULT_ENABLED_GUILD')

bot = lightbulb.BotApp(
    token=_token
)

# Global Variables
valorant_image_url = 'https://cdn.vox-cdn.com/thumbor/FJz0LeakZVB3NCy17LSHzeE8yX8=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19884649/VALORANT_Jett_Red_1_1.jpg'
lol_image_url = 'https://static.wikia.nocookie.net/leagueoflegends/images/7/7b/League_of_Legends_Cover.jpg/revision/latest?cb=20191018222445'


# Section for API handling functions

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


# Section for bot commands & functions
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot Activated!')


# This is a Slash Command Group. Means it has subcommands that it runs
@bot.command()
@lightbulb.command('valorant', 'All commands referring to Valorant')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def valorant(ctx):
    pass  # this means don't do anything
    # we do nothing here since a command group cannot be run on its own.
    # Only the subcommands can be run


def create_player_embed(dict, game):
    # Function will return a list of embeds
    embed_list = []

    if dict:  # if the dictionary is NOT empty
        for player in dict:
            # Set all values to N/A
            game_name = "N/A"
            name = "N/A"
            current_team = "N/A"
            hometown = "N/A"
            nationality = "N/A"
            age = "N/A"
            birthday = "N/A"

            if game == 'valorant':
                image_url = valorant_image_url
            elif game == 'lol':
                image_url = lol_image_url

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

            print("\nGamer Name: " + game_name)
            print("Name: " + name)
            print("Age: " + age)
            print("Birthday: " + birthday)
            print("Team: " + current_team)
            print("Hometown: " + hometown)
            print("Nationality: " + nationality)


            # Try to get image of player
            if 'image_url' in player and player['image_url'] is not None:
                image_url = player['image_url']
            # If player image isn't available, get image of team instead
            elif 'current_team' in player and player['current_team'] is not None:
                if player['current_team']['image_url'] is not None:
                    image_url = player['current_team']['image_url']

            # For each player found, send an embed
            # TODO: Possibly change this to a single embed with pages?
            embed = hikari.Embed(title=game_name, colour='d22a36')
            embed.add_field("Name", name, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Team", current_team, inline=True)
            embed.add_field('Age', age, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Birthday", birthday, inline=True)
            embed.add_field("Hometown", hometown, inline=True)
            embed.add_field('\u200b', '\u200b', inline=True)
            embed.add_field("Nationality", nationality, inline=True)
            embed.set_thumbnail(image_url)
            embed_list.append(embed)

            if len(embed_list) == 8:
                return embed_list

    else:  # If the dictionary IS empty
        embed = hikari.Embed(title='No Results Found', description='Please try again')
        embed.set_thumbnail(valorant_image_url)
        embed_list.append(embed)
        return embed_list

    return embed_list


@valorant.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional Valorant player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_player_search(ctx):

    url = url_builder('valorant', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    # print(players_dict)
    embed_list = create_player_embed(players_dict, 'valorant')

    for embed in embed_list:
        # print(embed)
        await ctx.respond(embed)  # or respond(embed=embed)

    # url = url_builder('valorant', 'players', ctx.options.player_name)
    # players_dict = build_dict(url)
    # results_printed = 0
    #
    # if players_dict:  # if the dictionary is NOT empty
    #     for player in players_dict:
    #         if results_printed == 8:
    #             break
    #
    #         # Set all values to N/A
    #         game_name = "N/A"
    #         name = "N/A"
    #         current_team = "N/A"
    #         hometown = "N/A"
    #         nationality = "N/A"
    #         age = "N/A"
    #         birthday = "N/A"
    #         image_url = valorant_image_url
    #
    #         # Test each value from dictionary and fill variable if it is available
    #         if player['name'] is not None:
    #             game_name = player['name']
    #         if player['first_name'] is not None:
    #             name = player['first_name']
    #         if player['last_name'] is not None:
    #             name += " " + player['last_name']
    #         if player['age'] is not None:
    #             age = str(player['age'])
    #         if player['birthday'] is not None:
    #             birthday = player['birthday']
    #         if player['current_team'] is not None:
    #             current_team = player['current_team']['name']
    #         if player['hometown'] is not None:
    #             hometown = player['hometown']
    #         if player['nationality'] is not None:
    #             nationality = player['nationality']
    #
    #         # Try to get image of player
    #         if player['image_url'] is not None:
    #             image_url = player['image_url']
    #         # If player image isn't available, get image of team instead
    #         elif player['current_team'] is not None:
    #             if player['current_team']['image_url'] is not None:
    #                 image_url = player['current_team']['image_url']
    #
    #         # For each player found, send an embed
    #         # TODO: Possibly change this to a single embed with pages?
    #         embed = hikari.Embed(title=game_name)
    #         embed.add_field("Name", name, inline=True)
    #         embed.add_field('\u200b', '\u200b', inline=True)
    #         embed.add_field("Team", current_team, inline=True)
    #         embed.add_field('Age', age, inline=True)
    #         embed.add_field('\u200b', '\u200b', inline=True)
    #         embed.add_field("Birthday", birthday, inline=True)
    #         embed.add_field("Hometown", hometown, inline=True)
    #         embed.add_field('\u200b', '\u200b', inline=True)
    #         embed.add_field("Nationality", nationality, inline=True)
    #         embed.set_thumbnail(image_url)
    #         await ctx.respond(embed)  # or respond(embed=embed)
    #         results_printed += 1
    #
    # else:  # If the dictionary IS empty
    #     embed = hikari.Embed(title='No Results Found', description='Please try again')
    #     embed.set_thumbnail(valorant_image_url)
    #     await ctx.respond(embed)  # or respond(embed=embed)


@valorant.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional Valorant team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_team_search(ctx):
    await ctx.respond('You searched for team: ' + ctx.options.team_name)


@valorant.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a Valorant tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_tournament_search(ctx):
    await ctx.respond('You searched for tournament: ' + ctx.options.tournament_name)


@bot.command()
@lightbulb.command('league', 'All commands referring to League of Legends')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def league(ctx):
    pass


@league.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional League player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lol_player_search(ctx):
    url = url_builder('lol', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    print(players_dict)
    embed_list = create_player_embed(players_dict, 'lol')

    # print("\nEmbed List:")
    # print(embed_list)

    for embed in embed_list:
        # print("\nEmbed:")
        # print(embed)

        await ctx.respond(embed)  # or respond(embed=embed)


@league.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional League team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lol_team_search(ctx):
    await ctx.respond('You searched for team: ' + ctx.options.team_name)


@league.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a League tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tournament_search(ctx):
    await ctx.respond('You searched for tournament: ' + ctx.options.tournament_name)


# Boiler plate embed code
@bot.command()
@lightbulb.command('sendlove', 'Sends an embed in the command channel')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx):
    embed = hikari.Embed(title="Example embed", description="An example hikari embed")
    embed.add_field("Field name", "Field content (value)")
    embed.set_thumbnail("https://i.imgur.com/EpuEOXC.jpg")
    embed.set_footer("This is the footer")
    await ctx.respond(embed)  # or respond(embed=embed)


if __name__ == '__main__':
    bot.run()