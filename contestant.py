class Contestant:

    def __init__(self, first, last, email, number):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.reg_number = int(number)

    def notify(self):
        #notifys winner calling method from user interface
        pass
