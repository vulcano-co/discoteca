from flask import Blueprint, render_template

artista = Blueprint('artista',__name__, template_folder='templates')

@artista.route('/')
def index():
    return render_template('artistas.html')

@artista.route('/cadastrar',methods=["GET","POST"])
def cadastrar():
    return render_template('cadastrar_artistas.html')     