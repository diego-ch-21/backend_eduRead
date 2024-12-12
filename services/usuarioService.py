from flask import Blueprint, request, jsonify
from utils.db import db
from schemas.usuarioShemas import usuario_schema, usuarios_schema
from models.usuario import Usuario

usuario_service = Blueprint('usuario_service', __name__)

# Listar todos los usuarios
@usuario_service.route('/usuario_service/v1/usuario/listar', methods=['GET'])
def get_all_usuarios():
    try:
        usuarios = Usuario.query.all()
        if not usuarios:
            return jsonify({'message': 'No se encontraron usuarios', 'status': 404}), 404

        data_usuarios = usuarios_schema.dump(usuarios)
        return jsonify({
            'message': 'Usuarios obtenidos correctamente',
            'status': 200,
            'data': data_usuarios
        }), 200

    except Exception as e:
        return jsonify({
            'message': 'Error al obtener los usuarios',
            'status': 500,
            'error': str(e)
        }), 500

# Listar un usuario por ID
@usuario_service.route('/usuario_service/v1/usuario/<id>', methods=['GET'])
def get_usuario(id):
    try:
        if not id.isdigit():
            return jsonify({'message': 'ID inválido', 'status': 400}), 400

        usuario = Usuario.query.get(id)
        if not usuario:
            return jsonify({'message': 'Usuario no encontrado', 'status': 404}), 404

        data_usuario = usuario_schema.dump(usuario)
        return jsonify({
            'message': 'Usuario obtenido correctamente',
            'status': 200,
            'data': data_usuario
        }), 200

    except Exception as e:
        return jsonify({
            'message': 'Error al obtener el usuario',
            'status': 500,
            'error': str(e)
        }), 500
