from utils.ma import ma
from models.control import Control
from marshmallow import fields
from schemas.usuarioShemas import UsuarioSchema
from schemas.cuentoShemas import CuentoSchema

class ControlSchema(ma.Schema):
    class Meta:
        model= Control
        fields = (
            'id_control',
            'id_cuento',
            'estrella'
        )
    usuario = ma.Nested(UsuarioSchema)
    cuento = ma.Nested(CuentoSchema)

control_schema = ControlSchema()
controles_schema = ControlSchema(many=True)