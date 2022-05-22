import logging
from os import getenv

from telethon import TelegramClient

from handlers import handle_albums, handle_any_message


log = logging.getLogger(__name__)


def init_bot(targets: list[str]) -> TelegramClient:
    log.info('Initializing client…')
    client = TelegramClient(
        session=getenv('SESSION_NAME') or 'meowgram_parser',
        api_id=getenv('API_ID'),
        api_hash=getenv('API_HASH'),
    )
    log.info('Done')
    log.info('Setting up handlers…')
    handle_albums(client, targets)
    handle_any_message(client, targets)
    log.info('Done')
    return client


def start_bot(client: TelegramClient):
    log.info('Starting client…')
    client.start()
    log.info('Done')
    client.run_until_disconnected()
