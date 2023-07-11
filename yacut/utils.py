import random

from .models import URLMap
from .constants import ALLOWED_CHARACTERS, DEFAULT_SHORT_ID_LENGTH


def get_unique_short_id():
    while True:
        random_list = random.choices(ALLOWED_CHARACTERS, k=DEFAULT_SHORT_ID_LENGTH)
        random_string = ''.join(random_list)
        if not URLMap.query.filter_by(short=random_string).first():
            return random_string
