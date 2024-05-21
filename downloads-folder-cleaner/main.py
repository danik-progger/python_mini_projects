import os
from datetime import datetime

downloads_folder_path = "/home/dan/Downloads/"
files_in_telegram_folder = os.listdir(downloads_folder_path + "telegram/")
files_in_yandex_folder = os.listdir(downloads_folder_path + "yandex/")


now = datetime.now()
for folder in [files_in_yandex_folder, files_in_telegram_folder]:
    for f in folder:
        last_access_time_ms = os.stat(f)[8] # 8 - index of st_atime
        if (now - datetime.fromtimestamp(last_access_time_ms)).days > 30:
            os.remove(f)
