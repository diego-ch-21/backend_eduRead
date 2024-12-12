from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.usuarioShemas import usuario_schema,usuarios_schema
from schemas.cuentoShemas import cuentos_schema,cuento_schema
from models.cuento import Cuento

cuento_service = Blueprint('cuento_service',__name__)


@cuento_service.route('/cuento_service/v1/cuento/listar', methods=['GET'])
def get_all_cuentos(id):
    try:
        cuentos = Cuento.query.all()
        data_cuentos = cuentos_schema.dump(cuentos)
        data = {
            'message': 'Cuentos obtenidos correctamente',
            'status': 200,
            'data': data_cuentos
        }
        return jsonify(data), 200
    except Exception as e:
        error_data = {
            'message': 'Error al obtener los cuentos',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
    