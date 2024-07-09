import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    drawing_utils = mp.solutions.drawing_utils
    if hands:
        for hand in hands:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)