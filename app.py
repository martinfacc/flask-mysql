from flask import render_template
from flask_name import app
from database import db
import os

USERNAME = ''
PASSWORD = ''
SERVER = ''
DATABASE = ''

FULL_URL_DB = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')