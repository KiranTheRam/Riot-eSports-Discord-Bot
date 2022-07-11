import hikari
import lightbulb

bot = lightbulb.BotApp(
    token="OTE1NzQzMTkxOTYwMDI3MTk2.GiP3p3.f3a4IZ9wgyibvOgFnqMH1zOL5Se3wIqyTIvnZ0",
    default_enabled_guilds=(918548261202190417)
)

bot.load_extensions_from('./extensions')

@bot.command
@lightbulb.command('ping', 'says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('group', 'slash command group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command("subcommand", 'this is a sub command')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a sub')

@bot.command
@lightbulb.option('num2', 'Second number to be added', type=int)
@lightbulb.option('num1', 'First number to be added', type=int)
@lightbulb.command('add', 'adds 2 numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.run()
