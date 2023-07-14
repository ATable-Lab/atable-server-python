import click
import uvicorn
import os

@click.command()
@click.option('--host', '-h', default='0.0.0.0', help='Host')
@click.option('--port', '-p', default=8080, help='Port')
@click.option('--application', '-app', default='wine_info_app', help='Application')
def run_app(**params):

    host = params.get('host', os.environ.get('HOST'))
    port = params.get('port', os.environ.get('PORT'))
    # uvicorn_options = params.get('uvicorn_options', os.environ.get('UVICORN_OPTIONS'))
    app = params.get('application', os.environ.get('APPLICATION'))

    uvicorn.run(f'atable_lab.{app}.server:fast_api_app', factory=True, host=host, port=port)


if __name__ == '__main__':
    run_app()
