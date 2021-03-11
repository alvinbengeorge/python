import numpy as np
import cv2
import time
import psutil
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
time.sleep(1)
cap.set(3,300)
cap.set(4,200)
if True:
    cv2.namedWindow('image')
    cv2.createTrackbar('H_l','image',0,180,nothing)
    cv2.createTrackbar('S_l','image',0,255,nothing)
    cv2.createTrackbar('V_l','image',0,255,nothing)
    cv2.createTrackbar('H_u','image',0,180,nothing)
    cv2.createTrackbar('S_u','image',0,255,nothing)
    cv2.createTrackbar('V_u','image',0,255,nothing)
#lower:70,101,89
#higher:111,255,169
h,s,v=70,101,80
h1,s1,v1=111,255,169
while True:    
    #time.sleep(0.02)
    if True:
        h = cv2.getTrackbarPos('H_l','image')
        s = cv2.getTrackbarPos('S_l','image')
        v = cv2.getTrackbarPos('V_l','image')
        h1 = cv2.getTrackbarPos('H_u','image')
        s1 = cv2.getTrackbarPos('S_u','image')
        v1 = cv2.getTrackbarPos('V_u','image')
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l=np.array([h,s,v])
    u=np.array([h1,s1,v1])
    mask=cv2.inRange(hsv,l,u)
    #cv2.imshow("Capture",frame)
    cv2.imshow("Mask",mask)
    con,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img=cv2.drawContours(frame,con,-1,(255,100,0),1)
    cv2.imshow("Contour",img)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
