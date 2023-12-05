from flask import Blueprint

bp = Blueprint("main", __name__, static_folder="static", url_prefix="/main")

from app.main import routes
