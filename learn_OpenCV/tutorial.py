import cv2
# # 读取照片
# img = cv2.imread("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/colorcolor.jpg")
#
# # img= cv2.resize(img,       (100,100))
# # #               改变的图片  大小
# img =  cv2.resize(img,       (0,0),fx = 0.5,fy = 0.5)
#
# cv2.imshow("img",img)
# #          标题   要显示的图片
#
# cv2.waitKey(0) # 图片显示时间

#显示视频

# cap = cv2.VideoCapture("G:/Code/Python/Learn_Python_by_youtube/learn_OpenCV/sources/thumb.mp4")

# ret,                    frame = cap.read()
# #是否成功读取下一张图片     视频的下一帧


# cap = cv2.VideoCapture(0)
# #取得电脑视频的画面
# while True :
#     ret,frame = cap.read()
#     frame = cv2.resize(frame,(0,0),fx = 1,fy = 1)
#     if ret:
#         cv2.imshow('video',frame)
#     else:
#         break
#     if cv2.waitKey(10) == ord('q'):
#         break

# #############################################################
