import shutil
import os
import random

# Шлях до папки
folder_path = 'data/images'

# Отримуємо всі файли з розширенням .png
files = [file for file in os.listdir(folder_path) if file.endswith('.png') and os.path.isfile(os.path.join(folder_path, file))]

# Зберігаємо варіанти з розширенням .txt для кожного файлу
txt_files = [file.replace('.png', '.txt') for file in files]

# Рандомно змішуємо файли
random.shuffle(files)

# Підрахунок кількості файлів
total_files = len(files)
seventy_percent = int(total_files * 0.7)
fifteen_percent = int(total_files * 0.15)

# Перші 70% файлів - виведення назви
for file in files[:seventy_percent]:
    shutil.move(f"{folder_path}/{file}", f"data/train/images/{file}")
    print(f"{file} saved to data/train/images")
    txt_file = file.replace('.png', '.txt')
    shutil.move(f"{folder_path}/{txt_file}", f"data/train/annotations/{txt_file}")
    print(f"{file} saved to data/train/images")

# Наступні 15% файлів - виведення розміру
for file in files[seventy_percent:seventy_percent + fifteen_percent]:
    shutil.move(f"{folder_path}/{file}", f"data/val/images/{file}")
    print(f"{file} saved to data/val/images")
    txt_file = file.replace('.png', '.txt')
    shutil.move(f"{folder_path}/{txt_file}", f"data/val/annotations/{txt_file}")
    print(f"{file} saved to data/val/images")

# Останні 15% файлів - виведення дати створення
for file in files[seventy_percent + fifteen_percent:]:
    shutil.move(f"{folder_path}/{file}", f"data/test/images/{file}")
    print(f"{file} saved to data/test/images")
    txt_file = file.replace('.png', '.txt')
    shutil.move(f"{folder_path}/{txt_file}", f"data/test/annotations/{txt_file}")
    print(f"{file} saved to data/test/images")
