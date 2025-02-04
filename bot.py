from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = Flask(__name__)  # Create Flask app

# Create bot application
bot_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Define /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Your news bot is active.")

bot_app.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.route(f"/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def webhook():
    """Handles incoming webhook updates from Telegram."""
    update = Update.de_json(request.get_json(), bot_app.bot)
    bot_app.process_update(update)
    return "OK", 200

# Run Flask server
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=5000,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_BOT_TOKEN}"
    )
