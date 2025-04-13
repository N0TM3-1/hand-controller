from pynput.keyboard import Controller
import disable_warnings
disable_warnings.disable()
from pynput.keyboard import Key, Controller
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
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release('a')
        keyboard.release('d')
        keyboard.release(Key.space)

def detect_index(hand_landmarks):
    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y:
        print("Index finger detected")
        keyboard.press('w')

def detect_two_fingers(hand_landmarks):
    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y:
        print("Two fingers detected")
        keyboard.press('s')

def detect_palm(hand_landmarks):
    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y and hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y:
        print("Open palm detected")
        keyboard.press(Key.space)

def detect_pinky(hand_landmarks):
    if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y and hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y and hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            print("Thumb pointing right")
            keyboard.press('d')
        elif hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            print("Thumb pointing left")
            keyboard.press('a')

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
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
            detect_index(hand_landmarks)
            detect_two_fingers(hand_landmarks)
            detect_palm(hand_landmarks)
            detect_pinky(hand_landmarks)

        cv2.imshow("Hand Tracker", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

cap.release()
cv2.destroyAllWindows()
