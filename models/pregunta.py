from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id_pregunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cuento = db.Column(db.Integer,db.ForeignKey('cuento.id_cuento'))
    contenido = db.Column(db.String(1000))
    resp_correcta= db.Column(db.String(2))
    
    cuento = db.relationship('Cuento', backref='pregunta')
    
    def __init__(self, id_cuento, contenido, resp_correcta):
        self.id_cuento = id_cuento
        self.contenido = contenido
        self.resp_correcta = resp_correcta