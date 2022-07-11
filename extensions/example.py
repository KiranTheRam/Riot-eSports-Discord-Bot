import lightbulb
import hikari
plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@plugin.command
@lightbulb.command('ping2', 'says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping1(ctx):
    await ctx.respond('Ponggggg')

def load(bot):
    bot.add_plugin(plugin)