from utils.dal import *

class RolesLogic:
    def __init__(self):
        self.dal = DAL()

    def close(self):
        self.dal.close()

