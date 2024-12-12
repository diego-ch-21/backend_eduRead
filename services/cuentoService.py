from flask import Blueprint, jsonify
from utils.db import db
from schemas.usuarioShemas import usuario_schema, usuarios_schema
from schemas.cuentoShemas import cuentos_schema, cuento_schema
from schemas.controlShemas import controles_schema, control_schema
from schemas.preguntaShemas import preguntas_schema, pregunta_schema
from models.cuento import Cuento
from models.control import Control
from models.pregunta import Pregunta

cuento_service = Blueprint('cuento_service', __name__)

# Listar todos los cuentos
@cuento_service.route('/cuento_service/v1/cuento/listar', methods=['GET'])
def get_all_cuentos():
    try:
        cuentos = Cuento.query.all()
        if not cuentos:
            return jsonify({'message': 'No se encontraron cuentos', 'status': 404}), 404

        data_cuentos = cuentos_schema.dump(cuentos)
        return jsonify({
            'message': 'Cuentos obtenidos correctamente',
            'status': 200,
            'data': data_cuentos
        }), 200

    except Exception as e:
        return jsonify({
            'message': 'Error al obtener los cuentos',
            'status': 500,
            'error': str(e)
        }), 500

# Listar cuentos con datos adicionales por usuario
@cuento_service.route('/cuento_service/v1/cuento/listar/<int:id>', methods=['GET'])
def get_all_cuentos_usuario(id):
    try:
        cuentos = Cuento.query.all()
        if not cuentos:
            return jsonify({'message': 'No se encontraron cuentos', 'status': 404}), 404

        data_cuentos = cuentos_schema.dump(cuentos)

        for cuento in data_cuentos:
            control = Control.query.filter_by(id_usuario=id, id_cuento=cuento['id_cuento']).first()
            cuento['estrella'] = control.estrella if control else 0  # Asigna 0 si no hay control

            preguntas = Pregunta.query.filter_by(id_cuento=cuento['id_cuento']).all()
            cuento['preguntas'] = preguntas_schema.dump(preguntas)

        return jsonify({
            'message': 'Cuentos obtenidos correctamente',
            'status': 200,
            'data': data_cuentos
        }), 200

    except Exception as e:
        return jsonify({
            'message': 'Error al obtener los cuentos',
            'status': 500,
            'error': str(e)
        }), 500
