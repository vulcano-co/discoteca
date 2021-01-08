from flask import Blueprint, render_template

album = Blueprint('album',__name__, template_folder='templates')

@album.route('/')
def index():
  return render_template('albuns.html')