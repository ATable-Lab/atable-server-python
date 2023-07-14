import logging
from fastapi import APIRouter

router = APIRouter()

_LOGGER = logging.getLogger(__name__)


@router.get("/check")
async def index():
    return {"status": "RUNNING"}
