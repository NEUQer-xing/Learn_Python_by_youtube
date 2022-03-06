# 人脸识别
#openbcv github
import cv2

img = cv2.imread('G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/lenna.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/face_detect.xml")

faceRect = faceCascade.detectMultiScale(gray,1.3,3)

for (x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("img",img)

cv2.waitKey(0)