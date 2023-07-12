from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .constants import MISSING_DATA


@app.route('/api/id/', methods=['POST'])
def create_url():
    """Ввод ссылки и проверка на валидность данных."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(MISSING_DATA)
    return jsonify(URLMap.save_obj(**data).to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    """Редирект короткой ссылки на оригинальную."""
    url_obj = URLMap.get_url_obj(short_id).first()
    if not url_obj:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_obj.original}), HTTPStatus.OK
