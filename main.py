import logging
from myBot import MyBot
from environs import Env
from cogs.calendar import Calendar
from logging import basicConfig


def main() -> None:
    """Main function."""
    basicConfig(level=logging.INFO)

    env = Env()
    env.read_env()
    BOT_TOKEN = env.str("BOT_TOKEN")
    GUILD_ID = env.str("GUILD_ID")
    ICAL_URL = env.str("ICAL_URL")
    CHANNEL_ID = env.str("CHANNEL_ID")
    CAL_CHANNEL_ID = env.int("CAL_CHANNEL_ID")

    bot = MyBot(token=BOT_TOKEN, guild=GUILD_ID, cal_channel_id=CAL_CHANNEL_ID, command_prefix="$")
    bot.add_cog(Calendar(bot, ICAL_URL, CHANNEL_ID))
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
