from utils.ma import ma
from models.cuento import Cuento
from marshmallow import fields

class CuentoSchema(ma.Schema):
    class Meta:
        model= Cuento
        fields = (
            'id_cuento',
            'title',
            'text',
            'image'
        )

cuento_schema = CuentoSchema()
cuentos_schema = CuentoSchema(many=True)