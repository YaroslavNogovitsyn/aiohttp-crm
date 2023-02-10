import typing

from app.crm.routes import setup_routes as crm_setup_routes
if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    crm_setup_routes(app)
