from flask import request
from logic.likes_logic import *
from models.likes_model import *
from models.error_model import *

class LikesFacade:
    def __init__(self):
        self.logic = LikesLogic()

    def get_all_likes_count_by_vacations(self):
        return self.logic.get_all_likes_to_all_vacations()
    
    def get_likes_by_user(self, user_id):
        return self.logic.get_all_likes_by_user_id(user_id)
    

    def get_likes_by_vacation_id(self, vacation_id):
        return self.logic.get_likes_by_vacation_id(vacation_id)
    
    def handel_like_unlike(self, user_id, vacation_id):
        like_unlike = LikesModel(user_id, vacation_id)
        error = like_unlike.validate_like()
        if error: raise ValidationError(error, like_unlike)
        if self.logic.check_like_exists(like_unlike):
            self.logic.delete_like(like_unlike)
            return "unlike"
        else:
            self.logic.add_new_like(like_unlike)
            return "like"
        

    def check_like_exists(self):
        user_id = request.form.get("user_id")
        vacation_id = request.form.get("vacation_id")
        check_like = LikesModel(user_id, vacation_id)
        error = check_like.validate_like()
        if error: raise ValidationError(error, check_like)
        if self.logic.check_like_exists(check_like):
            return True
        else:
            return False


    def close(self):
        self.logic.close()






