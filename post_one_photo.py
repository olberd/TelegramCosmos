import argparse
import random
import os
import telegram
from dotenv import load_dotenv
from load_images_core import get_images_from_dir


load_dotenv()


token_telegram = os.environ['TOKEN_TELEGRAM']
chat_id = os.environ['CHAT_ID']


bot = telegram.Bot(token=token_telegram)


def send_photo():
    parser = argparse.ArgumentParser(description='Публикует одно фото из каталога Image в телеграм канал, '
                                                 'если не указано - случайную')
    parser.add_argument('-p', '--photo', help='Укажите название фотографии')
    args = parser.parse_args()

    if args.photo:
        bot.send_photo(chat_id=chat_id, photo=open(f'image/{args.photo}', 'rb'))

    else:
        photo = random.choice(get_images_from_dir())
        bot.send_photo(chat_id=chat_id, photo=open(photo, 'rb'))


if __name__ == "__main__":
    send_photo()
