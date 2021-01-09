from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.artista.models import Artista
from discoteca.album.models import Album
from sqlalchemy import desc

home = Blueprint('home',__name__)

@home.route('/')
def index():
    artistas = Artista.query.all()
    albuns = Album.query.order_by(Album.id.desc()).limit(5)
    return render_template('index.html', albuns=albuns, artistas=artistas)
