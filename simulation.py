import user_interface

from marketingfirmcreator import marketingFirmCreator


class Simulation:

    def __init__(self):
        self.run_simulation()

    def run_simulation(self):
        # firm_name = input(user_interface.name_firm())
        marketingFirmCreator()
        # firm = Marketing_firm(firm_name, manager)#create firm with name input
        # firm.create_sweepstakes()
