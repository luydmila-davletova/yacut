from flask import (
    flash, redirect,
    render_template,
    request
)

from . import app
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Ввод оригинальной ссылки и генерация короткой."""
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data or URLMap.get_unique_short_id(None)
        if URLMap.get_url_obj(short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('main_page.html', form=form)
        flash(f'Ваша новая ссылка готова: '
              f'<a href="{request.base_url}{short}">'
              f'{request.base_url}{short}</a>')
        return render_template(
            'main_page.html',
            url=URLMap.save_obj(original=form.original_link.data, short=short),
            form=form)

    return render_template('main_page.html', form=form)


@app.route('/<string:custom_id>')
def url_redirect(custom_id):
    """Редирект короткой ссылки на оригинальную."""
    return redirect(URLMap.get_url_obj(custom_id).first_or_404().original)
