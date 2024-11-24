from flask import Blueprint, render_template, send_file, make_response
from models.error_model import GetError
from utils.logger import Logger
from models.status_code import StatusCode
from utils.image_handler import ImageHandler

contact_blueprint = Blueprint("contact_view", __name__)


@contact_blueprint.route("/contact")
def contact_us():
    try:
        return render_template("contact_us.html", active = "contact")
    except GetError as err:
        Logger.get_log(err.message)
        render = render_template("500_server_error.html", error = err.message)
        return make_response(render, StatusCode.InternalServerError.value)


@contact_blueprint.route("/contact/target")
def contact_target():
    try:
        return render_template("contact_us_target.html", active = "contact")
    except GetError as err:
        Logger.get_log(err.message)
        render = render_template("500_server_error.html", error = err.message)
        return make_response(render, StatusCode.InternalServerError.value)


@contact_blueprint.route("/contact/logo/<string:logo_image_name>")
def get_logo_image(logo_image_name):
    logo_image_path = ImageHandler.get_background_logo_path(logo_image_name)
    return send_file(logo_image_path)