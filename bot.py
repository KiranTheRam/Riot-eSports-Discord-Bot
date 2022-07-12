import hikari
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()
_token = os.getenv('TOKEN')
_guild_id = os.getenv('DEFAULT_ENABLED_GUILD')

bot = lightbulb.BotApp(
    token=_token,
    default_enabled_guilds=_guild_id
)

# Loading plugin
bot.load_extensions_from('./extensions')


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has been started!')


# Basic command with no input
@bot.command()
@lightbulb.command('command-name', 'description of the command')
@lightbulb.implements(lightbulb.SlashCommand)
async def command_name(ctx):  # all commands must take in a context object, commonly called ctx
    await ctx.respond('this is the reply the bot will display when triggered')

# Another basic command with no input
@bot.command()
@lightbulb.command('classic', 'prints Hello World!')
@lightbulb.implements(lightbulb.SlashCommand)
async def command_name(ctx):  # all commands must take in a context object, commonly called ctx
    await ctx.respond('Hello World')


# This is a Slash Command Group. Means it has subcommands tht it runs
@bot.command()
@lightbulb.command('group-name', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass  # this means don't do anything
    # we do nothing here since a command group cannot be run on its own.
    # Only the subcommands can be run
    # TODO: Might be a good idea to have valorant and LoL subgroups


# we use a decorator to show this command being made is a sub command on the 'my_group' group
@my_group.child()
@lightbulb.command('subcommand-one', 'This is the first subcommand under the my_group group')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('This is subcommand one!')


@my_group.child()
@lightbulb.command('subcommand-two', 'This is the second subcommand under the my_group group')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('This is subcommand two!')


# This example gives the user options to fill in
@bot.command()
@lightbulb.option('option3', 'desc of second option')
@lightbulb.option('option2', 'desc of first option')
@lightbulb.option('option1', 'desc of first option')
@lightbulb.command('input-cmd', 'this demos taking input')
@lightbulb.implements(lightbulb.SlashCommand)
async def input_cmd(ctx):
    await ctx.respond(
        'First thing you entered: ' + ctx.options.option1 + '\nSecond thing you entered: ' + ctx.options.option2 + '\nThird thing you entered: ' + ctx.options.option3)


bot.run()
