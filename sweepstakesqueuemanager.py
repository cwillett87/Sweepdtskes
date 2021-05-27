from data_queue import Queue

class Sweepstakes_queue_manager:

    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)

    def get_sweepstakes(self):
        return Queue.dequeue()
