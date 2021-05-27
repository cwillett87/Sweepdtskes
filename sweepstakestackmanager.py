from stack import Stack


class Sweepstake_stack_manager:

    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self):
        return Stack.pop()
