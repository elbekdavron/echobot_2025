import requests
import os

TOKEN = os.getenv("TOKEN")

def send_audio(chat_id:str, audio):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id
    }
    files = {
        'audio':audio
    }
    response = requests.post(url,params=param,files=files)
    return response.json
mp3 = open('audio.mp3', 'rb').read()
chat_id = 988528730
send_audio(chat_id=chat_id, audio=mp3)