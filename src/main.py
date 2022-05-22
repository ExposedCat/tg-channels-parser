import logging
import asyncio
from os import getenv
from dotenv import load_dotenv

from bot_config import init_bot, start_bot


load_dotenv('.env')

asyncio.set_event_loop(asyncio.new_event_loop())

logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__name__)

client = init_bot(getenv('CHANNELS').split(' '))
start_bot(client)
