import cv2
import  numpy as np

cap = cv2.VideoCapture(0)
pencolorHSV = [[101,95,58,134,178,238],
               [49,51,63,93,110,215]]
color = [[255,0,0],
         [0,255,0]]
# [x,y,color]
drawPoint = []
def findpen(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(len(pencolorHSV)):
        lower = np.array(pencolorHSV[i][:3])
        upper = np.array(pencolorHSV[i][3:])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        penx,peny = findContour(mask)
        cv2.circle(imgContour,(penx,peny),10,color[i],cv2.FILLED)
        if peny!=-1:
            drawPoint.append([penx,peny,i])

        # cv2.imshow("result",result)

def findContour(img):
    x,y,w,h = -1,-1,-1,-1
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
        area = cv2.contourArea(cnt)
        if area >500:
            peri = cv2.arcLength(cnt,True)
            vertices = cv2.approxPolyDP(cnt,peri*0.02,True)
            x,y,w,h = cv2.boundingRect(vertices)
    return x+w//2,y+h//8

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour,(point[0],point[1]),10,color[point[2]],cv2.FILLED)

while(True):

     ret,frame = cap.read()

     if ret:
         imgContour = frame.copy()
         cv2.imshow("video",frame)
         findpen(frame)
         draw(drawPoint)
         cv2.imshow("contour",imgContour)
     else:
         break
     if cv2.waitKey(1)==ord("q"):
         break

# 做颜色的侦测
