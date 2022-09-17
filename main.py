import requests
from pathlib import Path
from urllib.parse import urlparse
from os.path import splitext
import os
import datetime
from dotenv import load_dotenv


load_dotenv()


name_photo = 'hubble.jpeg'
url_photo = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


def save_image(url, filename):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    path = Path('image', filename)
    path.parent.mkdir(exist_ok=True, parents=True)
    with path.open('wb') as file:
        file.write(response.content)


def get_links_photo_spacex(link_launch):
    response = requests.get(link_launch)
    response.raise_for_status()
    launch_url = response.json()
    photo_urls = launch_url.get('links').get('flickr').get('original')
    return photo_urls


def fetch_spacex_last_launch(url_launch):
    links_photo_spacex = get_links_photo_spacex(url_launch)
    for num, photo_spacex in enumerate(links_photo_spacex):
        ext = get_photo_ext(photo_spacex)
        file = f"spacex_{num}.{ext}"
        save_image(photo_spacex, file)


def get_photo_ext(url):
    path_file = urlparse(url)[2]
    ext = splitext(path_file)[1]
    return ext


def get_apod_photo(num_photo):
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key, "count": num_photo}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_json = response.json()
    for num, apod in enumerate(apod_json):
        apod_url = apod.get('url')
        ext = get_photo_ext(apod_url)
        file = f"nasa_apod_{num}.{ext}"
        save_image(apod_url, file)


def get_apic_photo(date):
    apic_date = datetime.date.fromisoformat(date)
    year, month, day = apic_date.year, apic_date.month, apic_date.day
    # year, month, day = date.split(" ")[0].split("-")
    api_key = os.environ['API_KEY']
    params = {"api_key": api_key}
    url_natural = f"https://api.nasa.gov/EPIC/api/natural/date/{apic_date}/?api_key={api_key}"
    response = requests.get(url_natural, params=params)
    url_natural_json = response.json()
    for url in url_natural_json:
        image = url.get("image")
        url_image = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month:02d}/{day:02d}/png/{image}.png?api_key={api_key}"
        file = f"{image}.png"
        save_image(url_image, file)


def main():
    # save_image(url_photo, name_photo)
    get_apod_photo(15)
    # get_apic_photo('2022-05-20')


if __name__ == "__main__":
    main()