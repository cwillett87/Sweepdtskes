import user_interface
from sweepstake import Sweepstake


class Marketing_firm:

    def __init__(self, name, manager): # dependency injection
        self.name = name
        self.manager = manager # works no matter which manager is used

    # create sweepstakes with input name
    def create_sweepstakes(self):
        sweepstake_name = input(user_interface.name_sweepstakes())
        sweepstake = Sweepstake(sweepstake_name)
        sweepstake.registration()
        return sweepstake
