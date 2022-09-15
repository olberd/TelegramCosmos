import requests
from pathlib import Path


# filename = 'hubble.jpeg'
# url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

def save_image(url, filename):
    response = requests.get(url)
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


# url = 'https://api.spacexdata.com/v5/launches/latest'
url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
print(get_links_photo_spacex(url))
