import telegram
import os
from dotenv import load_dotenv


load_dotenv()


api_telegram = os.environ['API_TELEGRAM']
bot = telegram.Bot(token=api_telegram)
chat_id = '@tk_elbrus'
bot.send_message(chat_id='@tk_elbrus', text="Hi!")
bot.send_document(chat_id=chat_id, document=open('image/nasa_apod_8.jpg', 'rb'))



