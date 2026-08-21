
import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]
GOLD_API_KEY = os.environ["GOLD_API_KEY"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(
        url,
        json={"chat_id": CHAT_ID, "text": text},
        timeout=20
    )

@app.route("/")
def home():
    return "Gold Signal Bot is running!"

@app.route("/test")
def test():
    send_telegram("🟢 Gold Signal Bot connected!")
    return "Test message sent."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
