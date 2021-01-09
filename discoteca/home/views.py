from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.artista.models import Artista
from discoteca.album.models import Album

home = Blueprint('home',__name__)

@home.route('/')
def index():
    artistas = Artista.query.all()
    albuns = Album.query.all()
    return render_template('index.html', albuns=albuns, artistas=artistas)
