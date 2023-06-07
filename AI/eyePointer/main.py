# program to detect eye

import cv2
import numpy as np
import dlib
import pyautogui


def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

def average(left, right, shape=pyautogui.size()):
    x, y = left[0]+right[0]//2, left[1]+right[1]//2
    windowSize = pyautogui.size()
    return x*windowSize[1]//shape[0], y*windowSize[0]//shape[1]


cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

def getFrame(cap):
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray, frame.shape

def getEyes(gray, face):
    landmarks = predictor(gray, face)
    # left eye
    center_bottom = midpoint(landmarks.part(41), landmarks.part(40))

    # right eye
    center_bottom2 = midpoint(landmarks.part(47), landmarks.part(46))
    return center_bottom, center_bottom2

while True:
    gray, shape = getFrame(cap=cap)
    faces = detector(gray)
    for face in faces:
        left, right = getEyes(gray, face)
        x, y = average(left, right, shape=shape)
        print(x, y, pyautogui.size()[1], shape[1])
        pyautogui.moveTo(x, y, duration=0.01)