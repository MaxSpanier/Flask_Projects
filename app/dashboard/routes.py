from app.dashboard import bp as dashboard
from flask import redirect, current_app, render_template

@dashboard.route("/", methods=['GET', 'POST'])
@dashboard.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    projects_cards = []

    camillemormal_clone = {
        "title": "Carmille Mormal Clone",
        "description": "...",
        "link": "camillemormal_clone/",
    }

    navbar_hacking = {
        "title": "Navbar Hacking Effect",
        "description": "...",
        "link": "navbar_hacking",
    }

    picture_hover_snake = {
        "title": "Pictures that follow your cursor",
        "description": "...",
        "link": "picture_hover_snake",
    }

    projects_cards.append(camillemormal_clone)
    projects_cards.append(navbar_hacking)
    projects_cards.append(picture_hover_snake)

    return render_template("dashboard.html", cards = projects_cards)

