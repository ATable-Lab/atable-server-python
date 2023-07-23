import os

from bson import ObjectId
from pydantic import BaseModel
from pymongo import MongoClient

from atable_lab.wine_info_app.conf.server_conf import *


class BaseAPIModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect(**kwargs)

    @classmethod
    def connect(cls, **kwargs):
        local_mongo_db_config = DATABASE['mongo_db']
        host = os.environ.get('ATABLE_LAB_MONGO_DB_HOST', local_mongo_db_config.get('host'))
        port = os.environ.get('ATABLE_LAB_MONGO_DB_PORT', local_mongo_db_config.get('port'))
        mongo_id = os.environ.get('ATABLE_LAB_MONGO_DB_ID', local_mongo_db_config.get('id'))
        password = os.environ.get('ATABLE_LAB_MONGO_DB_PASSWORD', local_mongo_db_config.get('password'))
        database = os.environ.get('ATABLE_LAB_MONGO_DB_DATABASE', local_mongo_db_config.get('database'))
        env = os.environ.get('ATABLE_LAB_ENV')
        collection = kwargs['collection']
        if env:
            database = f'{env}-{database}'

        cls.client = MongoClient(f'mongodb+srv://{mongo_id}:{password}@{host}')[database][collection]

    @classmethod
    def meta(cls):
        return {
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": cls.schema()
                    }
                }
            }
        }


class BaseSchema(BaseModel):
    @classmethod
    def meta(cls):
        return {
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": cls.schema()
                    }
                }
            }
        }
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")