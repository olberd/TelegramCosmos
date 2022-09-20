import datetime
import os
import requests
import argparse
from dotenv import load_dotenv
from load_images_core import save_image


load_dotenv()

URL_EPIC_API = 'https://api.nasa.gov/EPIC/api/natural/date/'
URL_EPIC_NATURAL = 'https://api.nasa.gov/EPIC/archive/natural/'


def get_epic_photo():
    parser = argparse.ArgumentParser(description='Скачивает фотографии земли на определенную дату. Например 2021-05-20')
    parser.add_argument('date', help='Введите дату в формате год-месяц-день')
    args = parser.parse_args()

    apic_date = datetime.date.fromisoformat(args.date)
    year, month, day = apic_date.year, apic_date.month, apic_date.day
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key}
    url_natural = f"{URL_EPIC_API}{apic_date}/?api_key={api_key}"
    response = requests.get(url_natural, params=params)
    url_natural_json = response.json()
    for url in url_natural_json:
        image = url.get("image")
        url_image = f"{URL_EPIC_NATURAL}{year}/{month:02d}/{day:02d}/png/{image}.png?api_key={api_key}"
        file = f"{image}.png"
        save_image(url_image, file)


if __name__ == "__main__":
    get_epic_photo()