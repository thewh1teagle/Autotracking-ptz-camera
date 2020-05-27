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
        face_dimensions = detector.detect(frame, display_window=True)
        if face_dimensions:
            x, y, w, h = face_dimensions
            algo.decide(x, y, w, h)


def main():

    frame_grabber = ThreadedCamera(RTSP_URL)
    frame_dimensions = frame_grabber.get_frame_dimentions()
    detector = ObjDetection(CASCADE_PATH)
    algorithm = PtzAlgorithm(HOST, MOTOR_PORT, frame_dimensions)

    while True:
        procees(frame_grabber, detector, algorithm)


if __name__ == '__main__':
    RTSP_URL = "rtsp://192.168.1.117:8554/substream"
    HOST = "192.168.1.117"
    MOTOR_PORT = 8080
    CASCADE_PATH = '/home/qlorg/Documents/ptz_opencv_face_detection/src/cascades/haarcascade_frontalface_default.xml'
    main()
