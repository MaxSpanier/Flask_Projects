from flask import Blueprint

bp = Blueprint("dashboard", __name__, url_prefix="", static_folder="static", static_url_path="dashboard/static", template_folder="templates")

from app.dashboard import routes
