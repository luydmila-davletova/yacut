from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (
    URL, DataRequired,
    Length, Optional,
    Regexp
)

from .constants import (
    DESCRIPTION_URL, MISSING_DATA,
    ERROR_URL, DESCRIPTION_SHORT,
    ERROR_LEN, PATTERN,
    ERROR_SHORT_URL, LENGHT_MAX_URL,
    MIN_LENGHT_URL, MAX_LEN_CUSTOM_URL,
)


class URLForm(FlaskForm):
    """Форма для генерации коротких ссылок."""
    original_link = URLField(
        DESCRIPTION_URL,
        validators=[
            DataRequired(message=MISSING_DATA),
            Length(max=LENGHT_MAX_URL),
            URL(require_tld=True, message=ERROR_URL)
        ])
    custom_id = URLField(
        DESCRIPTION_SHORT,
        validators=[
            Length(
                MIN_LENGHT_URL,
                MAX_LEN_CUSTOM_URL,
                message=ERROR_LEN),
            Optional(),
            Regexp(PATTERN,
                   message=ERROR_SHORT_URL)
        ])
    submit = SubmitField('Создать')
