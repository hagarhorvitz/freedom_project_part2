from flask import Blueprint, request, render_template, redirect, url_for, make_response, jsonify
from facades.users_facade import UsersFacade
from models.error_model import *
from utils.logger import Logger
from models.status_code import StatusCode

users_blueprint = Blueprint("users_view", __name__)
facade = UsersFacade()


@users_blueprint.route("/register", methods = ["GET", "POST"])
def register():
    try:
        if request.method == "GET":
            return render_template("register.html", active = "register", new_user = {}) 
        register = facade.register_new_user()
        if register == "OK":
            facade.login_user()
        return redirect(url_for("home_view.home", clicked = "You just register successfully! Welcome to the club 🍋"))
    except (ValidationError, AuthenticationError) as err:
        Logger.get_log(err.message)
        render = render_template("register.html", active = "register", error = err.message, new_user = err.model)
        return make_response(render, StatusCode.Unauthorized.value)


@users_blueprint.route("/login", methods = ["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            error = request.args.get("error")
            render = render_template("login.html", active = "login", error = error, credentials = {})
            if error:
                response = make_response(render, StatusCode.Unauthorized.value)
                return response
            return render
        facade.login_user()
        return redirect(url_for("home_view.home", clicked = "Login successfully! Have fun 🍋"))
    except (ValidationError, AuthenticationError) as err:
        Logger.get_log(err.message)
        render = render_template("login.html", active = "login", error = err.message, credentials = err.model, json = jsonify({"error": err.message}))
        return make_response(render, StatusCode.Unauthorized.value)


@users_blueprint.route("/logout") ## default is "GET" so no need methods
def logout():
    facade.logout()
    return redirect(url_for("home_view.home", clicked = "Logged out successfully! See you next time🍋"))
