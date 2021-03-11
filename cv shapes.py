import cv2
import numpy as np
import pyautogui
import time
img=np.zeros((640,640,3),np.uint8)
img=np.zeros((640,640,3),np.uint8)
cv2.line(img,(0,0),(640,640),(255,0,0),3)
cv2.imshow("Image",img) 
