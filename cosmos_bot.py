import telegram
import os
from dotenv import load_dotenv


load_dotenv()


api_telegram = os.environ['API_TELEGRAM']
bot = telegram.Bot(token=api_telegram)
bot.send_message(text='Привет!', chat_id='@tk_elbrus')
