import uvicorn

from fastapi import FastAPI
from conf.server_conf import *


app = FastAPI()


@app.get("/")
def index():
    return "dd"


def main():
    # uvicorn_options = CONFIG.get('UVICORN_OPTIONS', {})
    print(UVICORN_OPTIONS)
    uvicorn.run('server:app', host=HOST, port=PORT, **UVICORN_OPTIONS)


if __name__ == "__main__":
    main()
