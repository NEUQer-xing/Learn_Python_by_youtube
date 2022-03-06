import cv2

img = cv2.imread("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/colorcolor.jpg")

img =  cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
            #图片         bgr to gray

# 模糊处理 高斯模糊

mohu = cv2.GaussianBlur(img,(15,15),0)

# 找到图像的轮廓

canny = cv2.Canny(img,200,250)
#低于150 全部过滤掉
#高于200 全部作为边缘

# 把图片做膨胀效果
import numpy as np
kernel = np.ones((2,2 ),np.uint8)

dilate = cv2.dilate(canny,kernel,iterations=3)


# 把线条变细
erode = cv2.erode(dilate,kernel,iterations=3)
# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('mohu',mohu)


cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)