import requests
import time
import LiveImageCapturter
import WhatsAppSender
from pygame import mixer
import threading

# =========================
# ThingSpeak Details
# =========================
CHANNEL_ID = "3295497"
READ_KEY = "DG83X1KJHQMSV1RC"

# =========================
# Alert Settings
# =========================
alert_active = False

# Dangerous current threshold
THRESHOLD = 40.0


# =========================
# Audio Alert Function
# =========================
def playvoice():

    try:

        mixer.init()

        mixer.music.load("alert_marathi.mp3")

        mixer.music.play()

        while mixer.music.get_busy():

            time.sleep(1)

    except Exception as e:

        print("Audio error:", e)


# =========================
# Read ThingSpeak Data
# =========================
def read_thingspeak_data(admin_name, admin_password, mob):

    global alert_active

    while True:

        try:

            # =========================
            # Fetch latest data
            # =========================
            url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_KEY}&results=1"

            response = requests.get(url, timeout=5)

            data = response.json()

            # =========================
            # Check valid feed
            # =========================
            if 'feeds' not in data or len(data['feeds']) == 0:

                print("❌ No data received")

                time.sleep(5)

                continue

            feed = data['feeds'][0]

            # =========================
            # Safe float conversion
            # =========================
            pole1 = float(feed.get('field1') or 0)

            pole2 = float(feed.get('field2') or 0)

            print("Pole1:", pole1)

            print("Pole2:", pole2)

            # =========================
            # Danger Detection
            # =========================
            if (
                abs(pole1) >= THRESHOLD
                or
                abs(pole2) >= THRESHOLD
            ) and not alert_active:

                alert_active = True

                print("⚠️ DANGER DETECTED")

                # =========================
                # Audio Alert
                # =========================
                threading.Thread(target=playvoice).start()

                # =========================
                # Capture Image
                # =========================
                img = LiveImageCapturter.getLiveImage()

                if img == 1:

                    print("📸 Image captured")

                    # =========================
                    # Send WhatsApp Alert
                    # =========================
                    WhatsAppSender.sendInfoWA(
                        admin_name,
                        admin_password,
                        mob
                    )

                    print("📲 WhatsApp alert sent")

                else:

                    print("❌ Image capture failed")

                # =========================
                # Cooldown
                # =========================
                print("⏳ Cooling down for 60 seconds...")

                time.sleep(60)

                alert_active = False

        except Exception as e:

            print("Network error:", e)

        # =========================
        # Refresh delay
        # =========================
        time.sleep(5)