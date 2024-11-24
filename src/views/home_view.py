import random
from flask import Blueprint, jsonify, render_template, request, send_file, make_response
from facades.vacations_facade import VacationsFacade
from models.error_model import GetError
from models.status_code import StatusCode
from utils.image_handler import ImageHandler
from utils.logger import Logger

home_blueprint = Blueprint("home_view", __name__)

vacations_facade = VacationsFacade()

@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    try:
        vacations = vacations_facade.get_all_vacations_basic()
        vacations_id = [vacation_id["vacation_id"] for vacation_id in vacations]
        random_number = random.randint(0, len(vacations_id)-1)
        clicked = request.args.get("clicked")
        main_images = ImageHandler.get_home_images_list() 
        return render_template("home.html", active = "home", clicked = clicked, images = main_images, 
                               id_list = vacations_id, random_index = random_number)
    except GetError as err:
        Logger.get_log(err.message)
        render = render_template("500_server_error.html", error = err.message)
        return make_response(render, StatusCode.InternalServerError.value)
    
@home_blueprint.route("/home/image/<string:image_name>")
def get_home_image(image_name):
    image_path = ImageHandler.get_home_image_path(image_name)
    return send_file(image_path)


@home_blueprint.route("/home/images", methods = ["GET"])
def get_home_images_list():
    try:
        main_images = ImageHandler.get_home_images_list()
        return jsonify({"images": main_images})    
    except GetError as err:
        Logger.get_log(err.message)
        return jsonify({"error": err.message})
    






