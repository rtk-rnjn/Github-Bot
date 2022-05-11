import asyncio
from datetime import datetime
import logging
import os
import aiohttp


import discord
from discord.ext import commands
import github

import config

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

    async def on_message_edit(self, before, after) -> None:
        if before.content == after.content:
            return
        await self.process_commands(after)

    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
        logging.getLogger('discord').error(error)

    async def start(self) -> None:
        await super().start(self._config.BOT_TOKEN)



