from flask import Blueprint, jsonify, make_response
from facades.vacations_facade import VacationsFacade
from facades.likes_facade import LikesFacade
from models.error_model import *
from utils.logger import Logger
from models.status_code import StatusCode

api_blueprint = Blueprint("api_view", __name__)

vacation_facade = VacationsFacade()
likes_facade = LikesFacade()


@api_blueprint.route("/api/vacations")
def vacations():
    try:
        all_vacations = vacation_facade.get_all_vacations_full_information()
        return jsonify(all_vacations)
    except GetError as err:
        Logger.get_log(err.message)
        render_json = jsonify({"Sever Error": err.message})
        return make_response(render_json, StatusCode.InternalServerError.value)


@api_blueprint.route("/api/vacations/<int:id>")
def one_vacation(id):
    try:
        one_vacation = vacation_facade.get_one_vacation(id)
        return jsonify(one_vacation)
    except SourceNotFoundError as err:
        Logger.get_log(err.message)
        render_json = jsonify({"Source Not Found Error": err.message})
        return make_response(render_json, StatusCode.NotFound.value)
    







