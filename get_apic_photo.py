import datetime
import os
import requests
import argparse
from load_images_core import save_image
from dotenv import load_dotenv


load_dotenv()


def get_epic_photo():
    parser = argparse.ArgumentParser(description='Скачивает фотографии земли на определенную дату. Например 2021-05-20')
    parser.add_argument('date', help='Введите дату в формате год-месяц-день')
    args = parser.parse_args()

    apic_date = datetime.date.fromisoformat(args.date)
    year, month, day = apic_date.year, apic_date.month, apic_date.day
    # year, month, day = date.split(" ")[0].split("-")
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key}
    url_natural = f"https://api.nasa.gov/EPIC/api/natural/date/{apic_date}/?api_key={api_key}"
    response = requests.get(url_natural, params=params)
    url_natural_json = response.json()
    for url in url_natural_json:
        image = url.get("image")
        url_image = f"https://api.nasa.gov/EPIC/archive/natural/" \
                    f"{year}/{month:02d}/{day:02d}/png/{image}.png?api_key={api_key}"
        file = f"{image}.png"
        save_image(url_image, file)


if __name__ == "__main__":
    get_epic_photo()