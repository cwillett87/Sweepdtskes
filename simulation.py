import user_interface
from marketingfirm import Marketing_firm
from marketingfirmcreator import Marketing_firm_creator


class Simulation:

    def __init__(self):
        self.run_simulation()

    def run_simulation(self):
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1: #if yes please name the marketing firm
                firm_name = input(user_interface.name_firm())
                name = Marketing_firm_creator(firm_name)#create firm with name input
                name.choose_manager_type()
            elif user_option == 2:
                user_interface.clear_console()
            else:
                will_proceed = False
