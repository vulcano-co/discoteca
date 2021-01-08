import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

print(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = "qualquercoisa"


##########################################
############ BANCO DE DADOS ##############
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

""" 
- Inicializando o BANCO DE DADOS.

set FLASK_APP = app.py
flask run
flask db init
flask db migrate
flask db upgrade
"""

################################################
################BLUEPRINTS######################
################################################

from discoteca.home.views import home
from discoteca.album.views import album
from discoteca.artista.views import artista

app.register_blueprint(home)
app.register_blueprint(album, url_prefix="/album")
app.register_blueprint(artista, url_prefix="/artista")