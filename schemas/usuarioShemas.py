from utils.ma import ma
from models.usuario import Usuario
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    class Meta:
        model= Usuario
        fields = (
            'id_usuario',
            'nombre',
            'edad',
            #'clave'
        )

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)