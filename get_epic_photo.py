import datetime
import os
import requests
import argparse
from dotenv import load_dotenv
from load_images_core import save_image


load_dotenv()

EPIC_API_URL = 'https://api.nasa.gov/EPIC/api/natural/date/'
EPIC_NATURAL_URL = 'https://api.nasa.gov/EPIC/archive/natural/'


def get_epic_photo():
    parser = argparse.ArgumentParser(description='Скачивает фотографии земли на определенную дату. Например 2021-05-20')
    parser.add_argument('date', help='Введите дату в формате год-месяц-день')
    args = parser.parse_args()
    apic_date = datetime.date.fromisoformat(args.date)
    year, month, day = apic_date.year, apic_date.month, apic_date.day
    token_nasa = os.environ['TOKEN_NASA']
    params = {"api_key": token_nasa}
    url_natural = f"{EPIC_API_URL}{apic_date}/"
    response = requests.get(url_natural, params=params)
    url_natural_list = response.json()
    for url in url_natural_list:
        image = url.get("image")
        image_url = f"{EPIC_NATURAL_URL}{year}/{month:02d}/{day:02d}/png/{image}.png?api_key={token_nasa}"
        epic_image = f"{image}.png"
        save_image(image_url, epic_image)


if __name__ == "__main__":
    get_epic_photo()
