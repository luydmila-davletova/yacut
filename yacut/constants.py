from string import ascii_letters, digits


ALLOWED_CHARACTERS = ascii_letters + digits

PATTERN = r'^[a-zA-Z0-9]{1,16}$'
REGEXP_VALIDATION = r'(https?://[\w.:]+/?(?:[\w/?&=.~;\-+!*_#%])*)'

DEFAULT_SHORT_ID_LENGTH = 6
LENGHT_MAX_URL = 256
MIN_LENGHT_URL = 1
MAX_LEN_CUSTOM_URL = 16

DESCRIPTION_URL = 'Длинная ссылка'
MISSING_DATA = 'Отсутствует тело запроса'
FIELD_REQUIRED = '"url" является обязательным полем!'
ERROR_URL = 'Некорректный URL'
DESCRIPTION_SHORT = 'Ваш вариант короткой ссылки'
ERROR_LEN = 'Длина ссылки не может быть больше 16 символов'
ERROR_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
SHORT_URL_TAKEN = 'Имя "{short}" уже занято.'
ERROR_URL_LEN = f'Длина url превышает {LENGHT_MAX_URL} символов.'
