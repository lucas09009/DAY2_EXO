from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import User
import json

app = Flask(__name__)

# DATABASE CONNECTION
db_info = {
        'host': 'localhost',
        'database': 'robot',
        'psw': 'bayernmunich',
        'user': 'postgres',
        'port': '5432'
        }

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}:{db_info['port']}/{db_info['database']}"

#DATABASE REPRESENTATION
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import models, routes

def populate():
    with open('users.json') as u:
        data =  json.load(u)

    for items in data:
        name = items['name']
        street = items['address']['street']
        city = items['address']['city']
        zipcode = items['address']['zipcode']

        utilisateur = User(name=name, street=street, city=city, zipcode=zipcode)
        db.session.add(utilisateur)
        
        db.session.commit()
        print('Transfert Terminé!')

populate()