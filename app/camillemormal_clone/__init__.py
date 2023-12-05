from flask import Blueprint

bp = Blueprint("camillemormal_clone", __name__, url_prefix="/camillemormal_clone", static_folder="static", static_url_path="static", template_folder="templates")

from app.camillemormal_clone import routes