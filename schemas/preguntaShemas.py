from utils.ma import ma
from models.pregunta import Pregunta
from marshmallow import fields
from schemas.cuentoShemas import CuentoSchema

class PreguntaSchema(ma.Schema):
    class Meta:
        model= Pregunta
        fields = (
            'id_pregunta',
            #'id_cuento',
            'contenido',
            #'resp_correcta'
        )
    rol = ma.Nested(CuentoSchema)

pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many=True)