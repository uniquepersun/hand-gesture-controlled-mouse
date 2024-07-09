import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    drawing_utils = mp.solutions.drawing_utils
    if hands:
        for hand in hands:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = pyautogui.size()[0] / frame.shape[1] * x
                    index_y = pyautogui.size()[1] / frame.shape[0] * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = pyautogui.size()[0] / frame.shape[1] * x
                    thumb_y = pyautogui.size()[1] / frame.shape[0] * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)