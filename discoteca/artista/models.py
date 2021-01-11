from discoteca import app, db


class Artista(db.Model):
    __tablename__ = "artista"

    id              = db.Column(db.Integer, primary_key=True)
    nome            = db.Column(db.String(30), nullable=False)
    pais            = db.Column(db.String(30), nullable=False)
    genero_musical  = db.Column(db.String(30), nullable=False)
    img             = db.Column(db.String(2083), nullable=True)
