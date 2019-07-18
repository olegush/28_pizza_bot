import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

DB_URI = os.environ.get('DB_URI')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_URI}?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
