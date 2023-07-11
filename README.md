# Сервис YaCut


## Описание проекта

Сервис YaCut - это сервис укорачивания ссылок и API к нему

Ключевые возможности сервиса:
* генерация коротких ссылок и связь их с исходными длинными ссылками
* переадресация на исходный адрес при обращении к коротким ссылкам

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
* обязательного для длинной исходной ссылки
* необязательного для пользовательского варианта короткой ссылки (не должен превышать 16 символов)

Если пользователь предложит вариант короткой ссылки, который уже занят, то появляется соответствующее уведомление. Существующая в базе данных ссылка должна остаться неизменной.

Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис должен сгенерировать её автоматически. Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:
* большие латинские буквы,
* маленькие латинские буквы,
* цифры в диапазоне от 0 до 9.

Автоматически сгенерированная короткая ссылка добавляется в базу данных, но только если в ней уже нет такого же идентификатора. В противном случае идентификатор генерируется заново.


## API для проекта

API проекта доступен всем желающим. Сервис обслуживает только два эндпоинта:
* /api/id/ — POST-запрос на создание новой короткой ссылки;
* /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации openapi.yml


## Примеры запросов

**GET** `.../api/id/{short_id}/`
*200*
```
{
  "url": "string"
}
```
*404*
```
{
  "message": "Указанный id не найден"
}
```


**POST** `.../api/id/`
```
{
  "url": "string",
  "custom_id": "string"
}
```
*201*
```
{
  "url": "string",
  "short_link": "string"
}
```
*400*
```
{
  "message": "Отсутствует тело запроса"
}
```


## .env файл
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET
```


## Инструкция по разворачиванию проекта

* клонировать проект на компьютер `git clone https://github.com/luydmila-davletova/yacut`
* создание виртуального окружения `python3 -m venv venv`
* запуск виртуального окружения `. venv/bin/activate`
* установить зависимости из файла requirements.txt `pip install -r requirements.txt`
* запуск тестов `pytest`
* запуск приложения `flask run`


## Системные требования

* Python 3.8
* Flask 2.0.2
