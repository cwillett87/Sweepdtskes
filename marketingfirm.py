import user_interface
from sweepstake import Sweepstake
import marketingfirmcreator


class Marketing_firm:

    def __init__(self, name):
        self.name = name
        self.manager = marketingfirmcreator.choose_manager_type()

    # create sweepstakes with input name
    def create_sweepstakes(self):
        will_proceed = True
        while will_proceed:
            user_option = user_interface.sweepstakes_menu()
            if user_option == 1:
                sweepstake_name = input(user_interface.name_sweepstakes())
                Sweepstake(sweepstake_name)
            elif user_option == 2:
                user_interface.clear_console()
            else:
                will_proceed = False
