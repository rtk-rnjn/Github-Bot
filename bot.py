from __future__ import annotations

from datetime import datetime
import logging
import os
import aiohttp
from discord.ext import commands
import github
import discord
import config
from cogs import DEFAULT_COGS


class GithubPython(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.uptime = datetime.utcnow()
        self._config = config

    async def setup_hook(self):
        await self.load_extension('jishaku')
        self.session = aiohttp.ClientSession(headers={'User-Agent' : 'GithubPythonBot'})
        os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
        os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
        os.environ["JISHAKU_HIDE"] = "True"
        for loadable in DEFAULT_COGS:
            try:
                await self.load_extension(loadable)
            except Exception as e:
                logging.error(f'Failed to load extension {loadable}.', exc_info=e)

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        if before.content == after.content:
            return
        await self.process_commands(after)

    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
        logging.getLogger('discord').error(error)

    async def start(self) -> None:
        await super().start(self._config.BOT_TOKEN)
