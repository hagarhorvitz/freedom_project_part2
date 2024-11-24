from flask import Blueprint, render_template, redirect, request, url_for, make_response
from facades.users_facade import UsersFacade
from models.error_model import *
from models.status_code import StatusCode
from utils.logger import Logger
from facades.countries_facade import CountriesFacade

countries_blueprint = Blueprint("countries_view", __name__)
facade = CountriesFacade()
users_facade = UsersFacade()


@countries_blueprint.route("/countries/new", methods = ["GET", "POST"])
def new_country():
    try:
        users_facade.block_not_admin()
        if request.method == "GET": return render_template("add_new_country.html", country = {})
        new_country_name = facade.add_new_country()
        return redirect(url_for("vacations_view.all_vacations", admin_action = f"New country ({new_country_name}) just added successfully!🍋"))
    except AuthenticationError as err:
        Logger.get_log(err.message)
        render = render_template("home.html", error = err.message)
        return make_response(render, StatusCode.Forbidden.value)
    except ValidationError as err: 
        Logger.get_log(err.message)
        render = render_template("add_new_country.html", error = err.message, country = err.model)
        return make_response(render, StatusCode.BadRequest.value)
