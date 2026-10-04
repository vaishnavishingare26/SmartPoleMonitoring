import cv2
import time

def capture_image():

    cap=cv2.VideoCapture(0)

    ret,frame=cap.read()

    filename=f"Captured_Images/pole_{int(time.time())}.jpg"

    cv2.imwrite(filename,frame)

    cap.release()

    return filename