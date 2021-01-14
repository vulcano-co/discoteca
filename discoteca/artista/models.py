from discoteca import app, db

ArtistaAlbum = db.Table("artistaAlbum",
    db.Column('id_artista',db.Integer,db.ForeignKey('artista.id')),
    db.Column('id_album',db.Integer, db.ForeignKey('album.id'))
)

class Artista(db.Model):
    __tablename__ = "artista"

    id              = db.Column(db.Integer, primary_key=True)
    nome            = db.Column(db.String(30), nullable=False)
    pais            = db.Column(db.String(30), nullable=False)
    genero_musical  = db.Column(db.String(30), nullable=False)
    img             = db.Column(db.String(2083), nullable=True)
    media           = db.Column(db.Float, default=0.0)
    albuns          = db.relationship("Album", secondary=ArtistaAlbum, back_populates="artistas")