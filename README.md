# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как
реализованы запросы к БД. Пульт охраны - это сайт, который можно подключить к удалённой базе данных с
визитами и карточками пропуска сотрудников нашего банка.

### Как установить

- Склонируйте репозиторий на локальную машину
```
git clone https://github.com/Vika301296/Django-ORM-standalone
```

- В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Cоздайте в корне файл .env
```
ENGINE = django.db.backends.postgresql_psycopg2
ALLOWED_HOSTS=['localhost', '127.0.0.1']
DATABASE_URL=postgres://<Ваш_юзернейм>:<Ваш_пароль>@checkpoint.devman.org:5434/checkpoint
SECRET_KEY = <Ваш_код>
DEBUG = False
```

- Запустите сайт командой 
```
python3 manage.py runserver
```

- Перейдите на сайт по адресу
[http://127.0.0.1:8000](http://127.0.0.1:8000).

На сайте вы увидите данные хранилища.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).