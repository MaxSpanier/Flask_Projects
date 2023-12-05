from flask import Blueprint

bp = Blueprint("navbar_hacking", __name__, url_prefix="/navbar_hacking", static_folder="static", static_url_path="static", template_folder="templates")

from app.navbar_hacking import routes
