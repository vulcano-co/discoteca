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
    



    ############Maior Media################
    TodosArtistas=Artista.query.all()

    MediaTodos = [(0,0,0)] * len(TodosArtistas)


    for i in range(len(TodosArtistas)):
        soma=0
        nalbuns=0
        for j in range(len(TodosArtistas[i].albuns)):
            nalbuns+=1
            soma+=TodosArtistas[i].albuns[j].avaliacao
        if nalbuns!=0:
            MediaTodos[i]=(soma/nalbuns,nalbuns,i)

        else:
            MediaTodos[i]=(0,nalbuns,i)

        
    
    MaiorMedias = sorted(MediaTodos, reverse=True)
    Media=MaiorMedias[0][0]
    MaiorMedia = Artista.query.get(TodosArtistas[MaiorMedias[0][2]].id)




    albuns = Album.query.order_by(Album.id.desc()).limit(5)
    return render_template('index.html', albuns=albuns, artistas=top5, numeroDeCadastros=top5Num,MaiorMedia=MaiorMedia,Media=Media)
