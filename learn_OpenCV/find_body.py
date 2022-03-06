import  cv2
import  mediapipe as mp
import  time
cap = cv2.VideoCapture(0)

mp_body = mp.solutions.pose
poses = mp_body.Pose()

draw_pose = mp.solutions.drawing_utils
poseLms_style = draw_pose.DrawingSpec(color=(0,0,255),thickness=4,circle_radius= 3)
posecon_style = draw_pose.DrawingSpec(color=(0,255,0),thickness= 4,circle_radius= 3)

pre_time = 0
cur_time = 0


while True:
    ret,img = cap.read()
    if ret:
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = poses.process(img)
        img_h = img.shape[0]
        img_w = img.shape[1]
        draw_pose.draw_landmarks(img,result.pose_landmarks,mp_body.POSE_CONNECTIONS,poseLms_style,posecon_style)
        i = 0

        cur_time = time.time()
        fps = 1 / (cur_time - pre_time)
        text = 'FPS: ' + str(int(fps))
        pre_time = cur_time
        cv2.putText(img, text, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        cv2.imshow('img',img)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
