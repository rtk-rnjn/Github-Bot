import asyncio
from asyncio.log import logger
from logging import Logger
import logging
import re

import discord

from bot import GithubPython

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

async def launch():
    bot = GithubPython(command_prefix='?', description='GithubPythonBot',intents=discord.Intents.all())
    await bot.start()

asyncio.run(launch())