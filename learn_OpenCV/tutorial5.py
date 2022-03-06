# 检测图片的颜色

import  cv2
import numpy as np
from numpy import array


def empty(v):
    pass

# img = cv2.imread("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/XiWinnie.jpg")
#
# img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)

cap  = cv2.VideoCapture(0)

# ret,img = cap.read()

cv2.namedWindow("trackBar")
cv2.resizeWindow('trackBar',640,320)

cv2.createTrackbar('Hue Min',"trackBar",0,179,empty)
cv2.createTrackbar('Hue Max',"trackBar",179,179,empty)
cv2.createTrackbar('Sat Min',"trackBar",0,255,empty)
cv2.createTrackbar('Sat Max',"trackBar",255,255,empty)
cv2.createTrackbar('Val Min',"trackBar",0,255,empty)
cv2.createTrackbar('Val Max',"trackBar",255,255,empty)


# ret,img = cap.read()
# hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min','trackBar')
    h_max = cv2.getTrackbarPos('Hue Max','trackBar')
    s_min = cv2.getTrackbarPos('Sat Min','trackBar')
    s_max = cv2.getTrackbarPos('Sat Max','trackBar')
    v_min = cv2.getTrackbarPos('Val Min','trackBar')
    v_max = cv2.getTrackbarPos('Val Max','trackBar')

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask = mask)

    # cv2.imshow("img", img)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result",result)
    cv2.waitKey(1)


# hsv 更容易过滤掉颜色
cv2.waitKey(0)

