import hikari
import miru
from miru.ext import nav

class MyNavButton(nav.NavButton):
    # This is how you can create your own navigator button
    # The extension also comes with the following nav buttons built-in:
    #
    # FirstButton - Goes to the first page
    # PrevButton - Goes to previous page
    # IndicatorButton - Indicates current page number
    # StopButton - Stops the navigator session and disables all buttons
    # NextButton - Goes to next page
    # LastButton - Goes to the last page

    async def callback(self, ctx: miru.Context) -> None:
        await ctx.respond("You clicked me!", flags=hikari.MessageFlag.EPHEMERAL)

    async def before_page_change(self) -> None:
        # This function is called before the new page is sent by
        # NavigatorView.send_page()
        self.label = f"Page: {self.view.current_page+1}"


def nav_buttons_generator():
    buttons = [
        nav.FirstButton(style=hikari.ButtonStyle.DANGER, emoji='', label='<<'),
        nav.PrevButton(style=hikari.ButtonStyle.DANGER, emoji='', label='<'),
        MyNavButton(label="Page: 1", disabled=True, style=hikari.ButtonStyle.SECONDARY),
        nav.NextButton(style=hikari.ButtonStyle.DANGER, emoji='', label='>'),
        nav.LastButton(style=hikari.ButtonStyle.DANGER, emoji='', label='>>'),
        # nav.StopButton(emoji='', label='X')
    ]

    return buttons

