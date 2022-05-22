import logging
from os import getenv

from telethon import TelegramClient, events

from filter import make_filter


log = logging.getLogger(__name__)


def handle_albums(client: TelegramClient, targets: list[str]) -> None:
    filter = make_filter(targets)

    @client.on(events.Album(func=filter))
    async def album_handler(event: events.Album):
        log.info('Forwarding album post')
        photos = []
        for message in event.messages:
            photos.append(message.media)
        await client.send_file(getenv('BOT'), photos)


def handle_any_message(client: TelegramClient, targets: list[str]) -> None:
    filter = make_filter(targets)

    @client.on(events.NewMessage(func=filter))
    async def any_message_handler(event: events.NewMessage):
        if event.grouped_id is None:
            log.info('Forwarding simple post')
            await event.forward_to(getenv('BOT'))
