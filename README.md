# Educational Center API

Бекенд для системи управління навчальним центром.

## Як запустити проєкт:
1. Клонуйте репозиторій.
2. Запустіть Docker: `docker-compose up --build`
3. Зробіть міграції: `docker-compose exec web python manage.py migrate`
4. Створіть суперкористувача: `docker-compose exec web python manage.py createsuperuser`