#!/usr/bin/python3

import numpy as np
import sys
import cv2
from threading import Thread
import requests
from time import sleep


from ThreadedCamera import ThreadedCamera
from ObjDetection import ObjDetection
from Algorithm import PtzAlgorithm


def procees(frame_grabber, detector, algo):
    frame = frame_grabber.grab_frame()
    if frame is not None:
        detector.detect(frame)
        face_dimentions = detector.detect(frame)
        if face_dimentions:
            x, y, w, h = face_dimentions
            algo.decide(x, y, w, h)



def main():
    RTSP_URL = "rtsp://192.168.1.117:8554/substream"
    HOST = "192.168.1.117"
    MOTOR_PORT = 8080
    CASCADE_PATH = '/home/qlorg/Documents/ptz_opencv_face_detection/src/cascades/haarcascade_frontalface_default.xml'


    frame_grabber = ThreadedCamera(RTSP_URL)
    frame_dimentions = frame_grabber.get_frame_dimentions()
    detector = ObjDetection(CASCADE_PATH)
    algo = PtzAlgorithm(HOST, MOTOR_PORT, frame_dimentions)


    while True:
        procees(frame_grabber, detector, algo)

if __name__ == '__main__':
    main()






