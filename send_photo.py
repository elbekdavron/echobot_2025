import requests
import os

TOKEN = os.getenv("TOKEN")

def send_photo(chat_id:str, photo:str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id
    }
    files = {
        'photo':photo
    }
    response = requests.post(url,params=param,files=files)
    return response.json
img = open('logo.png', 'rb').read()
chat_id = 988528730
send_photo(chat_id=chat_id, photo=img)
