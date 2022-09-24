import os
import argparse
import random
import time

import telegram
from dotenv import load_dotenv
from load_images_core import get_images_from_dir


def post_to_telegram(telegram_token, chat_id, args):
    bot = telegram.Bot(token=telegram_token)
    minutes = args.time * 60
    images = get_images_from_dir()
    while True:
        for img in images:
            with open(img, 'rb') as image:
                bot.send_photo(chat_id=chat_id, photo=image)
            time.sleep(minutes)
        else:
            random.shuffle(images)


def main():
    load_dotenv()
    timeout = os.environ['TIMEOUT_POST']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    parser = argparse.ArgumentParser(description='Публикует фото из каталога Image в телеграм канал.')
    parser.add_argument('-t', '--time', type=int, default=timeout,
                        help='Задержка публикации в минутах, по умолчанию 4 часа.')
    args = parser.parse_args()
    post_to_telegram(telegram_token, chat_id, args)


if __name__ == "__main__":
    main()
