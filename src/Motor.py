import requests
from threading import Thread
from time import sleep


class Motor:
    """ 
    Control the motor using http request
    with Threading.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.MOTOR_LOCK = False


        """ 
        pan forward: left 
        pan reverse: right
        tilt forward: up
        tilt reverse: down
        """

        self.pan = "pan"
        self.tilt = "tilt"
        self.forward = "forward"
        self.reverse = "reverse"




    def _move(self, motor, direction, steps):
        response = requests.get("http://{}:{}/motor_move/{}/{}/{}".format(self.host, self.port, motor, direction, steps))
        sleep(1)
        self.MOTOR_LOCK = False
        return response.text == "max" # MAX offset

    def motor_move(self, motor, direction, steps):
        if not self.MOTOR_LOCK:
            self.MOTOR_LOCK = True
            print("Moving motor {} {} {} steps".format(motor, direction, steps))
            Thread(target=self._move, args=(motor, direction, steps)).start()

