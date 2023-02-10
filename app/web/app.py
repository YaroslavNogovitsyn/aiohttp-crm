from typing import Optional

from aiohttp.web import \
    Application as AiohttpApplication, \
    Request as AiohttpRequest, \
    View as AiohttpView, \
    run_app as aiohttp_run_app

from app.store import setup_accessor
from app.store.crm.accessor import CrmAccessor
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_routes(app)
    setup_accessor(app)
    aiohttp_run_app(app, host="127.0.0.1")
