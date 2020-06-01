#!/usr/bin/python3

from ThreadedCamera import ThreadedCamera # for capturing frames
from ObjDetection import ObjDetection # for object detection in the frame
from Algorithm import PtzAlgorithm # for controlling the ptz by the face position


def start_process(frame_grabber, detector, algorithm):
    while True: # Do this process forever
        frame = frame_grabber.grab_frame() # get the frame from the camera
        if frame is not None:
            face_dimensions = detector.detect(frame, display_window=True) # detect face in the frame
            if face_dimensions: # if face was detected
                x, y, w, h = face_dimensions # unpack positions from face
                algorithm.decide(x, y, w, h) # let the algorithm decide how to move the motors by the face positions


if __name__ == '__main__':
    RTSP_URL = "rtsp://192.168.1.117:8554/substream"
    MOTOR_HOST = "192.168.1.117"
    MOTOR_PORT = 8080
    CASCADE_PATH = '/home/qlorg/Documents/ptz_opencv_face_detection/src/cascades/haarcascade_frontalface_default.xml'
    

    frame_grabber = ThreadedCamera(RTSP_URL)
    frame_dimensions = frame_grabber.get_frame_dimentions()
    detector = ObjDetection(CASCADE_PATH)
    algorithm = PtzAlgorithm(MOTOR_HOST, MOTOR_PORT, frame_dimensions)
    start_process(frame_grabber, detector, algorithm)
