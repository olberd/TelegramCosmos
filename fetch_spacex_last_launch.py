import argparse
from load_images_core import get_photo_ext, save_image, get_links_photo_spacex


LAUNCHERS_URL = 'https://api.spacexdata.com/v5/launches/'


def fetch_spacex_last_launch(launch):
    launch_url = f'{LAUNCHERS_URL}{launch}'
    spacex_photo_links = get_links_photo_spacex(launch_url)
    for num, photo_spacex_url in enumerate(spacex_photo_links):
        ext = get_photo_ext(photo_spacex_url)
        if ext in ['.jpg', '.jpeg', '.gif', '.png']:
            spacex_photo = f'spacex_{num}{ext}'
            save_image(photo_spacex_url, spacex_photo)


def main():
    parser = argparse.ArgumentParser(description='Скачивает фото запуска ракет')
    parser.add_argument('--id', help='ID запуска. Например 5eb87d47ffd86e000604b38a', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == "__main__":
    main()