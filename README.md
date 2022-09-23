# Космический телеграм канал 

Скрипты позволяют скачивать фотографии SpaceX, NASA и публиковать их в телеграм канал.

## Настройка 

### Устанавливаем зависимости
Для запуска кода необходим установленный Python3.
Используйте в консоли `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

### Получаем токены для работы с API
Получите токен для работы с API NASA.
Для получения токена NASA перейдите по ссылке [https://api.nasa.gov/](https://api.nasa.gov/) и зарегистрируйтесь. 

Пример токена:
```
VvolhJZVcfM2A11W8NofzEewF6yvY0o2o8d57Y7Y
```
Получите токен для работы с API телеграм канала.

Пример токена:
```
958423683:AABYtJ5Lde5YYfkjergber
```


### Создаем файл настроек .env
Создайте файл .env в папке со скриптами:
1. Ключ NASA - переменная под названием TOKEN_NASA.
2. Ключ Telegram -  TOKEN_TELEGRAM.
3. Канал в Telegram для публикации фотографий - CHAT_ID.
4. Периодичность публикации фотографий ботом в минутах - TIMEOUT_POST.

Пример заполненного файла .env:
```
NASA_TOKEN="your token here"
TELEGRAM_TOKEN="your token here"
CHAT_ID="@your_channel_name"
TIMEOUT_POST="delay in minutes"
```

## Приступаем к работе

### Структура файлов:
#### fetch_spacex_last_launch.py
Скачивает фото запуска SpaceX, если не указан параметр -id, грузить фото последнего запуска, если они были.

Запуск:
```
python fetch_spacex_last_launch.py --id 5eb87d47ffd86e000604b38a
```
#### get_epic_photo.py
Скачивает EPIC-фото от NASA на указанную дату.

Запуск:
```
python get_epic_photo.py 2022-01-01
```

#### get_apod_photo.py 
Скачивает APOD-фото от NASA, в параметре необходимо указать количество фото.

Запуск:
```
python get_apod_photo.py 10
```
#### post_one_photo.py
Публикует указанную фотографию в канал. Если какую не указано, публикует случайную фотографию.

Запуск:
```
python post_one_photo.py spacex_0.jpg
```
#### post_to_telegram.py
Публикует все фото из директории в бесконечном цикле, в параметре указать через сколько минут, по умолчанию раз в 4 часа.

Запуск:
```
python post_to_telegram.py 60
```

#### load_images_core.py
Вспомогательный файл.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/). 