from email_validator import validate_email, EmailNotValidError

from models.role_model import RoleModel

class UsersModel:
    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id


    def validate_register(self):
        if not self.first_name: return "Please enter first name"
        if not self.last_name: return "Please enter last name"
        if not self.email: return "Please enter email"
        if not self.password: return "Please enter password"
        if len(self.first_name) < 2 or len(self.first_name) > 45: return "Please ensure you entered first name between 2 to 45 characters long"
        if len(self.last_name) < 2 or len(self.last_name) > 45: return "Please ensure you entered last name between 2 to 45 characters long"
        if len(self.email) < 5 or len(self.email) > 60: return "Please ensure you entered an email between 5 to 60 characters long"
        if len(self.password) < 4 or len(self.password) > 20: return "Please ensure you entered a password between 4 to 20 characters long"
        if self.role_id != RoleModel.Admin.value and self.role_id != RoleModel.User.value: return "invalid role id"
        try:
            validate_email(self.email)
        except EmailNotValidError as e:
            print(f"Email validation failed: {e}") 
            return "invalid email, please try again"
        return None
    


    
class CredentialModel:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    
    def validate_login(self):
        if not self.email: return "Please enter email"
        if not self.password: return "Please enter password"
        if len(self.email) < 5 or len(self.email) > 60: return "Please ensure you entered an email that is up to the maximum length possible"
        if len(self.password) < 4: return "Please ensure you entered password between the length range"
        try:
            validate_email(self.email)
        except EmailNotValidError as e:
            print(f"Email validation failed: {e}") 
            return "invalid email, please try again"
        return None
    

    
    


    
    

    

    





    






