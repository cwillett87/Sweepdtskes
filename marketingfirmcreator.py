import user_interface
from marketingfirm import Marketing_firm
from sweepstakestackmanager import Sweepstake_stack_manager
from sweepstakesqueuemanager import Sweepstakes_queue_manager


class marketingFirmCreator:

    def __init__(self):
        self.choose_manager_type()

    def choose_manager_type(self):
        will_proceed = True
        while will_proceed:
            firm_name = input(user_interface.name_firm())
            user_option = user_interface.marketing_firm_menu()
            if user_option == 1:  # create stack manager
                stack_manager = Sweepstake_stack_manager()
                firm = Marketing_firm(firm_name, stack_manager)  # create firm with name input
                sweepstake = firm.create_sweepstakes()
                stack_manager.insert_sweepstakes(sweepstake)
                return firm
            elif user_option == 2:  # create queue manager
                queue_manager = Sweepstakes_queue_manager()
                firm = Marketing_firm(firm_name, queue_manager)  # create firm with name input
                sweepstake = firm.create_sweepstakes()
                queue_manager.insert_sweepstakes(sweepstake)
                return firm
            else:
                will_proceed = False
