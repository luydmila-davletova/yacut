import re
import random
from datetime import datetime

from flask import url_for

from . import db
from .error_handlers import InvalidAPIUsage
from .constants import (
    DEFAULT_SHORT_ID_LENGTH, SHORT_URL_TAKEN,
    ALLOWED_CHARACTERS, PATTERN, ERROR_SHORT_URL,
    FIELD_REQUIRED, REGEXP_VALIDATION, ERROR_URL,
    LENGHT_MAX_URL, ERROR_URL_LEN
)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Метод сериализатор."""
        return dict(
            url=self.original,
            short_link=url_for(
                'url_redirect',
                custom_id=self.short,
                _external=True
            ))

    @classmethod
    def check_url(cls, data):
        """Метод для проверки оригинальной ссылки на валидность."""
        if 'url' not in data:
            raise InvalidAPIUsage(FIELD_REQUIRED)
        url_value = data.get('url')
        if not re.match(REGEXP_VALIDATION, url_value):
            raise InvalidAPIUsage(ERROR_URL)
        if len(url_value) > LENGHT_MAX_URL:
            raise InvalidAPIUsage(ERROR_URL_LEN)

        return url_value

    @staticmethod
    def get_url_obj(short_id):
        """Метод для получения оригинальной ссылки."""
        return URLMap.query.filter(URLMap.short == short_id)

    @classmethod
    def get_unique_short_id(cls, short):
        """Метод для проверки и генерации короткой ссылки."""
        if not short:
            random_list = random.choices(
                ALLOWED_CHARACTERS, k=DEFAULT_SHORT_ID_LENGTH
            )
            short = ''.join(random_list)
        if cls.get_url_obj(short).first() is not None:
            raise InvalidAPIUsage(SHORT_URL_TAKEN.format(short=short))
        if not re.match(PATTERN, short):
            raise InvalidAPIUsage(ERROR_SHORT_URL)

        return short

    @classmethod
    def save_obj(cls, **data):
        """Метод сохраняющий объект в БД."""
        if cls.original.name not in data:
            url_obj = URLMap(
                original=cls.check_url(data),
                short=cls.get_unique_short_id(data.get('custom_id')))
        else:
            url_obj = URLMap(**data)
        db.session.add(url_obj)
        db.session.commit()

        return url_obj
