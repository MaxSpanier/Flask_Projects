from app.navbar_hacking import bp as navbar_hacking
from flask import redirect, current_app, render_template

@navbar_hacking.route("/")
def index():
    return render_template("navbar_hacking.html")

