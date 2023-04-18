# *API_YaMDb*

## Описание

Проект YaMDb собирает отзывы пользователей на произведения. 
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся по категориям (фильмы, книги, музыка и др.)и могут относиться к каому-либо жанру (детектив, роман, рок и др.).
Пользователи могут оставить свои отзывы с оценкой произведения по 10-балльной шкале, а также комментировать отзывы других пользователей.
На основе пользовательских оценок произведения получают свой рейтинг.
Чтобы оставлять отзывы и комментарии, необходима регистрация.

*Алгоритм регистрации пользователей*
Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле. 

### Технологии

Python 3.7

Django 3.2

DjangoRestFramework 3.12.4

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/KirillSalamonov/api_yamdb.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:

```
cd infra
```

Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1):

```
docker-compose up -d --build
```

Выполняем миграции:

```
docker-compose exec web python manage.py makemigrations reviews

docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собираем статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Заполняем базу данными:

```
docker-compose exec web python3 manage.py shell  

from django.contrib.contenttypes.models import ContentType

ContentType.objects.all().delete()

quit()

python manage.py loaddata fixtures.json
```

Останавливаем контейнеры:

```
docker-compose down -v
```

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env

DB_ENGINE=django.db.backends.postgresql

DB_NAME=postgres

POSTGRES_USER=postgres

POSTGRES_PASSWORD=postgres

DB_HOST=db

DB_PORT=5432

### Документация API YaMDb

Документация доступна по эндпойнту: http://localhost/redoc/

### Авторы

Саламонов Кирилл

Зайцев Григорий

Ежова Марина
