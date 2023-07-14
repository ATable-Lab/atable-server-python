from fastapi import APIRouter, Request
from atable_lab.wine_info_app.controller import WineInfoController
from atable_lab.wine_info_app.model.wine_info_model import WineInfo

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
