import argparse
import random
import os
from pathlib import Path

import telegram
from dotenv import load_dotenv
from load_images_core import get_images_from_dir


def send_photo(token_telegram, chat_id, photo):
    bot = telegram.Bot(token=token_telegram)
    if photo:
        # photo = os.path.join('image/', photo)
        photo = Path.cwd() / 'image' / photo
        with open(photo, 'rb') as image:
            bot.send_photo(chat_id=chat_id, photo=image)
    else:
        photo = random.choice(get_images_from_dir())
        with open(photo, 'rb') as image:
            bot.send_photo(chat_id=chat_id, photo=image)


def main():
    load_dotenv()
    token_telegram = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    parser = argparse.ArgumentParser(description='Публикует одно фото из каталога Image в телеграм канал, '
                                                 'если не указано - случайную')
    parser.add_argument('-p', '--photo', help='Укажите название фотографии')
    args = parser.parse_args()
    photo = args.photo
    send_photo(token_telegram, chat_id, photo)


if __name__ == "__main__":
    main()
