Сервис доступен по адресу http://3.137.178.137/
# Были созданы пользователи:
| login | passwod |
| ----------- | ----------- |
 | admin|admin|
 | user|user|
 | user2|user2|
 | user_admin|user_admin|
 
# Тестовое задание   
Python developer

## Стек   
Python, Poetry, Django, DRF, Docker, Docker-compose, PostgreSQL.

# Использование
### Без docker
1. Склонируйте данный репозиторий на свою локальную машину
2. Убедитесь, что у вас установлен пакет [Poetry](https://python-poetry.org/docs/)
3. Установите зависимости командой:
```sh
poetry install
```
4. Заполните .env файл
5. Примените миграции:
```sh
python manage.py migrate
```

6. Для запуска сервера используйте команду:
```sh
python manage.py runserver
```

7. Для авторизации создайте суперпользователя:
```sh
python manage.py createsuperuser
```

### Использование через docker
1. Склонируйте данный репозиторий на свою локальную машину
2. Заполните .env файл
3. Выполните команду:
```sh
docker-compose up -d --build
```
### API
Документация к апи доступна по адресу http://3.137.178.137/swagger-ui/
