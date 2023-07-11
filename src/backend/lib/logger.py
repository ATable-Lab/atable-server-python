import logging
from fastapi import Request

logging.basicConfig(level=logging.DEBUG, format='')
_LOGGER = logging.getLogger(__name__)


def log_handler(func):
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapper


