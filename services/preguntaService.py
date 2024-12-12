from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.preguntaShemas import preguntas_schema,pregunta_schema
from models.pregunta import Pregunta
pregunta_service = Blueprint('pregunta_service',__name__)


@pregunta_service.route('/pregunta_service/v1/pregunta/listar', methods=['GET'])
def get_all_preguntas():
    try:
        pregunta = Pregunta.query.all()
        data_preguntas = preguntas_schema.dump(pregunta)
        data = {
            'message': 'Preguntas obtenidos correctamente',
            'status': 200,
            'data': data_preguntas
        }
        return jsonify(data), 200
    except Exception as e:
        error_data = {
            'message': 'Error al obtener los preguntas',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
    