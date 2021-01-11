from discoteca import app, db


class Album(db.Model):
    __tablename__ = "album"

    id              = db.Column(db.Integer, primary_key=True)
    nome            = db.Column(db.String(30), nullable=False)
    ano             = db.Column(db.Integer, nullable=False)
    img             = db.Column(db.String(2083), nullable=True)
    duracao         = db.Column(db.Integer)
    genero_musical  = db.Column(db.String(30), nullable=False)
    idioma          = db.Column(db.String(30), nullable=False)
    formato         = db.Column(db.String(30), nullable=False)
    avaliacao       = db.Column(db.Integer, nullable=False)