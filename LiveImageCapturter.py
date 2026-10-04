import os
import time

def getLiveImage():

    path = "Captured_Images/Temp.jpg"

    # ⏳ wait until image exists
    timeout = 10
    start = time.time()

    while not os.path.exists(path):
        if time.time() - start > timeout:
            print("❌ Image not found")
            return 0
        time.sleep(0.5)

    print("✅ Image Ready")
    return 1