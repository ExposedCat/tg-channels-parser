from typing import Callable
import logging

from telethon import events, types


log = logging.getLogger(__name__)


def message_has_links(message) -> bool:
    url_types = (types.MessageEntityUrl, types.MessageEntityTextUrl)
    entities = message.entities or ()
    return any(isinstance(entity, url_types) for entity in entities)


def make_filter(channels: list[int]) -> Callable[[events.Album], bool]:
    def filter(event: events.Album) -> bool:
        if hasattr(event, 'messages'):
            message = event.messages[0]
        else:
            message = event.message

        no_goes = (
            not event.is_channel,
            message.fwd_from,
            not str(event.chat_id) in channels,
            message_has_links(message),
        )
        return not any(no_goes)

    return filter
