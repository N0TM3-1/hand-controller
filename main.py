from pynput.keyboard import Controller

import disable_warnings
disable_warnings.disable()
import pynput
import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start capturing video
cap = cv2.VideoCapture(0)
keyboard = Controller()
def detect_fist(hand_landmarks):
    if hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y and hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y:
        print("Fist detected")

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip for selfie view and convert to RGB
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            detect_fist(hand_landmarks)


        cv2.imshow("Hand Tracker", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

cap.release()
cv2.destroyAllWindows()
