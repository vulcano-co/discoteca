from flask import Blueprint, render_template, request, redirect, url_for
from discoteca import db
from discoteca.artista.models import Artista

artista = Blueprint('artista',__name__, template_folder='templates')

@artista.route('/')
def index():
    return render_template('artistas.html')

@artista.route('/cadastrar',methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        pais = request.form['pais']
        genero_musical = request.form['genero_musical']
        img = request.form['img']
        
        artista = Artista(nome=nome,
                          pais=pais,
                          genero_musical=genero_musical,
                          img=img)
        db.session.add(artista)
        db.session.commit()

        return redirect(url_for('artista.index'))


    return render_template('cadastrar_artistas.html')     