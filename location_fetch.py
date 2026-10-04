import requests

def get_location():

    try:

        response=requests.get("http://ip-api.com/json/")
        data=response.json()

        lat=data["lat"]
        lon=data["lon"]

        link=f"https://www.google.com/maps?q={lat},{lon}"

        return link

    except:

        return "Location unavailable"