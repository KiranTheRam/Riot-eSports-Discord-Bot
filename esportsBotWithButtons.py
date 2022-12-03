import hikari
import lightbulb
import os
from dotenv import load_dotenv

from LogicFunctions import *
from ButtonHandling import *

load_dotenv()
_token = os.getenv('TOKEN')
_guild_id = os.getenv('DEFAULT_ENABLED_GUILD')

bot = lightbulb.BotApp(
    token=_token
)

miru.load(bot)


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


# All commands are similar, so only this one will have explanation comments
@valorant.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional Valorant player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_player_search(ctx):
    # Build the url for the api we are using
    url = url_builder('valorant', 'players', ctx.options.player_name)
    # Use the url to send the request. Then take returned json and make it into a dict
    players_dict = build_dict(url)
    # Parse dict and create embeds for the first 8 results
    embed_list = create_player_embed_all(players_dict, 'valorant', ctx.options.player_name)
    # crate a navigator message, with the embeds and a set of custom buttons
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    # Send the navigator in response to command call
    await navigator.send(ctx.interaction)


@valorant.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional Valorant team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_team_search(ctx):
    url = url_builder('valorant', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'valorant', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@valorant.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a Valorant tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def val_tournament_search(ctx):
    url = tournament_url_builder('valorant', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'valorant', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


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
    embed_list = create_player_role(players_dict, 'lol', ctx.options.player_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@league.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional League team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lol_team_search(ctx):
    url = url_builder('lol', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'lol', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@league.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a League tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tournament_search(ctx):
    url = tournament_url_builder('lol', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'lol', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


# -------------------------------------------------------

@bot.command()
@lightbulb.command('overwatch', 'All commands referring to Overwatch')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def overwatch(ctx):
    pass


@overwatch.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional League player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ow_player_search(ctx):
    url = url_builder('ow', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    embed_list = create_player_role(players_dict, 'ow', ctx.options.player_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@overwatch.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional League team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ow_team_search(ctx):
    url = url_builder('ow', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'ow', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@overwatch.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a League tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ow_tournament_search(ctx):
    url = tournament_url_builder('ow', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'ow', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


# -------------------------------------------------------

@bot.command()
@lightbulb.command('csgo', 'All commands referring to Counter Strike: Global Offensive')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def csgo(ctx):
    pass


@csgo.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional CSGO player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def csgo_player_search(ctx):
    url = url_builder('csgo', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    embed_list = create_player_embed_partial(players_dict, 'csgo', ctx.options.player_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@csgo.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional CSGO team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def csgo_team_search(ctx):
    url = url_builder('csgo', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'csgo', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@csgo.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a CSGO tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def csgo_tournament_search(ctx):
    url = tournament_url_builder('csgo', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'csgo', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


# -------------------------------------------------------

@bot.command()
@lightbulb.command('r6siege', 'All commands referring to Rainbow 6 Siege')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def r6siege(ctx):
    pass


@r6siege.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional Rainbow 6 Siege player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def r6siege_player_search(ctx):
    url = url_builder('r6siege', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    embed_list = create_player_embed_all(players_dict, 'r6siege', ctx.options.player_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@r6siege.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional Rainbow 6 Siege team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def r6siege_team_search(ctx):
    url = url_builder('r6siege', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'r6siege', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@r6siege.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a Rainbow 6 Siege tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def r6siege_tournament_search(ctx):
    url = tournament_url_builder('r6siege', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'r6siege', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


# -------------------------------------------------------

@bot.command()
@lightbulb.command('rl', 'All commands referring to Rocket League')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def rl(ctx):
    pass


@rl.child()
@lightbulb.option('player_name', 'Player you want to search for')
@lightbulb.command('player_search', 'Get information about a professional Rocket League player')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def rl_player_search(ctx):
    url = url_builder('rl', 'players', ctx.options.player_name)
    players_dict = build_dict(url)
    embed_list = create_player_embed_all(players_dict, 'rl', ctx.options.player_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@rl.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional Rocket League team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def rl_team_search(ctx):
    url = url_builder('rl', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'rl', ctx.options.team_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@rl.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a Rocket League tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def r6siege_tournament_search(ctx):
    url = tournament_url_builder('rl', ctx.options.tournament_name)
    tournament_dict = build_dict(url)
    embed_list = create_tournament_embed(tournament_dict, 'rl', ctx.options.tournament_name)
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


if __name__ == '__main__':
    bot.run()
