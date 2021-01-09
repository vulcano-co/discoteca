from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.album.models import Album

album = Blueprint('album',__name__, template_folder='templates')

@album.route('/')
def index():
  albuns = Album.query.all()
  return render_template('album.html', albuns=albuns)



@album.route('/cadastrar',methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome            = request.form['nome']
        ano             = request.form['ano']
        img             = request.form['img']
        duracao         = request.form['duracao']
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