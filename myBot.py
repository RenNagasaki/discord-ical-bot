from discord.ext.commands import Bot
import logging
import discord


class MyBot(Bot):
    def __init__(self, token: str, guild: str, cal_channel_id: int, command_prefix: str, **options) -> None:
        """
        Summary:
        Initialize the bot.

        Args:
            token: bot token
            guild: server id the bot should interact with
            command_prefix: [$,!,>,etc.] prefix for commands
            **options:
        """
        intents = discord.Intents.all()
        super().__init__(command_prefix, **options, intents=intents)
        self.token = token
        self.guild = guild
        self.cal_channel_id = cal_channel_id

    async def on_ready(self) -> None:
        """
        Summary:
        Called when bot is ready to be used.
        """
        logging.info("Logged in as %s", self.user)
        logging.info("Getting channel: " + self.cal_channel_id.__str__())
        self.message_channel = self.get_channel(self.cal_channel_id)
