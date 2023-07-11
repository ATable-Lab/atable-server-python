from backend.model import BaseAPIModel
from pydantic import Field
from typing import Union, List
from datetime import datetime


class WineInfo(BaseAPIModel):
    name: str = Field(...)
    price: float = Field(...)
    currency: str = Field(None)
