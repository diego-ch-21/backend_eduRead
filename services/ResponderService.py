from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.controlShemas import controles_schema,control_schema
from models.cuento import Cuento
from models.control import Control
from models.pregunta import Pregunta

responder_service = Blueprint('responder_service',__name__)

@responder_service.route('/responder_service/v1/responder', methods=['POST'])
def responder_preguntas():
    try:
        data = request.get_json()
        id_usuario = data.get('id_usuario')
        id_cuento = data.get('id_cuento')
        array_respuestas = data.get('array_respuestas')

        if not id_usuario or not id_cuento or not array_respuestas:
            return jsonify({'message': 'Datos incompletos', 'status': 400}), 400

        # Asegúrate de que array_respuestas sea una lista
        lista_respuestas = array_respuestas if isinstance(array_respuestas, list) else array_respuestas.split(",")

        cuento = Cuento.query.filter_by(id_cuento=id_cuento).first()
        if not cuento:
            return jsonify({'message': 'Cuento no encontrado', 'status': 404}), 404

        preguntas = Pregunta.query.filter_by(id_cuento=id_cuento).all()
        if len(lista_respuestas) != len(preguntas):
            return jsonify({'message': 'Número de respuestas no coincide con las preguntas', 'status': 400}), 400

        cont_estrella = 0
        for i in range(len(preguntas)):
            if lista_respuestas[i] == preguntas[i].resp_correcta:
                cont_estrella += 1

        control = Control.query.filter_by(id_usuario=id_usuario, id_cuento=id_cuento).first()
        if not control:
            return jsonify({'message': 'No se encontró control para el usuario y el cuento', 'status': 404}), 404

        if control.estrella < cont_estrella:
            control.estrella = cont_estrella
            db.session.commit()

        return jsonify({
            'message': 'Respuestas guardadas correctamente',
            'status': 200,
            'data': cont_estrella
        }), 200

    except Exception as e:
        return jsonify({'message': 'Error al procesar la solicitud', 'status': 500, 'error': str(e)}), 500
