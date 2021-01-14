from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.artista.models import Artista
from discoteca.album.models import Album
from sqlalchemy import desc

home = Blueprint('home',__name__)

@home.route('/')
def index():
    artistas = Artista.query.all()
    numAlb = [(0,0)] * len(artistas)
    for i in range(len(artistas)):
        numAlb[i] = (len(artistas[i].albuns),artistas[i].id)
    maisAlbCad = sorted(numAlb, reverse=True)
    top5=list()
    top5Num=list()

    for i in range(5):
        top5.append(Artista.query.get(maisAlbCad[i][1]))
        top5Num.append(maisAlbCad[i][0])
    

    #query_melhorClassificacao = Artista.query.order_by(desc(Artista.media))

    albuns = Album.query.order_by(Album.id.desc()).limit(5)
    return render_template('index.html', albuns=albuns, artistas=top5, numeroDeCadastros=top5Num)
