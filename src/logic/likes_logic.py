from utils.dal import *


class LikesLogic:
    def __init__(self):
        self.dal  = DAL()

    def get_all_likes_to_all_vacations(self):
        sql = "SELECT vacation_id, count(*) as count_likes_for_vacation FROM freedom.likes GROUP BY vacation_id"
        return self.dal.get_table(sql) #returns vacation and number of likes
    

    def get_likes_by_vacation_id(self, vacation_id):
        sql = "SELECT count(*) as total_likes FROM freedom.likes WHERE vacation_id = %s"
        result = self.dal.get_scalar(sql, (vacation_id,))
        return result["total_likes"] # returns number of likes for a vacation


    def get_all_likes_by_user_id(self, id):
        sql = "SELECT * FROM freedom.likes WHERE user_id = %s"
        return self.dal.get_table(sql, (id, ))
    
    

    def get_likes(self, like): ## send like object ##
        sql = "SELECT * FROM freedom.likes WHERE user_id = %s and vacation_id=%s"
        return self.dal.get_table(sql, (like.user_id, like.vacation_id))

    

    def add_new_like(self, like):  ## send like object ##
        sql = "INSERT INTO freedom.likes (user_id, vacation_id) VALUES (%s,%s)"
        return self.dal.insert(sql, (like.user_id, like.vacation_id))
   

    def delete_like(self, like):  ## send like object ##
        sql = "DELETE FROM freedom.likes WHERE user_id = %s and vacation_id = %s"
        return self.dal.delete(sql, (like.user_id, like.vacation_id))
    
    
    def check_like_exists(self, like): ## send like object ##
        sql = "SELECT exists(SELECT * FROM freedom.likes WHERE user_id = %s and vacation_id = %s) as is_likes"
        result = self.dal.get_scalar(sql, (like.user_id, like.vacation_id))
        return result["is_likes"] == 1

   
    def close(self):
        self.dal.close()

    


