from datetime import datetime
from atable_lab.wine_info_app.model import BaseAPIModel, BaseSchema
from pydantic import BaseModel
from pydantic import Field

from bson import ObjectId


class WineInfo(BaseAPIModel):
    class WineInfoResult(BaseAPIModel):
        id: str = Field(...)
        name: str = None
        price: float = None
        currency: str = None
        created_at: datetime = None

    class Create(BaseSchema):
        name: str = Field(...)
        price: float = Field(...)
        region: str = Field(None)
        store_name: str = Field(None)
        event: bool = Field(None)
        discount_rate: float = Field(None)
        discount_price: float = Field(None)
        currency: str = Field(None)

    def create(self, params: Create):
        params['created_at'] = datetime.utcnow()

        result_object_id = self.client.insert_one(params)
        result = self.client.find_one({"_id": result_object_id.inserted_id})
        result['_id'] = str(result['_id'])

        return result
