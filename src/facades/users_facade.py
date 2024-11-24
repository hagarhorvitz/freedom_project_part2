from flask import request, session
from logic.users_logic import UsersLogic
from models.users_model import *
from models.error_model import *
from models.role_model import RoleModel
from utils.cyber_hash import CyberHash


class UsersFacade:
    def __init__(self):
        self.logic = UsersLogic()

    def register_new_user(self):
        first_name = request.form.get("first_name").capitalize()
        last_name = request.form.get("last_name").capitalize()
        email = request.form.get("email")
        password = request.form.get("password") 
        new_user = UsersModel(None, first_name, last_name, email, password, RoleModel.User.value)
        error = new_user.validate_register()
        if error: raise ValidationError(error, new_user)
        if self.logic.if_email_exists(email): raise AuthenticationError("Email is already exist in the system", new_user)
        new_user.password = CyberHash.hash(new_user.password)
        self.logic.insert_new_user(new_user)
        return "OK"

    def login_user(self):
        email = request.form.get("email")
        password = request.form.get("password") 
        credentials = CredentialModel(email, CyberHash.hash(password))
        error = credentials.validate_login()
        if error: raise ValidationError(error, credentials)
        user = self.logic.get_user_by_email_and_password(credentials)
        if not user: raise AuthenticationError("Incorrect email or password", credentials)
        del user["password"] ##delete from session dictionary the password key
        session["current_user"] = user

    def logout(self):
        session.clear()

    
    def block_guest(self):
        user = session.get("current_user")
        if not user: raise AuthenticationError("Only registered members can proceed to this page, please make a login")


    def block_not_admin(self):
        user = session.get("current_user")
        if not user: raise AuthenticationError("Only registered members can proceed to this page, please make a login")
        if user["role_id"] != RoleModel.Admin.value: raise AuthenticationError("Action authorized for admin only")


    def close(self):
        self.logic.close()
