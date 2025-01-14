import requests
import os


TOKEN = os.getenv("TOKEN")



def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    r=requests.get(url)
    return r.json()

while True:
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
    data = response.json()

    if data["result"]: 
        last_update = data["result"][-1]
        message = last_update["message"]
        chat_id = message["chat"]["id"]
        text = message["text"]

        send_message(text, chat_id) 
        break 

