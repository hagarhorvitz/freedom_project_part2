from flask import request
from logic.countries_logic import *
from models.error_model import *
from models.countries_model import CountriesModel

class CountriesFacade:
    def __init__(self):
        self.logic = CountriesLogic()

    def get_all_countries(self):
        return self.logic.get_all_countries()
    

    def get_all_countries_orderby_name(self):
        return self.logic.get_all_countries_orderby_name()
    

    def add_new_country(self):
        country_name = request.form.get("country_name").capitalize()
        new_country = CountriesModel(None, country_name)
        error = new_country.validate_add_new_country()
        if error: raise ValidationError(error, new_country)
        if self.logic.is_country_name_exists(country_name): raise ValidationError("This country is already exist in the system", new_country)
        self.logic.insert_new_county(new_country)
        return country_name


    def close(self):
        self.logic.close()
