import cv2
# 读取照片
img = cv2.imread("Learn_Python_by_youtube/learn_OpenCV/sources/colorcolor.jpg")

# img= cv2.resize(img,       (100,100))
# #               改变的图片  大小
img =  cv2.resize(img,       (0,0),fx = 0.5,fy = 0.5)

cv2.imshow("img",img)
#          标题   要显示的图片

cv2.waitKey(0) # 图片显示时间

#显示视频