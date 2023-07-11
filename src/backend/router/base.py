import logging
from fastapi import APIRouter, Request
from backend.lib.logger import log_handler

router = APIRouter()

_LOGGER = logging.getLogger(__name__)


@router.get("/check")
async def index():
    return {"status": "RUNNING"}
