from utils.ma import ma
from models.cliente import Cliente
from marshmallow import fields

class ClienteSchema(ma.Schema):
    class Meta:
        model= Cliente
        fields = (
            'id_cliente',
            'nombre',
            'telefono',
            'email'
        )

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)