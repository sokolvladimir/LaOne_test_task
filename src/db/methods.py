import json

from aiogram.types import Poll


class DB:

    @staticmethod
    def _get():
        """Метод возвращает db"""
        with open("src/db/db.json", "r") as file:
            return json.load(file)

    @staticmethod
    def _post(db):
        """Метод записывает db в файл"""
        with open("src/db/db.json", "w") as file:
            json.dump(db, file, indent=4)

    @classmethod
    def get_poll(cls, poll_id):
        """Метод возвращает опрос из базы данных"""
        return cls._get().get(poll_id)

    @classmethod
    def post_poll(cls, poll_id, poll):
        """Метод добавляет опрос в базу данных"""
        db = cls._get()
        db[poll_id] = cls._generate_poll_for_send(poll)
        cls._post(db)
        return True

    @staticmethod
    def _generate_poll_for_send(poll: Poll):
        """Метод генерирует опрос для отправки в группу"""
        dct = {"question": poll.question,
               "options": [i.text for i in poll.options],
               "is_anonymous": poll.is_anonymous,
               "type": poll.type,
               "allows_multiple_answers": False}
        return dct
