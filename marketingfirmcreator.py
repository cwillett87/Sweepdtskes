import user_interface
from sweepstakestackmanager import Sweepstake_stack_manager
from sweepstakesqueuemanager import Sweepstakes_queue_manager


def choose_manager_type(self):
    will_proceed = True
    while will_proceed:
        user_option = user_interface.marketing_firm_menu()
        if user_option == 1:  # create stack manager
            Sweepstake_stack_manager()
        elif user_option == 2:  # create queue manager
            Sweepstakes_queue_manager()
        else:
            will_proceed = False
