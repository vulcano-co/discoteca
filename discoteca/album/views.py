from flask import Blueprint

album = Blueprint('album',__name__, template_folder='templates')

@album.route('/')
def index():
    return "Album"