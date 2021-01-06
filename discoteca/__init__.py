from flask import Flask

print(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = "qualquercoisa"

################################################
################BLUEPRINTS######################
################################################

from discoteca.home.views import home
from discoteca.album.views import album
from discoteca.artista.views import artista

app.register_blueprint(home)
app.register_blueprint(album, url_prefix="/album")
app.register_blueprint(artista, url_prefix="/artista")