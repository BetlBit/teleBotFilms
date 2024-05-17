import telebot
from telebot import types
from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname
from parser import get_film

app = Flask(__name__)

def getFromEnv(key):
    dotenv_Path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_Path)
    return os.environ.get(key)

def sendMessage(chat_id, text):
    method = "sendMessage"
    token = getFromEnv("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route('/', methods=["POST"]) # localhost:5000/
def process():
    chat_id = request.json["message"]["chat"]["id"]
    sendMessage(chat_id=chat_id, text=get_film())
    return {"ok": True}


if __name__ == '__main__':
    app.run()
