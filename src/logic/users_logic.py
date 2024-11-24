from utils.dal import DAL

class UsersLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_users(self):
        sql = "SELECT * FROM freedom.users" 
        return self.dal.get_table(sql)

    def get_one_user(self, id):
        sql = "SELECT * FROM freedom.users WHERE user_id = %s"
        return self.dal.get_scalar(sql, (id, ))


    def insert_new_user(self, user): ## send user object ##
        sql = "INSERT INTO freedom.users (first_name, last_name, email, password, role_id) VALUES (%s,%s,%s,%s,%s)"
        return self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password, user.role_id))

    
    def if_email_exists(self, email):
        sql = "SELECT exists(SELECT * FROM freedom.users WHERE email = %s) as email_is_exists"
        output = self.dal.get_scalar(sql, (email, ))
        return output["email_is_exists"] == 1 ## 1 = true / 0 = false
        
    def get_user_by_email_and_password(self, credentials): ## send credentials object ##
        sql = "SELECT * FROM freedom.users WHERE email = %s and password = %s"
        user = self.dal.get_scalar(sql, (credentials.email, credentials.password))
        return user
        

    def close(self):
        self.dal.close()
        







