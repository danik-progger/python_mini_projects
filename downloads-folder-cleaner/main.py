import os
from datetime import datetime

downloads_folder_path = "/home/dan/Downloads/"
yandex_downloads_path = downloads_folder_path + "yandex/"
telegram_downloads_path = downloads_folder_path+ "telegram/"
files_in_yandex_folder = os.listdir(yandex_downloads_path)
files_in_telegram_folder = os.listdir(telegram_downloads_path)


now = datetime.now()
for f in files_in_yandex_folder:
    last_access_time_ms = os.stat(yandex_downloads_path + f)[8] # 8 - index of st_atime
    if (now - datetime.fromtimestamp(last_access_time_ms)).days > 30:
        os.remove(f)

for f in files_in_telegram_folder:
    last_access_time_ms = os.stat(
        telegram_downloads_path + f)[8]  # 8 - index of st_atime
    if (now - datetime.fromtimestamp(last_access_time_ms)).days > 30:
        os.remove(f)
