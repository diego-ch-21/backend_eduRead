from utils.db import db
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario= db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    clave = db.Column(db.String(6))
    
    def __init__(self,nombre,edad,clave):
        self.nombre = nombre
        self.edad = edad
        self.clave = clave