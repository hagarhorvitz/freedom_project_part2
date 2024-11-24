from utils.dal import *
from utils.image_handler import ImageHandler

class VacationsLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT * FROM freedom.vacations" 
        return self.dal.get_table(sql)
    
    def get_all_vacations_by_start_date(self):
        sql = "SELECT * FROM freedom.vacations ORDER BY start_date" 
        return self.dal.get_table(sql)

    def get_all_vacations_by_startDate_w_countryName(self):
        sql = "SELECT vacations.*, countries.country_name FROM freedom.vacations join freedom.countries on vacations.country_id = countries.country_id ORDER BY start_date"
        return self.dal.get_table(sql)
    

    def get_all_vacations_by_startDate_w_countryName_likes(self):
        sql = "SELECT vacations.*, countries.country_name, COUNT(likes.vacation_id) AS count_likes FROM freedom.vacations LEFT JOIN freedom.countries ON vacations.country_id = countries.country_id LEFT JOIN freedom.likes ON vacations.vacation_id = likes.vacation_id GROUP BY vacations.vacation_id, countries.country_name ORDER BY start_date"
        return self.dal.get_table(sql)



    def get_one_vacation(self, id):
        sql = "SELECT * FROM freedom.vacations WHERE vacation_id = %s"
        return self.dal.get_scalar(sql, (id, ))
    
    def get_one_vacation_w_country_name(self, id):
        sql = "SELECT vacations.*, countries.country_name FROM freedom.vacations join freedom.countries on vacations.country_id = countries.country_id WHERE vacation_id = %s"
        return self.dal.get_scalar(sql, (id, ))


    def insert_new_vacation(self, vacation): ## send vacation object ##
        image_name = ImageHandler.save_image_on_disk(vacation.image_name)
        sql = "INSERT INTO freedom.vacations (country_id, description, start_date, end_date, price, image_name) VALUES (%s,%s,%s,%s,%s,%s)"
        return self.dal.insert(sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, image_name))
  
            
    def update_vacation(self, vacation): ## send vacation object ##
        current_image_name = self.get_current_image_name(vacation.vacation_id)
        image_name = ImageHandler.update_image_in_disk(current_image_name, vacation.image_name)
        sql = "UPDATE freedom.vacations SET country_id = %s, description = %s, start_date = %s, end_date = %s, price = %s, image_name = %s WHERE vacation_id = %s"
        return self.dal.update(sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, image_name, vacation.vacation_id))


    def get_current_image_name(self, id):
        sql = "SELECT image_name FROM freedom.vacations WHERE vacation_id = %s"
        image_name = self.dal.get_scalar(sql, (id, ))
        return image_name["image_name"]


    def delete_vacation(self, id):
        sql = "DELETE FROM freedom.vacations WHERE vacation_id = %s"
        return self.dal.delete(sql, (id, ))
        
    
    def close(self):
        self.dal.close()




