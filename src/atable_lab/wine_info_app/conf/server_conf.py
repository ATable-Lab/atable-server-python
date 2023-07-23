PORT = 8080
UVICORN_OPTIONS = {}
HOST = '0.0.0.0'


DATABASE = {
    'mongo_db': {
        'host': 'localhost',
        'port': 27017,
        'database': 'wine_info',
        'collection': 'wine_info'
    }
}
