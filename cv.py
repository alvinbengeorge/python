import cv2
import time
import pyautogui
from pynput.keyboard import Key,Controller
keyboard=Controller()


cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
while True:
    r,img=cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF==ord(' '):
        cv2.waitKey()
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
