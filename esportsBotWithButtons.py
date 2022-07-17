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
    embed_list = create_player_embed(players_dict, 'valorant')
    # crate a navigator message, iwth the embeds and a set of custom buttons
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
    embed_list = create_team_embed(team_dict, 'valorant')
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


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
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@league.child()
@lightbulb.option('team_name', 'Team you want to search for')
@lightbulb.command('team_search', 'Get information about a professional League team')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lol_team_search(ctx):
    url = url_builder('lol', 'teams', ctx.options.team_name)
    team_dict = build_dict(url)
    embed_list = create_team_embed(team_dict, 'lol')
    navigator = nav.NavigatorView(pages=embed_list, buttons=nav_buttons_generator())
    await navigator.send(ctx.interaction)


@league.child()
@lightbulb.option('tournament_name', 'Tournament you want to search for')
@lightbulb.command('tournament_search', 'Get information about a League tournament')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tournament_search(ctx):
    await ctx.respond('You searched for tournament: ' + ctx.options.tournament_name)



if __name__ == '__main__':
    bot.run()
