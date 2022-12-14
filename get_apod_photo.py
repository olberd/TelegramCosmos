import os
import requests
import argparse
from dotenv import load_dotenv
from load_images_core import get_photo_ext, save_image


APOD_URL = 'https://api.nasa.gov/planetary/apod'


def get_apod_photo(api_key, number):
    params = {'api_key': api_key, 'count': number}
    response = requests.get(APOD_URL, params=params)
    response.raise_for_status()
    apod_urls = response.json()
    for num, apod in enumerate(apod_urls):
        apod_url = apod.get('url')
        ext = get_photo_ext(apod_url)
        apod_photo = f'nasa_apod_{num}{ext}'
        save_image(apod_url, apod_photo)


def main():
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(description='Скачивает фото космоса')
    parser.add_argument('number', help='Сколько скачивать фото')
    args = parser.parse_args()
    get_apod_photo(api_key, args.number)


if __name__ == "__main__":
    main()
