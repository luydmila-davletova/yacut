from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import (
    DESCRIPTION_URL, MISSING_DATA,
    ERROR_URL, DESCRIPTION_SHORT,
    ERROR_LEN, PATTERN_SHORT_URL,
    ERROR_SHORT_URL
)


class URLForm(FlaskForm):
    original_link = URLField(
        DESCRIPTION_URL,
        validators=[DataRequired(message=MISSING_DATA),
                    URL(require_tld=True, message=ERROR_URL)]
    )
    custom_id = URLField(
        DESCRIPTION_SHORT,
        validators=[
            Length(1, 16,
                   message=ERROR_LEN),
            Optional(),
            Regexp(PATTERN_SHORT_URL,
                   message=ERROR_SHORT_URL)
        ]
    )
    submit = SubmitField('Создать')
