from flask import Blueprint

artista = Blueprint('artista',__name__, template_folder='templates')

@artista.route('/')
def index():
    return "Artista"