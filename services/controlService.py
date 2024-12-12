from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.controlShemas import controles_schema,control_schema
from models.control import Control

control_service = Blueprint('control_service',__name__)

@control_service.route('/control_service/v1/control/listar', methods=['GET'])
def get_all_controles():
    try:
        control = Control.query.all()
        data_controles = controles_schema.dump(control)
        data = {
            'message': 'Controles obtenidos correctamente',
            'status': 200,
            'data': data_controles
        }
        return jsonify(data), 200
    except Exception as e:
        error_data = {
            'message': 'Error al obtener los controles',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
    