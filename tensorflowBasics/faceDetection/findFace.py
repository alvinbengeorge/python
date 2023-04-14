import cv2

FACE_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def findFace(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        face, rect = findFace(frame)
        if face is not None:
            cv2.imshow('Face', face)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    