from logic.roles_logic import *

class RolesFacade:
    def __init__(self):
        self.logic = RolesLogic()
    
    def close(self):
        self.logic.close()


