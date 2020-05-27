from threading import Thread
import cv2

class ThreadedCamera(Thread):
    """
    Deamon for capture camera using threading.
    Works better.
    You get frames using grab_frame functions
    """
    def __init__(self, source):
        super().__init__()
        
        self.capture = cv2.VideoCapture(source)
        self.daemon = True
        self.start()

        self.status = False
        self.frame  = None
        
    def run(self):
        print("Thread camera started.")
        while True:
            if self.capture.isOpened():
                self.status, self.frame = self.capture.read()

    def grab_frame(self):
        if self.status:
            return self.frame
        return None

    def get_frame_dimentions(self):
        return (
            int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
