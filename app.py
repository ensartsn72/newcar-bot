import os
from flask import Flask, request
import telebot

TOKEN = "7950736837:AAGQHJpIyje1dt5j7VqLPlSRg8RmFKer8Jo"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_name = message.from_user.first_name
  welcome_text = (
      f"Merhaba {user_name}!\n\n"
      "Botum artık Render üzerinde 7/24 aktif ve başarıyla çalışıyor!"
  )
  bot.reply_to(message, welcome_text)


@app.route("/webhook", methods=["POST"])
def webhook():
  if request.headers.get("content-type") == "application/json":
    json_data = request.get_json()
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "", 200
  else:
    return "Forbidden", 403


@app.route("/")
def index():
  return "Bot Render üzerinde başarıyla çalışıyor!", 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
