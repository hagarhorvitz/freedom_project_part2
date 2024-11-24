
class CountriesModel:
    def __init__(self, country_id, country_name):
        self.country_id = country_id
        self.country_name = country_name


    def validate_add_new_country(self):
        if not self.country_name: return "Please enter valid country name"
        if len(self.country_name) < 2 or len(self.country_name) > 100: return "The country name should be up to 100 letters long"
        return None





