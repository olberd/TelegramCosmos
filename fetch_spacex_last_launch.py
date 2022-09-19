import argparse
from load_images_core import get_photo_ext, save_image, get_links_photo_spacex


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(description='Скачивает фото запуска ракет')
    parser.add_argument('--id', help='ID запуска. Например 5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    launch = args.id
    if not launch:
        url_launch = 'https://api.spacexdata.com/v5/launches/latest'
    else:
        url_launch = f'https://api.spacexdata.com/v5/launches/{launch}'
    links_photo_spacex = get_links_photo_spacex(url_launch)
    for num, photo_spacex in enumerate(links_photo_spacex):
        ext = get_photo_ext(photo_spacex)
        file = f"spacex_{num}.{ext}"
        save_image(photo_spacex, file)


if __name__ == "__main__":
    fetch_spacex_last_launch()
