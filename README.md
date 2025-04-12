# 🖐️ Hand Gesture Game Controller

Control PC games using hand gestures with your webcam! This project uses **MediaPipe** and **OpenCV** to detect hand gestures and map them to keyboard controls like moving, turning, and jumping.

---

## 🎮 Supported Gestures

| Gesture       | Action           | Description                          |
|---------------|------------------|--------------------------------------|
| ✊ Fist        | Stop             | All fingers folded                   |
| ☝️ Index up    | Move forward (W) | Only index finger is extended        |
| ✌️ Two fingers | Move back (S)    | Index and middle fingers extended    |
| 👍 Pinky Finger + Thumb (Pointing right) | Strafe right (D)   | Thumb extended to the right          |
| 👈 Pinky Finger + Thumb (Pointing left)  | Strafe left (A)    | Thumb extended to the left           |
| 🖐️ Open palm   | Jump (Spacebar)     | All fingers extended                 |

---

## 🧰 Requirements

- Python 3.10+
- OpenCV
- MediaPipe
- `pynput`

Install dependencies:

```bash
pip install opencv-python mediapipe pynput.keyboard
```
## 🚀 Try my project
 1. Clone the repository:
    ```bash
    git clone https://github.com/N0TM3-1/hand-controller.git
    cd hand-controller
    ```
2. Run the script:
    ```bash
    python main.py
    ```
## 🧠 How it works
1. The script uses MediaPipe to detect 21 hand landmarks
2. It compares the landmark positions to determine finger states
3. The gestures are mapped to the keyboard using **pynput**
## 🛠 Libraries Used
- [Google's MediaPipe](https://github.com/google-ai-edge/mediapipe)
- [OpenCV](https://opencv.org/)
- [Pynput](https://pynput.readthedocs.io/en/latest/)
## 📸 Credits
[Karthik Sankar](https://hackclub.slack.com/team/U04K5EPMZM1), who created the [Hack Club Visioneer project](visoneer.hackclub.com) (would've never done this if it wasn't for him).


