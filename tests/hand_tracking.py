import cv2
import mediapipe as mp
import socket
import json
import time

# Setup UDP socket to send data to Blender
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
BLENDER_IP = "127.0.0.1"
BLENDER_PORT = 9999

# MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            # Example: index fingertip landmark
            x = hand.landmark[8].x
            y = hand.landmark[8].y
            z = hand.landmark[8].z  # depth
            data = {"x": x, "y": y, "z": z}
            sock.sendto(json.dumps(data).encode(), (BLENDER_IP, BLENDER_PORT))

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
