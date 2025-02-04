from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def fetch_youtube_videos(query="Web3 technology"):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=5,
        order="date"
    )
    response = request.execute()
    
    videos = [
        {
            "title": item["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        for item in response.get("items", [])
    ]
    return videos
