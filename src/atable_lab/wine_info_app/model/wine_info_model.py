from atable_lab.wine_info_app.model import BaseAPIModel
from pydantic import Field


class WineInfo(BaseAPIModel):
    name: str = Field(...)
    price: float = Field(...)
    currency: str = Field(None)
