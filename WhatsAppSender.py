import pywhatkit as pwk
import time
import os

def sendInfoWA(admin_name, admin_password, mob):

    lat = "18.4635"
    longi = "73.8682"
    location_url = f"https://www.google.com/maps?q={lat},{longi}"

    # 🔥 IMPORTANT: paste your latest ngrok link here
    live_link = "https://anatomist-faster-shrunk.ngrok-free.dev"

    message = f"""🚨 ELECTRICAL POLE DANGER ALERT 🚨

Admin: {admin_name}

Electrical leakage detected in pole.

Immediate action required.

📍 Location:
{location_url}

🎥 Live Monitoring:
{live_link}

Smart Electrical Pole Monitoring System
"""

    mobilenumber = "+91" + mob
    reference_image_path = "Captured_Images/Temp.jpg"

    if not os.path.exists(reference_image_path):
        print("❌ Image missing")
        return

    time.sleep(2)

    print("📲 Sending WhatsApp...")

    pwk.sendwhats_image(
        mobilenumber,
        reference_image_path,
        message,
        wait_time=25,
        tab_close=False
    )