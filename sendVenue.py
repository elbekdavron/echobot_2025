import requests
import os
TOKEN = os.getenv("TOKEN")

def send_venue(chat_id, latitude, longitude, title, address):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVenue"
    params = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude,
        "title": title,
        "address": address
    }
    response = requests.post(url, params=params)
    return response.json()

send_venue(chat_id=988528730, latitude=39.654052, longitude=66.975986, title="Registon", address="Samrqand shahar, Registon ko'chasi")