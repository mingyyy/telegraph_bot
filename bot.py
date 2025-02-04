from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Start Command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Type /news for Web3 news and /videos for the latest tech videos.")

# Fetch and Send News
def send_news(update: Update, context: CallbackContext):
    news_list = fetch_news()
    for news in news_list:
        update.message.reply_text(f"{news['title']}\n{news['url']}")

# Fetch and Send Videos
def send_videos(update: Update, context: CallbackContext):
    video_list = fetch_youtube_videos()
    for video in video_list:
        update.message.reply_text(f"{video['title']}\n{video['url']}")

bot = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
dp = bot.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("news", send_news))
dp.add_handler(CommandHandler("videos", send_videos))

bot.start_polling()
