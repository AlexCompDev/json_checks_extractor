import os
import json
import base64
from datetime import datetime


def process_log_file(file_path):
    # Создание выходной директории
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Открытие лог-файла
    with open(file_path, "r") as f:
        content = f.readlines()

    # Итерация по строкам в лог-файле
    for line in content:
        # Проверка на наличие нужной строки
        if "DEBUG r.c.c.q.Main [main] finish create json:" in line:
            print("Found matching line!")
            # Извлечение JSON из строки
            json_str = line.split("finish create json:")[
                1
            ].strip()  # Извлекаем часть строки после шаблона
            try:
                json_obj = json.loads(json_str)

                # Декодирование данных
                xml_data = base64.b64decode(json_obj["data"]).decode("utf-8")

                # Создание директории с текущей датой
                date_dir = os.path.join(output_dir, datetime.now().strftime("%Y-%m-%d"))
                if not os.path.exists(date_dir):
                    os.makedirs(date_dir)

                # Сохранение XML файла
                xml_file_path = os.path.join(date_dir, json_obj["uri"] + ".xml")
                with open(xml_file_path, "w") as f:
                    f.write(xml_data)

                print(f"File created: {xml_file_path}")
            except json.JSONDecodeError as e:
                print("Error parsing JSON:", e)
            except Exception as e:
                print("An error occurred:", e)


# Поиск всех лог-файлов в текущем каталоге
files = [f for f in os.listdir(".") if f.endswith((".log", ".txt"))]

# Печать списка файлов и запрос выбора пользователя
print("Choose a file:")
for i, f in enumerate(files):
    print(f"{i+1}. {f}")

choice = int(input("Enter the file number: ")) - 1

# Обработка выбранного файла
process_log_file(files[choice])
