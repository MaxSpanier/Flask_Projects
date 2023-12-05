from app.picture_hover_snake import bp as picture_hover_snake
from flask import redirect, render_template

@picture_hover_snake.route("/")
def index():
    return render_template("picture_hover_snake.html")