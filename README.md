# Retail network project

## Описание проекта

Проект реализует представления онлайн платформы торговой сети. Сеть может содержать три типа компаний:
* Завод
* Розничная сеть
* Индивидуальный предприниматель
Завод всегда находится на 0 уровне, то есть не может иметь поставщика. Каждое звено сети может ссылаться только на одного поставщика.

В проекте реализована админ-панель и CRUD для элемента сети.

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.

## Документация

Документация находится по ссылкам:
1. Для загрузки schema.yaml `api/schema/`
2. Swagger `api/schema/swagger-ui`
3. Redoc `api/schema/redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.sample
4. Соберите образ с помощью команды `docker-compose build`
5. Создайте БД командой `docker-compose exec db psql -U <postgres_user>`, а затем командой `CREATE DATABASE <database_name>;`
6. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `DATABASES_NAME, DATABASES_USER, DATABASES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
