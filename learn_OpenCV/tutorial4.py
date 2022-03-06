import cv2
import numpy as np

img = np.zeros((600,600,3),np.uint8)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(0,0),(400,300),(0,0,255),2)
cv2.circle(img,(300,400),40,(255,0,0),3)
cv2.putText(img,"Hello",(100,500),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

cv2.imshow('img',img)
cv2.waitKey(0)