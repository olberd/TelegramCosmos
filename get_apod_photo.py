import os
import requests
import argparse
from load_images_core import get_photo_ext, save_image
from dotenv import load_dotenv


load_dotenv()


def get_apod_photo():
    parser = argparse.ArgumentParser(description='Скачивает фото космоса')
    parser.add_argument('number', help='Сколько скачивать фото')
    args = parser.parse_args()

    url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key, "count": args.number}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_json = response.json()
    for num, apod in enumerate(apod_json):
        apod_url = apod.get('url')
        ext = get_photo_ext(apod_url)
        file = f"nasa_apod_{num}.{ext}"
        save_image(apod_url, file)


if __name__ == "__main__":
    get_apod_photo()
