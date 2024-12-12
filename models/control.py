from utils.db import db
from dataclasses import dataclass

@dataclass
class Control(db.Model):
    __tablename__ = 'control'
    id_control = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_cuento = db.Column(db.Integer, db.ForeignKey('cuento.id_cuento'))
    estrella= db.Column(db.Integer)
    
    def __init__(self, id_usuario, id_cuento, estrella):
        self.id_usuario = id_usuario
        self.id_cuento = id_cuento
        self.estrella = estrella