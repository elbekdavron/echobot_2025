import requests
import os
TOKEN = os.getenv("TOKEN")

def sendDice(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDice"
    data = {
        "chat_id": chat_id
    }
    response = requests.post(url, data=data)
    return response.json()
chat_id=988528730
sendDice(chat_id)