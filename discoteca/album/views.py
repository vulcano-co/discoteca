from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.album.models import Album
from discoteca.artista.models import Artista
from datetime import time

album = Blueprint('album',__name__, template_folder='templates')

@album.route('/')
def index():
    q = request.args.get('q')
    if q:
        albuns = Album.query.filter(Album.nome.contains(q))
    else :
        albuns = Album.query.all()
    return render_template('album.html', albuns=albuns)



@album.route('/cadastrar',methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome            = request.form['nome']
        ano             = request.form['ano']
        img             = request.form['img']
        duracaoCru      = request.form['duracao'].split(":")
        h=int(duracaoCru[0])
        m=int(duracaoCru[1])
        if len(duracaoCru) < 3:
            s=0
        else:
            s=int(duracaoCru[2])


        duracao = time(h,m,s) 

        genero_musical  = request.form['genero_musical']
        idioma          = request.form['idioma']
        formato         = request.form['formato']
        avaliacao       = request.form['avaliacao']

        album = Album(nome=nome,
                      ano=ano,
                      img=img,
                      duracao=duracao,
                      genero_musical=genero_musical,
                      idioma=idioma,
                      formato=formato,
                      avaliacao=avaliacao)
        db.session.add(album)
        db.session.commit()

        return redirect(url_for('album.index'))  

    return render_template('cadastrar_album.html')     

@album.route('/perfil/<_id>', methods=['GET'])
def perfil(_id):
    album = Album.query.get_or_404(_id)
    return render_template('perfil_album.html', album=album)

@album.route('/editar/<_id>', methods=['GET','POST'])
def editar(_id):
    album = Album.query.get_or_404(_id)

    if request.method == 'POST':
        album.nome            = request.form['nome']
        album.ano             = request.form['ano']
        album.img             = request.form['img']
        duracaoCru         = request.form['duracao'].split(":")
        album.duracao = time(
            int(duracaoCru[0]),
            int(duracaoCru[1]),
            int(duracaoCru[2]) 
        ) 
        album.genero_musical  = request.form['genero_musical']
        album.idioma          = request.form['idioma']
        album.formato         = request.form['formato']
        album.avaliacao       = request.form['avaliacao']

        db.session.commit()
        return redirect(url_for('album.perfil', _id=album.id))
    
    
    return render_template('editar_album.html', album=album)
     


@album.route('/excluir/<_id>', methods=['GET','POST'])
def excluir(_id):
    album = Album.query.get_or_404(_id)
    if request.method == 'POST':
        db.session.delete(album)
        db.session.commit()        
        return redirect(url_for('album.index'))
    
    return render_template('excluir_album.html', album=album)

@album.route('/associar_artista/<_id>', methods=['GET','POST'])
def associar_artista(_id):
    album  = Album.query.get_or_404(_id)
    artistas = Artista.query.all()

    if request.method == 'POST':
        id_artista = request.form['id_artista']
        artista_associado = Artista.query.get_or_404(id_artista)
        album.artistas.append(artista_associado)

        nAlbuns = len(artista_associado.albuns) + 1

        somaNotas = album.avaliacao
        for album in artista_associado.albuns:
            somaNotas += album.avaliacao

        artista_associado.media = somaNotas/nAlbuns
        db.session.commit()

        return redirect(url_for('album.perfil',_id=album.id))

    return render_template('associar_artista.html', album=album, artistas=artistas)