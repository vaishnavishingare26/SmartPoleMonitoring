import requests

CHANNEL_ID = "3272990"
READ_KEY = "2CV6JC0ZSYRG4JE1"

def get_sensor_data():

    url=f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_KEY}&results=1"

    try:

        response=requests.get(url,timeout=5)

        data=response.json()

        latest=data["feeds"][0]

        pole1=latest.get("field1") or 0.5
        pole2=latest.get("field2") or 0.5

        pole1=float(pole1)
        pole2=float(pole2)

        return pole1,pole2

    except:

        print("Sensor data error")

        return 0.5,0.5