import  cv2
import  mediapipe as mp
import  time
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_tracking_confidence=0.15,min_detection_confidence=0.15)

draw_hands = mp.solutions.drawing_utils
handLms_style = draw_hands.DrawingSpec(color=(0,0,255),thickness=4,circle_radius= 3)
hanscon_style = draw_hands.DrawingSpec(color=(0,255,0),thickness= 4,circle_radius= 3)

pre_time = 0
cur_time = 0

while True:
    ret, img = cap.read()
    if ret:
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = hands.process(img)
        img_h = img.shape[0]
        img_w = img.shape[1]
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                draw_hands.draw_landmarks(img,handlms,mp_hands.HAND_CONNECTIONS,handLms_style,hanscon_style)
                for i,lm in enumerate(handlms.landmark):
                    x_pos = round(lm.x * img_w)
                    y_pos = round(lm.y *img_h)
                    cv2.putText(img,str(i),(x_pos-15,y_pos+5),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,255,255),1)
                    print(i,x_pos,y_pos)

        cur_time = time.time()
        fps = 1/(cur_time - pre_time)
        text = 'FPS: ' + str(int(fps))
        pre_time = cur_time
        cv2.putText(img,text,(25,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        cv2.imshow('img',img)

    else :
        break
    if cv2.waitKey(1) == ord('q'):
        break
