from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Create the bot application
app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Start Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome! Type /news for Web3 news and /videos for the latest tech videos.")

# Add handlers
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    app.run_polling()
