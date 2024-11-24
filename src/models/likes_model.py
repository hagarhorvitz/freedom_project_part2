class LikesModel:
    def __init__(self, user_id, vacation_id):
        self.user_id = user_id
        self.vacation_id = vacation_id


    def validate_like(self):
        if not self.user_id: return "No active user at the vacation card"
        if not self.vacation_id: return "No vacation id found"
        return None
    
