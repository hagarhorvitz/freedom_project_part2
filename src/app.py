from flask import Flask, render_template
from views.home_view import home_blueprint
from views.users_view import users_blueprint
from views.vacations_view import vacations_blueprint
from views.counties_view import countries_blueprint
from views.contact_view import contact_blueprint
from views.api_view import api_blueprint
from utils.app_config import AppConfig
from utils.logger import Logger
from models.status_code import StatusCode

app = Flask(__name__)

app.secret_key = AppConfig.session_secret_key

app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(contact_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(StatusCode.NotFound.value)
def page_not_found(error):
    Logger.get_log(error)
    return render_template("404_page_not_found.html", error = error), StatusCode.NotFound.value


@app.errorhandler(Exception)
def catch_all_error(error):
    Logger.get_log(error)
    return render_template("500_server_error.html", error = error), StatusCode.InternalServerError.value


