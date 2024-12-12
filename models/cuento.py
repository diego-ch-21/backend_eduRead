from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuento(db.Model):
    __tablename__ = 'cuento'
    id_cuento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    image = db.Column(db.String(100))
    
    def __init__(self, title, text, image):
        self.title = title
        self.text = text
        self.image = image