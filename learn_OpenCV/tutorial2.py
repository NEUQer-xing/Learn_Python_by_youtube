import random
import cv2
import numpy as np

img = cv2.imread("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/colorcolor.jpg")

# print(img)

# img2 = np.empty((300,300,3),np.uint8)

# for row in range(0,300):
#     for col in range(0,img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

img_new = img[:105,200:400]
#               长     宽

cv2.imshow("img",img)
cv2.imshow('img_new',img_new)
cv2.waitKey(0)

