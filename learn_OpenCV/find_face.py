import cv2

cap = cv2.VideoCapture(0)
def find_face(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/face_detect.xml")
    faceRect = face.detectMultiScale(gray,1.3,3)
    return faceRect
while True:
    ret,img = cap.read()
    cv2.resize(img,(0,0),fx = 1.5, fy = 1.5)

    if ret :
        faceRect = find_face(img)
        for x,y,w,h in faceRect:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("video",img)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
