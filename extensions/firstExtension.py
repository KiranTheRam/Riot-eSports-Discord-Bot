import hikari
import lightbulb

# Creating an instance of a plugin
ourPlugin = lightbulb.Plugin('NameOfPlugin')


# listen for the event type specified (which in this case is someone creating a message in the guild)
# @ourPlugin.listener(hikari.GuildMessageCreateEvent)
# async def print_messages(event):
#     print(event.content)


@ourPlugin.command()
@lightbulb.command('extcmd', 'desc of the extension command')
@lightbulb.implements(lightbulb.SlashCommand)
async def extension_cmd(ctx):
    await ctx.respond('You\'ve called a command from our extension!')

# Adds out plugin to a passed bot
def load(bot):
    bot.add_plugin(ourPlugin)
