from utils.ma import ma
from models.control import Control
from marshmallow import fields
from schemas.usuarioShemas import UsuarioSchema
from schemas.cuentoShemas import cuento_schema
from models.cuento import Cuento

class ControlSchema(ma.Schema):
    class Meta:
        model= Control
        fields = (
            'id_control',
            'id_cuento',
            'id_usuario',
            'estrella'
        )


control_schema = ControlSchema()
controles_schema = ControlSchema(many=True)


'''
class ControlSchema(ma.Schema):
    class Meta:
        model= Control
        fields = (
            'id_control',
            'id_cuento',
            'cuento',
            'estrella'
        )
    cuento = ma.Method("get_cuento")

    def get_cuento(self, obj):
        cuento = Cuento.query.get(obj.id_cuento)
        return cuento_schema.dump(cuento) if cuento else None


control_schema = ControlSchema()
controles_schema = ControlSchema(many=True)
'''