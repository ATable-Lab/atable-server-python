import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.lib.config import set_config
from conf.server_conf import *
from backend.router import wine_info, base


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


def main():
    # uvicorn_options = CONFIG.get('UVICORN_OPTIONS', {})
    print(UVICORN_OPTIONS)
    set_config()
    uvicorn.run('server:fast_api_app', host=HOST, port=PORT, **UVICORN_OPTIONS)


if __name__ == "__main__":
    main()
