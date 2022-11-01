from flask import Blueprint

from . import views

main_blueprint = Blueprint("api", __name__)

main_blueprint.add_url_rule(
    "/api",
    view_func= views.Main.as_view("main")
)