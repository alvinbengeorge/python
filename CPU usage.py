import cv2
import numpy as np
import psutil
import time
while True:
    img=np.zeros((500,500,3),np.uint8)
    c=int(psutil.cpu_percent())
    ram=int(psutil.virtual_memory()[2])
    cv2.line(img,(80,500),(80,500-(5*ram)),(0,127,255),40)
    cv2.line(img,(40,500),(40,500-(5*c)),(255,0,0),40)    
    cv2.imshow("CPU USAGE",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    time.sleep(0.7)
