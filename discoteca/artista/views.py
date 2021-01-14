from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.artista.models import Artista

artista = Blueprint('artista',__name__, template_folder='templates')

@artista.route('/')
def index():
    artistas = Artista.query.all()
    return render_template('artistas.html', artistas=artistas)

@artista.route('/cadastrar',methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        pais = request.form['pais']
        genero_musical = request.form['genero_musical']
        img = request.form['img']
        media = 0.0
        
        artista = Artista(nome=nome,
                          pais=pais,
                          genero_musical=genero_musical,
                          img=img,media=media)
        db.session.add(artista)
        db.session.commit()

        return redirect(url_for('artista.index'))


    return render_template('cadastrar_artistas.html')


@artista.route('/perfil/<_id>', methods=['GET'])
def perfil(_id):
    
    artista_query = Artista.query.get_or_404(_id)
    nAlbuns = len(artista_query.albuns)
    
    return render_template('perfil_artista.html', artista=artista_query, nAlbuns=nAlbuns)

@artista.route('/editar/<_id>', methods=['GET','POST'])
def editar(_id):
    artista = Artista.query.get_or_404(_id)

    if request.method == 'POST':
        artista.nome = request.form['nome']
        artista.pais = request.form['pais']
        artista.genero_musical = request.form['genero_musical']
        artista.img = request.form['img']
        
        db.session.commit()

        return redirect(url_for('artista.perfil', _id=artista.id))

    return render_template('editar_artistas.html', artista=artista)


@artista.route('/excluir/<_id>', methods=['GET','POST'])
def excluir(_id):
    artista = Artista.query.get_or_404(_id)
    if request.method == 'POST':
        db.session.delete(artista)
        db.session.commit()        
        return redirect(url_for('artista.index'))
    
    return render_template('excluir_artista.html', artista=artista)
