import datetime
import os
import requests
import argparse
from dotenv import load_dotenv
from load_images_core import save_image


EPIC_API_URL = 'https://api.nasa.gov/EPIC/api/natural/date/'
EPIC_NATURAL_URL = 'https://api.nasa.gov/EPIC/archive/natural/'


def get_epic_photo(nasa_token, date):
    apic_date = datetime.date.fromisoformat(date)
    year, month, day = apic_date.year, apic_date.month, apic_date.day
    params = {"api_key": nasa_token}
    url_natural = f"{EPIC_API_URL}{apic_date}/"
    response = requests.get(url_natural, params=params)
    natural_urls = response.json()
    for url in natural_urls:
        image = url.get("image")
        image_url = f"{EPIC_NATURAL_URL}{year}/{month:02d}/{day:02d}/png/{image}.png"
        epic_image = f"{image}.png"
        save_image(image_url, epic_image, nasa_token)


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(description='Скачивает фотографии земли на определенную дату. Например 2021-05-20')
    parser.add_argument('date', help='Введите дату в формате год-месяц-день')
    args = parser.parse_args()
    get_epic_photo(nasa_token, args.date)


if __name__ == "__main__":
    main()
