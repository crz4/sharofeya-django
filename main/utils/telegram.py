# main/utils/telegram.py
import requests
from django.conf import settings
import os

def send_telegram_message(text: str) -> bool:
    """Отправка текста в несколько чатов Telegram."""
    success = True
    for chat_id in settings.TELEGRAM_CHAT_IDS:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        try:
            response = requests.post(
                url,
                data={
                    "chat_id": chat_id,
                    "text": text,
                    "parse_mode": "HTML",
                },
                timeout=5
            )
            if response.status_code != 200:
                success = False
                print(f"Ошибка отправки в чат {chat_id}: {response.text}")
        except requests.RequestException as e:
            print(f"Telegram error для {chat_id}:", e)
            success = False
    return success

def send_telegram_photo(photo_url_or_path: str, caption: str) -> bool:
    """Отправка фото в несколько чатов Telegram.
       Если передан локальный путь — откроем файл и отправим.
       Если URL — отправим по ссылке.
    """
    success = True
    for chat_id in settings.TELEGRAM_CHAT_IDS:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendPhoto"
        try:
            files = {}
            data = {"chat_id": chat_id, "caption": caption, "parse_mode": "HTML"}

            # Если файл существует локально — отправляем как файл
            if os.path.exists(photo_url_or_path):
                with open(photo_url_or_path, 'rb') as f:
                    files = {"photo": f}
                    response = requests.post(url, data=data, files=files, timeout=5)
            else:
                # Иначе считаем, что это публичный URL
                data["photo"] = photo_url_or_path
                response = requests.post(url, data=data, timeout=5)

            if response.status_code != 200:
                success = False
                print(f"Ошибка отправки фото в чат {chat_id}: {response.text}")

        except requests.RequestException as e:
            print(f"Telegram photo error для {chat_id}:", e)
            success = False

    return success
