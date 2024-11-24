from datetime import datetime
from flask import Blueprint, render_template, redirect, send_file, request, url_for, jsonify, session, make_response
from facades.vacations_facade import VacationsFacade
from models.error_model import *
from models.role_model import RoleModel
from utils.image_handler import ImageHandler
from utils.logger import Logger
from facades.countries_facade import CountriesFacade
from facades.users_facade import UsersFacade
from facades.likes_facade import LikesFacade
from models.status_code import StatusCode

vacations_blueprint = Blueprint("vacations_view", __name__)
facade = VacationsFacade()
country_facade = CountriesFacade()
users_facade = UsersFacade()
likes_facade = LikesFacade()


def format_date(date):
    return date.strftime("%d/%m/%Y")

vacations_blueprint.add_app_template_filter(format_date, "format_date")

@vacations_blueprint.route("/vacations", methods = ["GET", "POST"])
def all_vacations():
    try:
        users_facade.block_guest()
        user = session.get("current_user")
        all_vacations = facade.get_all_vacations_full_information()
        get_all_user_likes = likes_facade.get_likes_by_user(user["user_id"])
        Logger.get_log(get_all_user_likes)
        all_user_likes = [like["vacation_id"] for like in get_all_user_likes]
            
        error = request.args.get("error")
        admin_action = request.args.get("admin_action")
        return render_template("all_vacations.html", active = "vacations", vacations = all_vacations, 
                               admin_id = RoleModel.Admin.value, user_likes_vacations = all_user_likes, 
                               error = error, admin_action = admin_action) 
    except AuthenticationError as err:
        Logger.get_log(err.message)
        return redirect(url_for("users_view.login", error = err.message))
    except GetError as err:
        Logger.get_log(err.message)
        render = render_template("500_server_error.html", error = err.message)
        return make_response(render, StatusCode.InternalServerError.value)


@vacations_blueprint.route("/likes/<int:user_id>/<int:vacation_id>", methods = ["POST"])
def handle_likes(user_id, vacation_id):
    try:
        result = likes_facade.handel_like_unlike(user_id, vacation_id)
        return jsonify({"result": result})    
    except ValidationError as err:
        Logger.get_log(err.message)
        return jsonify({"error": err.message})


@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)


@vacations_blueprint.route("/vacations/new", methods = ["GET", "POST"])
def new_vacation():
    all_countries = country_facade.get_all_countries_orderby_name()
    try:
        users_facade.block_not_admin()
        if request.method == "GET": return render_template("add_new_vacation.html", vacation = {}, countries = all_countries)
        new_vacation_id = facade.add_new_vacation()
        return redirect(url_for("vacations_view.all_vacations", admin_action = f"Great job! New vacation (ID: {new_vacation_id}) just added successfully!🍋"))
    except AuthenticationError as err:
        Logger.get_log(err.message)
        render = render_template("home.html", error = err.message)
        return make_response(render, StatusCode.Forbidden.value)
    except ValidationError as err:
        Logger.get_log(err.message)
        render = render_template("add_new_vacation.html", error = err.message, vacation = err.model, countries = all_countries)
        return make_response(render, StatusCode.BadRequest.value)
    

@vacations_blueprint.route("/vacations/update/<int:id>", methods = ["GET", "POST"])
def update_vacation(id):
    all_countries = country_facade.get_all_countries_orderby_name()
    try:
        users_facade.block_not_admin()
        if request.method == "GET": 
            one_vacation = facade.get_one_vacation(id)
            return render_template("update_vacation.html", vacation = one_vacation, countries = all_countries)
        facade.update_vacation(id)
        return redirect(url_for("vacations_view.all_vacations", admin_action = f"Great job! You updated vacation ID {id} successfully!🍋"))
    except AuthenticationError as err:
        Logger.get_log(err.message)
        render = render_template("home.html", error = err.message)
        return make_response(render, StatusCode.Forbidden.value)
    except SourceNotFoundError as err:
        Logger.get_log(err.message)
        render = render_template("404_page_not_found.html", error = err.message)
        return make_response(render, StatusCode.NotFound.value)
    except ValidationError as err:
        Logger.get_log(err.message)
        render = render_template("update_vacation.html", error = err.message, vacation = err.model, countries = all_countries)
        return make_response(render, StatusCode.BadRequest.value)


@vacations_blueprint.route("/vacations/delete/<int:id>")
def delete_vacation(id):
    try:
        users_facade.block_not_admin()
        facade.delete_vacation(id)
        return redirect(url_for("vacations_view.all_vacations", admin_action = f"You deleted vacation (ID: {id}) successfully!🍋"))
    except AuthenticationError as err:
        Logger.get_log(err.message)
        render = render_template("home.html", error = err.message)
        return make_response(render, StatusCode.Forbidden.value)
    except SourceNotFoundError as err:
        Logger.get_log(err.message)
        render = render_template("404_page_not_found.html", error = err.message)
        return make_response(render, StatusCode.NotFound.value)


@vacations_blueprint.route("/vacations/<int:id>")
def one_vacation(id):
    try:
        users_facade.block_guest()
        one_vacation = facade.get_one_vacation(id)
        image_name = one_vacation["image_name"]
        check_image_name = ImageHandler.image_name_by_path(image_name)
        if check_image_name == "no-image.jpg": image_name = "no-image.jpg"
        return render_template("vacation_info.html", vacation = one_vacation)
    except AuthenticationError as err:
        Logger.get_log(err.message)
        return redirect(url_for("users_view.login", error = err.message))
    except SourceNotFoundError as err:
        Logger.get_log(str(err.message))
        render = render_template("404_page_not_found.html", error = err.message)
        return make_response(render, StatusCode.NotFound.value)








