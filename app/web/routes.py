from app.crm.routes import setup_routes as crm_setup_routes
from app.web.app import Application


def setup_routes(app: Application):
    crm_setup_routes(app)
