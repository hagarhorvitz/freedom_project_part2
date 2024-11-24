from datetime import datetime

class VacationsModel:
    def __init__(self, vacation_id, country_id, description, start_date, end_date, price, image_name):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.image_name = image_name

    
    def validate_add_new_vacation(self):
        if not self.country_id: return "Please select country"
        if not self.description: return "Please enter vacation description"
        if not self.start_date: return "Please select start date"
        if not self.end_date: return "Please select end date"
        if not self.price: return "Please enter price"
        if not self.image_name: return "Please select image"
        if len(self.description) < 5 or len(self.description) > 250: return "Ensure the vacation description is between 5 and 250 characters"
        today = datetime.today().date()
        start = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        end = datetime.strptime(self.end_date, "%Y-%m-%d").date()
        if start < today: return "The start date cannot be a past date"
        if end < start: return "The end date cannot be before the start date"
        if end < today: return "The end date cannot be a past date"
        if int(self.price) < 0 or int(self.price) > 10000: return "Please enter a vacation price between 0 and 10,000 nis"
        return None
        

    def validate_update(self):
        if not self.country_id: return "Please select country"
        if not self.description: return "Please enter vacation description"
        if not self.start_date: return "Please select start date"
        if not self.end_date: return "Please select end date"
        if not self.price: return "Please enter price"
        if len(self.description) < 5 or len(self.description) > 250: return "Please ensure the vacation description is up to the maximum length possible"
        start = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        end = datetime.strptime(self.end_date, "%Y-%m-%d").date()
        if end < start: return "The end date cannot be before the start date"
        if int(self.price) < 0 or int(self.price) > 10000: return "Please enter a vacation price between 0 and 10,000 nis"
        return None
        
