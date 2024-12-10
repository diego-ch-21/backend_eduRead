from utils.db import db
from dataclasses import dataclass

@dataclass
class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(9))
    email = db.Column(db.String(100))
    
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email