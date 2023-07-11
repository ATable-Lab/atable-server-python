from backend.lib.logger import log_handler
from fastapi import APIRouter, Request
from backend.controller import WineInfoController
from backend.model.wine_info_model import WineInfo

router = APIRouter()


@router.post("/create", openapi_extra=WineInfo.meta())
async def create(request: Request):
    '''
    **name**: wine name

    price: wine price
    '''
    request_body = await request.json()
    controller = WineInfoController()
    return controller.create(request_body)
