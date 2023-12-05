from app.main import bp as main
from flask import redirect, current_app, render_template

@main.route("/")
def index():
    return render_template("main/main.html")

