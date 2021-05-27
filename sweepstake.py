from contestant import Contestant
import random
import user_interface


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self):
        user_interface.registration()
        reg_number = input(user_interface.contestant_registration_number())
        first_name = input(user_interface.contestant_first_name())
        last_name = input(user_interface.contestant_last_name())
        email = input(user_interface.contestant_email())
        self.contestants[reg_number] = Contestant(first_name, last_name, email, reg_number)

    def registration(self):
        self.register_contestant()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.register_another_contestant()
            if user_option == 1:  #if yes continue to register
                self.register_contestant()
            elif user_option == 2:
                user_interface.clear_console()
                break
            else:
                will_proceed = False

    def pick_winner(self):
        #randomly pick winner and return contestant
        pass

    def print_contestant_info(self, contestant):
        #def print method in user interface and method here
        pass
