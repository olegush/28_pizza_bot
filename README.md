# Telegram Bot for Pizzeria

This simple telegram bot based on [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) library. Pizza menu stores in the [SQLite Database](https://sqlite.org/index.html) and manages with [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/).


# How to Install

1. Register new telegram bot and get the new token. [@BotFather](https://telegram.me/botfather)


2. Python 3.6 and libraries from **requirements.txt** should be installed. Use virtual environment tool, for example **virtualenv**.

```bash

virtualenv virtualenv_folder_name
source virtualenv_folder_name/bin/activate
python3 -m pip install -r requirements.txt
```

3.Put vulnerable parameters to to .env file.

```bash
HOST=127.0.0.1
PORT=5000
FLASK_DEBUG=TRUE
DB_URI=sqlite:///db/catalog.db
ADMIN_LOGIN=admin_login
ADMIN_PWD=admin_password
TELEGRAM_TOKEN=telegram_token
```

FLASK_DEBUG environment variable Flask loads by itself, but for PORT loading we should use python-dotenv package.


4. To create new database launch interactive Python shell:

```bash
python3
```

and run:

```python
from app import db
from models import Pizza, Choice
db.create_all()
```

Database will be created in the **db** dir. Then, export data from **catalog.json** with run **export.py**.


5. Change templates in the **templates** folder if you need.



# Quickstart

1. Run **admin.py**

```bash

$ python admin.py

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with inotify reloader
 * Debugger is active!

```

Goto [http://127.0.0.1:5000/admin ](http://127.0.0.1:5000/admin ) with your login and password. Here you can edit the menu.

2. Run **bot.py** and test your bot in Telegram.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
