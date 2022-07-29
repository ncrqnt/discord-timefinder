import re
import time
import string
import unicodedata

from datetime import datetime, timedelta
from pytz import timezone

from core.base import CustomClient

from naff import (
    Button,
    ButtonStyles,
    ComponentContext, Embed,
    EmbedField,
    Extension, InteractionContext,
    OptionTypes,
    SlashCommandChoice,
    component_callback, slash_command,
    slash_option,
)


class CommandExtension(Extension):
    bot: CustomClient

    @slash_command(name="findtime", description="Find a time together")
    @slash_option(
        name="earliest",
        description="earliest time in 12h/24h format (e.g. 11:00pm / 23:00)",
        required=True,
        opt_type=OptionTypes.STRING
    )
    @slash_option(
        name="latest",
        description="latest time in 12h/24h format (e.g. 11:00pm / 23:00)",
        required=True,
        opt_type=OptionTypes.STRING
    )
    @slash_option(
        name="interval",
        description="interval of the suggested times",
        required=True,
        opt_type=OptionTypes.INTEGER,
        choices=[
            SlashCommandChoice(name="00", value=0),
            SlashCommandChoice(name="15", value=15),
            SlashCommandChoice(name="30", value=30),
        ]
    )
    async def my_command(self, ctx: InteractionContext, earliest: str,
                         latest: str, interval: int):

        # check for time format
        time_pattern_12 = re.compile("^(0?[1-9]|1[0-2]):([0-5]\d)((?:a|p)m)$")
        time_pattern_24 = re.compile("^(0?[0-9]|1\d|2[0-3]):([0-5]\d)$")

        # convert time to datetime
        if time_pattern_24.match(earliest) and time_pattern_24.match(latest):
            earliest = datetime.strptime(earliest, "%H:%M").time()
            latest = datetime.strptime(latest, "%H:%M").time()

        elif time_pattern_12.match(earliest) and time_pattern_12.match(latest):
            earliest = datetime.strptime(earliest, "%H:%M%p").time()
            latest = datetime.strptime(latest, "%H:%M%p").time()

        else:
            print("earliest or latest doesn't match pattern")
            return

        # set correct datetimes
        today = datetime.today()

        if latest < earliest:
            latest_day = today.day+1
        else:
            latest_day = today.day

        earliest_datetime = today.replace(
            hour=earliest.hour, minute=earliest.minute, second=0,
            microsecond=0, tzinfo=timezone('UTC'))

        latest_datetime = today.replace(
            day=latest_day, hour=latest.hour, minute=latest.minute,
            second=0, microsecond=0, tzinfo=timezone('UTC'))

        print("{0}, {1}, {2}".format(
            earliest_datetime, latest_datetime, interval))

        # generate time suggestions
        if interval == 0:
            interval = "60"
        suggestions = []
        time_suggest = earliest_datetime
        while time_suggest <= latest_datetime:
            suggestions.append(time_suggest)
            time_suggest += timedelta(minutes=int(interval))

        # print(suggestions)

        if len(suggestions) > 24:
            print("suggestion list has more than 24 items, it'll be trimmed")

        suggestions = suggestions[:24]

        # generate fields
        fields = []
        vote_reaction = []
        alphabet = list(string.ascii_uppercase)
        i = 0

        for suggest in suggestions:
            unix = int(time.mktime(suggest.timetuple()))
            fields.append(EmbedField(
                name=alphabet[i], value=f"<t:{unix}:t>", inline=True))
            emoji = unicodedata.lookup(
                f"Regional Indicator Symbol Letter {alphabet[i]}")
            vote_reaction.append(emoji)
            i += 1

        print(vote_reaction)

        # adds a component to the message
        components = []
        # components.append(
        #     Button(
        #         style=ButtonStyles.GREEN,
        #         label="Close",
        #         custom_id="hello_world_button"
        #     )
        # )

        # adds an embed to the message
        embed = Embed(title="TimeFinder9000",
                      description="Vote for a suitable time for you",
                      fields=fields
                      )

        # respond to the interaction
        message = await ctx.send("", embeds=embed, components=components)

        for vote in vote_reaction:
            await message.add_reaction(vote)

    @component_callback("hello_world_button")
    async def my_callback(self, ctx: ComponentContext):
        """Callback for the component from the hello_world command"""

        await ctx.send("Closed by {0}".format(ctx.author.display_name))


def setup(bot: CustomClient):
    """Let naff load the extension"""

    CommandExtension(bot)
