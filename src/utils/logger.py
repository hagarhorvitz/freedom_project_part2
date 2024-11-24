from datetime import datetime

from flask import session

class Logger:
    __log_file_path = "./logger.log"

    @staticmethod
    def get_log(message):
        now = datetime.now()
        with open(Logger.__log_file_path, "a") as file:
            file.write(str(now) + "\n")
            file.write(str(message) + "\n")
            file.write(f"{"-"*30}\n")
            user = session.get("current_user")
            if user:
                file.write(f"User Id: {user["user_id"]}\nName: {user["first_name"]} {user["last_name"]}\nEmail: {user["email"]}\n") 
            file.write(f"{"*"*35}\n")

