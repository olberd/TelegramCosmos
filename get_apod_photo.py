import os
import requests
import argparse
from dotenv import load_dotenv
from load_images_core import get_photo_ext, save_image


load_dotenv()

URL_APOD = 'https://api.nasa.gov/planetary/apod'


def get_apod_photo():
    parser = argparse.ArgumentParser(description='Скачивает фото космоса')
    parser.add_argument('number', help='Сколько скачивать фото')
    args = parser.parse_args()
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key, "count": args.number}
    response = requests.get(URL_APOD, params=params)
    response.raise_for_status()
    apod_json = response.json()
    for num, apod in enumerate(apod_json):
        apod_url = apod.get('url')
        ext = get_photo_ext(apod_url)
        file = f"nasa_apod_{num}.{ext}"
        save_image(apod_url, file)


if __name__ == "__main__":
    get_apod_photo()
