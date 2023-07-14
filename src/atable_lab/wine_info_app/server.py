import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from atable_lab.wine_info_app.conf.server_conf import *
from atable_lab.wine_info_app.router import wine_info, base


def _add_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app


def _add_routers(app):
    app.include_router(router=wine_info, tags=['wine-info > wine-info'], prefix='/wine-info')
    app.include_router(base)
    return app


def fast_api_app():
    app = FastAPI()
    app = _add_middlewares(app)
    app = _add_routers(app)
    return app
