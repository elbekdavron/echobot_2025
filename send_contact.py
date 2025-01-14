import requests
import os
TOKEN = os.getenv("TOKEN")

def send_contact(chat_id, phone_number, first_name, last_name):
    url = f"https://api.telegram.org/bot{TOKEN}/sendContact"
    params= {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name
    }
    response = requests.post(url, params=params)
    return response.json()
chat_id=988528730
phone_number="+9989915396855"
first_name="Elbek"
last_name="Davronov"
send_contact(chat_id, phone_number, first_name, last_name)
