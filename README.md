## Запуск бота

### Через docker-compose:

1. Cклонировать репозиторий.
2. Скопировать файл `.env_example` в `.env` и заполнить его данными.
3. В терминале выполнить команду `docker-compose build app` находясь в корневой директории проекта.
4. В терминале выполнить команду `docker-compose up -d` находясь в корневой директории проекта.
5. Поздравляю, бот запущен!

### Через консоль:

1. Cклонировать репозиторий.
2. Скопировать файл `.env_example` в `.env` и заполнить его данными.
3. В терминале выполнить команду `pip install -r requirements.txt` находясь в корневой директории проекта.
4. В терминале выполнить команду `python3 -m src` находясь в корневой директории проекта.
5. Поздравляю, бот запущен!



## Техническое задание:

Напишите телеграмм-бота на языке Python, который будет выполнять следующие функции:

1. Приветствовать пользователя и предлагать ему выбрать определенную функцию бота.
2. Определить текущую погоду в определенном городе, используя публичное API погоды (например, OpenWeatherMap) и выдавать пользователю соответствующую информацию.
3. Конвертировать валюты, используя публичное API курсов валют (например, Exchange Rates API) и предоставлять пользователю результат конвертации.
4. Отправлять случайную картинку с милыми животными
5. Создавать опросы (polls) и отправлять их в групповой чат с определенным вопросом и вариантами ответов.


### Требования:

1. Бот должен быть реализован на языке Python с использованием библиотеки aiogram.
2. Бот должен быть оформлен в виде отдельного модуля или пакета.
3. Бот должен быть устойчив к ошибкам пользователя и корректно обрабатывать исключительные ситуации.
4. Код бота должен быть чистым, асинхронным, хорошо организованным и содержать комментарии, объясняющие логику работы.
5. Бот должен успешно выполнять все описанные функции.

### Инструкции:

1. Создайте новый репозиторий на GitHub и выложите в него ваше решение.
2. Оформите ваш бот в виде одного или нескольких Python-модулей или пакетов.
3. Реализуйте все описанные функции бота в соответствующих модулях.
4. Обработайте исключения и ошибки, чтобы бот был стабильным и надежным.
5. Добавьте комментарии в код, чтобы объяснить вашу логику.
6. Протестируйте вашего бота, убедитесь, что он работает корректно и выполняет все заданные функции.
7. Отправьте ссылку на ваш репозиторий с решением нашему отделу HR для оценки.