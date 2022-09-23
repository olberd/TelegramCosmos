import os
import argparse
import random
import time

import telegram
from dotenv import load_dotenv
from load_images_core import get_images_from_dir


def main():
    bot = telegram.Bot(token=api_telegram)
    parser = argparse.ArgumentParser(description='Публикует фото из каталога Image в телеграм канал.')
    parser.add_argument('-t', '--time', type=int, default=TIMEOUT,
                        help='Задержка публикации в минутах, по умолчанию 4 часа.')
    args = parser.parse_args()
    minutes = args.time * 60
    images = get_images_from_dir()
    while True:
        for img in images:
            with open(img, 'rb') as image:
                bot.send_photo(chat_id=chat_id, photo=image)
            time.sleep(minutes)
        else:
            random.shuffle(images)


if __name__ == "__main__":
    load_dotenv()

    TIMEOUT = os.environ['TIMEOUT_POST']
    api_telegram = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']

    main()
