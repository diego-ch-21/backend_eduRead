from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.usuarioShemas import usuario_schema,usuarios_schema
from models.usuario import Usuario
usuario_service = Blueprint('usuario_service',__name__)


@usuario_service.route('/usuario_service/v1/usuario/listar', methods=['GET'])
def get_all_usuarios():
    try:
        usuario = Usuario.query.all()
        data_usuarios = usuarios_schema.dump(usuario)
        data = {
            'message': 'Usuarios obtenidos correctamente',
            'status': 200,
            'data': data_usuarios
        }
        return jsonify(data), 200
    except Exception as e:
        error_data = {
            'message': 'Error al obtener los usuarios',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500
    