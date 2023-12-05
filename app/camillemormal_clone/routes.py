from app.camillemormal_clone import bp as camillemormal_clone
from flask import redirect, render_template

@camillemormal_clone.route("/")
def index():
    return render_template("camillemormal_clone.html")