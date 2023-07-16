from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from atable_lab.wine_info_app.controller.wine_info_controller import WineInfoController
from atable_lab.wine_info_app.model.wine_info_model import WineInfo

router = APIRouter()


@router.post("/create", openapi_extra=WineInfo.meta())
async def create(request: Request):
    '''
    **name**: wine name

    price: wine price
    '''

    params = await request.json()

    with WineInfoController() as wine_info_controller:
        return wine_info_controller.create(params)

