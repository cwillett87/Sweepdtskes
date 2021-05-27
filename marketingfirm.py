import sweepstakestackmanager
import user_interface
from sweepstake import Sweepstake
from sweepstakestackmanager import Sweepstake_stack_manager
from sweepstakesqueuemanager import Sweepstakes_queue_manager


class Marketing_firm:

    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

    # create sweepstakes with input name
    def create_sweepstakes(self):
        sweepstake_name = input(user_interface.name_sweepstakes())
        sweepstake = Sweepstake(sweepstake_name)
        sweepstake.registration()
        return sweepstake
