import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from os.path import splitext


NAME_PHOTO = 'hubble.jpeg'
PHOTO_URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}


def save_image(url, filename, nasa_token=None):
    params = {"api_key": nasa_token}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    path = Path('image', filename)
    path.parent.mkdir(exist_ok=True, parents=True)
    with path.open('wb') as file:
        file.write(response.content)


def get_links_photo_spacex(launch_link):
    response = requests.get(launch_link)
    response.raise_for_status()
    launch_url = response.json()
    photo_urls = launch_url.get('links').get('flickr').get('original')
    return photo_urls


def get_photo_ext(url):
    path_file = urlparse(url)[2]
    ext = splitext(path_file)[1]
    return ext


def get_images_from_dir():
    path = 'image/'
    file_in_dir = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_in_dir.append(os.path.join(root, file))
    return file_in_dir
