# JSON Checks Extractor


Этот скрипт предназначен для извлечения JSON-данных из лог-файлов и их преобразования в XML-формат. Он ищет строки, содержащие информацию о завершении создания JSON, декодирует данные из base64 и сохраняет их в виде XML-файлов в соответствующей директории.


## Описание


Скрипт выполняет следующие действия:


1. Ищет лог-файлы в текущем каталоге с расширениями `.log` и `.txt`.

2. Пользователь выбирает файл для обработки.

3. Скрипт читает файл и ищет строки, содержащие шаблон `DEBUG r.c.c.q.Main [main] finish create json:`.

4. Извлекает JSON-данные из найденных строк.

5. Декодирует данные из base64.

6. Создает директорию с текущей датой и сохраняет XML-файлы с именами, соответствующими `uri` из JSON.


## Установка


1. Убедитесь, что у вас установлен Python 3.x.

2. Клонируйте этот репозиторий на свой локальный компьютер:

       git clone https://github.com/AlexCompDev/json_checks_extractor.git

3. Перейдите в директорию проекта:

        cd json_checks_extractor

4. Использование:

  Поместите ваши лог-файлы в директорию с скриптом.

5. Запустите скрипт:

        python json_checks_extractor.py

  Следуйте инструкциям на экране, чтобы выбрать файл для обработки.

Пример

При запуске скрипта вы увидите список лог-файлов в текущем каталоге. Выберите номер файла, который хотите обработать, и скрипт создаст XML-файлы в папке output, структурированной по дате.
