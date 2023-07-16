from fastapi.encoders import jsonable_encoder
from atable_lab.wine_info_app.controller import BaseController
from atable_lab.wine_info_app.model.wine_info_model import WineInfo


class WineInfoController(BaseController):

    def create(self, params: dict):
        pass

    def get(self):
        pass
