import cv2
from live_stream import latest_frame

def capture():

    if latest_frame is None:
        print("❌ No frame available")
        return False

    cv2.imwrite("Captured_Images/Temp.jpg", latest_frame)
    return True