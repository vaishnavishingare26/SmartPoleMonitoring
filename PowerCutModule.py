import requests

CHANNEL_ID = "3295497"
READ_KEY = "DG83X1KJHQMSV1RC"

def check_and_display():

    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_KEY}&results=1"

    response = requests.get(url)
    data = response.json()

    feed = data['feeds'][0]

    pole1 = int(feed.get('field1', 0))
    pole2 = int(feed.get('field2', 0))

    print("\n📊 LIVE POLE VALUES FROM THINGSPEAK")
    print("Pole1:", pole1)
    print("Pole2:", pole2)

    # 🚨 Detection
    if pole1 == 1 or pole2 == 1:
        print("⚠ FAULT DETECTED → POWER CUT INITIATED")

    elif pole1 == 0 and pole2 == 0:
        print("⚡ POWER CUT SUCCESSFUL → SYSTEM SAFE")

    else:
        print("✅ NORMAL CONDITION")