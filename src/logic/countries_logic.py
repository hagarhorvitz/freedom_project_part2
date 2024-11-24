from utils.dal import *

class CountriesLogic:
    def __init__(self):
        self.dal  = DAL()

    def get_all_countries(self):
        sql = "SELECT * FROM freedom.countries" 
        return self.dal.get_table(sql)

    def get_all_countries_orderby_name(self):
        sql = "SELECT * FROM freedom.countries ORDER BY country_name" 
        return self.dal.get_table(sql)

        
    def get_one_country_name(self, id):
        sql = "SELECT country_name FROM freedom.countries WHERE country_id = %s"
        return self.dal.get_scalar(sql, (id, ))
        

    def insert_new_county(self, new_country):
        sql = "INSERT INTO freedom.countries (country_name) VALUES (%s)"
        return self.dal.insert(sql, (new_country.country_name, ))
    

    def is_country_name_exists(self, country_name):
        sql = "SELECT exists(SELECT * FROM freedom.countries WHERE country_name = %s) as country_name_exists"
        output = self.dal.get_scalar(sql, (country_name, ))
        return output["country_name_exists"] == 1 ## 1 = true / 0 = false


    def close(self):
        self.dal.close()
