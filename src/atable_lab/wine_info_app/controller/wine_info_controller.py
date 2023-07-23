from fastapi.encoders import jsonable_encoder
from atable_lab.wine_info_app.lib.utils import *
from atable_lab.wine_info_app.controller import BaseController
from atable_lab.wine_info_app.model.wine_info_model import WineInfo


class WineInfoController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        kwargs['collection'] = get_collection_name_from_class_name(self.__class__.__name__)
        self.wine_info_model: WineInfo = WineInfo(**kwargs)

    def create(self, params: dict):
        return self.wine_info_model.create(params)

    def get(self):
        pass
