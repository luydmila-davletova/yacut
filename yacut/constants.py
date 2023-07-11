from string import ascii_letters, digits


ALLOWED_CHARACTERS = ascii_letters + digits

PATTERN = r'^[a-zA-Z0-9]{1,16}$'
REGEXP_VALIDATION = r'^[a-zA-Z0-9-_]+$'

DESCRIPTION_URL = 'Длинная ссылка'
MISSING_DATA = 'Обязательное поле'
ERROR_URL = 'Некорректный URL'
DESCRIPTION_SHORT = 'Ваш вариант короткой ссылки'
ERROR_LEN = 'Длина ссылки не может быть больше 16 символов'
PATTERN_SHORT_URL = r'^[A-Za-z0-9_]+$'
ERROR_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'