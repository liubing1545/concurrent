from Queue import Queue
from functools import partial

eventloop = None

class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()
            
def save_value(value, callback):
    print "Saving {} to database".format(value)
    #save_result_to_db(result, callback)
    save_result_to_db(callback)

def save_result_to_db(callback):
    callback("test")
    
def print_response(db_response):
    print "Response from database: {}".format(db_response)

if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(
        partial(save_value, "Hello World", print_response)
        )
    eventloop.start()
