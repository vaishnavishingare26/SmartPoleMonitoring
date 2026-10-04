from flask import Flask, Response
import cv2
import pygame
import os
import time

app = Flask(__name__)

# 🔊 Initialize pygame
pygame.init()
pygame.mixer.init()

# 🔊 Alarm file
alarm_sound = "new.mp3"

# 👤 Face Detector (MORE ACCURATE)
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# 📷 Camera
camera = cv2.VideoCapture(0)

# 📁 Create folder
if not os.path.exists("Captured_Images"):
    os.makedirs("Captured_Images")

# ⏱ Cooldown
last_alert = 0


def generate_frames():

    global last_alert

    while True:

        success, frame = camera.read()

        if not success:
            break

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # 👤 Detect faces
        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        print("Faces:", len(faces))

        # 👀 If detected
        if len(faces) > 0:

            current = time.time()

            if current - last_alert > 10:

                print("⚠ HUMAN DETECTED")

                # 🔊 Alarm
                try:

                    pygame.mixer.music.load(
                        alarm_sound
                    )

                    pygame.mixer.music.play()

                    print("✅ Alarm Played")

                except Exception as e:

                    print("Alarm Error:", e)

                # 📸 Save Image
                try:

                    image_path = (
                        "Captured_Images/"
                        "HumanDetected.jpg"
                    )

                    cv2.imwrite(
                        image_path,
                        frame
                    )

                    print("✅ Image Saved")

                except Exception as e:

                    print("Image Error:", e)

                last_alert = current

        # 🟩 Draw rectangle
        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Human Detected",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

        # 📡 Encode stream
        _, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame_bytes +
            b'\r\n'
        )


@app.route('/')
def index():

    return """
    <h2 style='text-align:center;'>
        Smart Pole Monitoring
    </h2>

    <div style='text-align:center;'>
        <img src='/video' width='80%'>
    </div>
    """


@app.route('/video')
def video():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == "__main__":

    app.run(
        host='0.0.0.0',
        port=5000
    )

camera.release()

cv2.destroyAllWindows()