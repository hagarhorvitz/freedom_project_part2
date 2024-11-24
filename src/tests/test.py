from facades.users_facade import *
from facades.vacations_facade import *
from facades.likes_facade import *
from facades.countries_facade import *
from facades.roles_facade import *

class Test:
    def __init__(self):
        self.users_facade = UsersFacade()
        self.vacations_facade = VacationsFacade()
        self.likes_facade = LikesFacade()
        self.countries_facade = CountriesFacade()
        self.roles_facade = RolesFacade()
    
    def add_new_user_test(self):
        print(f"{"-"*20} ADD NEW USER {"-"*20}")
        try:
            args = ("first", "last", "test@gmail.com", "test123", 2)
            if len(args) != 5:
                raise ValueError("Please provide all required information")
            new_user = self.users_facade.register_new_user(*args)
            print(new_user)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)


    def login_user_test(self):
        try:
            args = ("hagar@gmail.com", "shraga12345")
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            user_roleId, message = self.users_facade.login_exists_user(*args)
            print(message)
            return user_roleId
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)


    def get_all_vacations_by_startDate_test(self):
        print(f"{"-"*20} ALL VACATIONS ORDERED BY START DATE {"-"*20}")
        try:
            args = ["startDate"]
            if len(args) != 1:
                raise ValueError("Please provide all required information")
            all_vacations = self.vacations_facade.all_vacations_ordered(*args)
            print(all_vacations)
        except ValueError as err:
            print("Value error:", err)
        except TypeError as err:
            print("Type error:", err)
        except Exception as err:
            print("General error:", err)

        
    def add_new_vacation_test(self):
        print(f"{"-"*20} ADD NEW VACATION {"-"*20}")
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            print(f"{"*"*40}")
            try:
                args = (1, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD", 14500, "photoFileName")
                if len(args) != 6:
                    raise ValueError("Please provide all required information")
                new_vacation = self.vacations_facade.add_new_vacation(*args)
                print(new_vacation)
            except ValueError as err:
                print("Value error:", err)
            except TypeError as err:
                print("Type error:", err)
            except Exception as err:
                print("General error:", err)


    def update_vacation_test(self):
        print(f"{"-"*20} UPDATE VACATION {"-"*20}")
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            print(f"{"*"*40}")
            try:
                args = (6, "vacationInfo", "startDate YYYY-MM-DD", "endDate YYYY-MM-DD", 100, 2)
                if len(args) != 6:
                    raise ValueError("Please provide all required information")
                vacation = self.vacations_facade.update_exist_vacation(*args)
                print(vacation)
            except ValueError as err:
                print("Value error:", err)
            except TypeError as err:
                print("Type error:", err)
            except Exception as err:
                print("General error:", err)


    def delete_vacation_test(self):
        print(f"{"-"*20} DELETE VACATION {"-"*20}")
        permission = self.login_user_test()
        if permission == False:
            print(f"{"*"*40}\nAccess denied!\nUser is not authorized for this action\n{"*"*40}")
        elif permission == True:
            print(f"{"*"*40}")
            try:
                args = [3]
                if len(args) != 1:
                    raise ValueError("Please provide all required information")
                delete_vacation = self.vacations_facade.delete_vacation(*args)
                print(delete_vacation)
            except ValueError as err:
                print("Value error:", err)
            except TypeError as err:
                print("Type error:", err)
            except Exception as err:
                print("General error:", err)


    def add_like_test(self):
        print(f"{"-"*20} ADD LIKE {"-"*20}")
        try:
            args = (3, 2)
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            like = self.likes_facade.add_new_like(*args)
            print(like)
        except ValueError as err:
            print("Value error:", err)
        except Exception as err:
            print("General error:", err)


    def unlike_vacation_test(self):
        print(f"{"-"*20} UNLIKE {"-"*20}")
        try:
            args = (35, 15)
            if len(args) != 2:
                raise ValueError("Please provide all required information")
            unlike = self.likes_facade.unlike_vacation(*args)
            print(unlike)
        except ValueError as err:
            print("Value error:", err)
        except Exception as err:
            print("General error:", err)


    def test_all(self):
        self.add_new_user_test()
        print(f"{"-"*20} LOGIN USER {"-"*20}")
        self.login_user_test()
        self.get_all_vacations_by_startDate_test()
        self.add_new_vacation_test()
        self.update_vacation_test()
        self.delete_vacation_test()
        self.add_like_test()
        self.unlike_vacation_test()
        self.close()


    def close(self):
        self.users_facade.close()
        self.vacations_facade.close()
        self.likes_facade.close()
        self.countries_facade.close()
        self.roles_facade.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()


