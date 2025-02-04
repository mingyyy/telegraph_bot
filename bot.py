from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
import requests  
from dotenv import load_dotenv
import asyncio  

# Load .env file
load_dotenv()

# Get bot token and Render URL from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RENDER_URL = "https://news-bot-for-ming.onrender.com"  # Change to your actual Render URL

# Ensure bot token exists
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN is missing! Set it in your environment variables.")

# Create Flask app
app = Flask(__name__)

# Create bot application
bot_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Define /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Your news bot is active.")

bot_app.add_handler(CommandHandler("start", start))

# ✅ Fix: Add a Health Check Route to Prevent 404 Errors
@app.route("/", methods=["GET"])
def home():
    return "Bot is running!", 200  # ✅ Returns HTTP 200 instead of 404

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handles incoming webhook updates from Telegram."""
    update = Update.de_json(request.get_json(), bot_app.bot)
    
    # ✅ Fix: Use thread-safe async function call
    loop = asyncio.get_event_loop()
    loop.create_task(bot_app.process_update(update))  # Correct way

    return "OK", 200

# Function to set webhook
def set_webhook():
    webhook_url = f"{RENDER_URL}/webhook"
    response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url={webhook_url}")
    print("Webhook setup response:", response.json())

# Run Flask server
if __name__ == "__main__":
    set_webhook()  # Automatically set webhook on startup
    app.run(host="0.0.0.0", port=5000)
