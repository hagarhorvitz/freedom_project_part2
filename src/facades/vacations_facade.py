from flask import request
from logic.vacations_logic import *
from utils.image_handler import ImageHandler
from models.error_model import *
from models.vacations_model import VacationsModel

class VacationsFacade:
    def __init__(self):
        self.logic = VacationsLogic()

    def get_all_vacations_basic(self):
        return self.logic.get_all_vacations()

    def get_all_vacations_full_information(self):
        return self.logic.get_all_vacations_by_startDate_w_countryName_likes()
    
    def get_all_vacations_by_startDate_w_countryName(self):
        return self.logic.get_all_vacations_by_startDate_w_countryName()

    
    def get_one_vacation(self, id):
        vacation = self.logic.get_one_vacation_w_country_name(id)
        if not vacation: raise SourceNotFoundError(id)
        return vacation


    def add_new_vacation(self):
        country_id = request.form.get("country_id")
        description = request.form.get("description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files["image"]
        new_vacation = VacationsModel(None, country_id, description, start_date, end_date, price, image)
        error = new_vacation.validate_add_new_vacation()
        if error: raise ValidationError(error, new_vacation) 
        return self.logic.insert_new_vacation(new_vacation)
      
 
    def update_vacation(self, vacation_id):
        if not vacation_id: raise SourceNotFoundError(vacation_id)
        country_id = request.form.get("country_id")
        description = request.form.get("description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files["image"]
        vacation = VacationsModel(vacation_id, country_id, description, start_date, end_date, price, image)
        error = vacation.validate_update()
        if error: 
            old_image_name = self.logic.get_current_image_name(vacation_id)
            current_vacation = VacationsModel(vacation_id, country_id, description, start_date, end_date, price, old_image_name)
            raise ValidationError(error, current_vacation)
        self.logic.update_vacation(vacation)


    def delete_vacation(self, id):
        if not id: raise SourceNotFoundError(id)
        image_name = self.logic.get_current_image_name(id)
        ImageHandler.delete_image_from_disk(image_name)
        self.logic.delete_vacation(id)
        

    def close(self):
        self.logic.close()


    
