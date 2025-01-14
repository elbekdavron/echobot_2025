import requests
import os
TOKEN = os.getenv("TOKEN")

def sendLocation(chat_id,latitude,longitude):
    url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
    respond = requests.get(url, data={
        'chat_id' : chat_id,
        'latitude':latitude,
        'longitude':longitude
    })
    return respond.json()

sendLocation(chat_id=988528730, latitude=39.654052, longitude=66.975986)