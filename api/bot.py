from telegram import Bot
from http.server import BaseHTTPRequestHandler
import os
import json

TOKEN = os.environ["8988150913:AAEah2JWOvVFiE2dHzOcZPLzFaF5lSAF3O8"]
bot = Bot(token=TOKEN)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("content-length", 0))
        body = self.rfile.read(length)

        try:
            update = json.loads(body)

            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                if text == "/start":
                    bot.send_message(
                        chat_id=chat_id,
                        text="اهلا بك في البوت"
                    )

                elif text == "/ping":
                    bot.send_message(
                        chat_id=chat_id,
                        text="Pong!"
                    )

            self.send_response(200)
            self.end_headers()

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
