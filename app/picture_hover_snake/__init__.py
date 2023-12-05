from flask import Blueprint

bp = Blueprint("picture_hover_snake", __name__, template_folder="templates", static_folder="static", static_url_path="static", url_prefix="/picture_hover_snake")

from app.picture_hover_snake import routes