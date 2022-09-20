import telegram
import os
from dotenv import load_dotenv


load_dotenv()


api_telegram = os.environ['API_TELEGRAM']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=api_telegram)
chat_id = chat_id
bot.send_document(chat_id=chat_id, document=open('image/nasa_apod_9.jpg', 'rb'))



