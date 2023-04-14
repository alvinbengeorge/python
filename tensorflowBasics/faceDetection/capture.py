import cv2
from findFace import findFace

cap = cv2.VideoCapture(0)
frameCount = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        face, _ = findFace(frame)
        
        if face is not None:
            cv2.imwrite('./images/{}.png'.format(frameCount), face)
            cv2.imshow("Face", face)
            face = cv2.resize(face, (300, 300))            
            frameCount+=1

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break