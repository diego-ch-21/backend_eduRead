from flask import Blueprint, request,jsonify,make_response
from utils.db import db
from schemas.usuarioShemas import usuario_schema,usuarios_schema
from schemas.cuentoShemas import cuentos_schema,cuento_schema
from schemas.controlShemas import controles_schema,control_schema
from models.usuario import Usuario
from models.control import Control
from models.cuento import Cuento

auth_service = Blueprint('auth_service',__name__)

@auth_service.route('/auth_service/v1/register/usuario', methods=['POST'])
def register_usuario():
    try:
        datos = request.json
        nombre = datos.get("nombre")
        clave = datos.get("clave")
        edad = datos.get("edad")

        if not nombre or not clave or not edad:
            return jsonify({
                'message': 'Todos los campos son requeridos',
                'status': 400
            }), 400

        usuario_existente = Usuario.query.filter_by(nombre=nombre).first()
        if usuario_existente:
            return jsonify({
                'message': 'El usuario ya está registrado',
                'status': 400
            }), 400

        # Crear el usuario
        nuevo_usuario = Usuario(nombre=nombre, clave=clave, edad=edad)
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Consultar los cuentos
        cuentos = Cuento.query.all()
        if cuentos:  # Solo si hay cuentos
            for cuento in cuentos:
                nuevo_control = Control(id_usuario=nuevo_usuario.id_usuario, id_cuento=cuento.id_cuento, estrella=0)
                db.session.add(nuevo_control)
            db.session.commit()  # Confirmar cambios después de agregar los controles

        return jsonify({
            'message': 'Usuario registrado correctamente',
            'status': 200
        }), 200
    except Exception as e:
        logging.error(f"Error al registrar el usuario: {str(e)}")
        return jsonify({
            'message': 'Error al registrar el usuario',
            'status': 500,
            'error': str(e)  # Opcional, solo para desarrollo
        }), 500

    
#logear
@auth_service.route('/auth_service/v1/login/usuario', methods=['POST'])
def login_usuario():
    try:
        datos = request.json
        nombre = datos.get("nombre")
        clave = datos.get("clave")
        if not nombre or not clave:
            return jsonify({
                'message': 'nombre y clave son requeridos',
                'status': 400
            }), 400
        
        usuario = Usuario.query.filter_by(nombre=nombre,clave=clave).first()
        data_usuario = usuario_schema.dump(usuario)
        
        
        if usuario:
            
            
            cuentos_en_control = Control.query.filter_by(id_usuario=usuario.id_usuario).all()
            lista_id_cuentos_usuario = [cuento.id_cuento for cuento in cuentos_en_control]
            
            todos_los_cuentos = Cuento.query.filter().all()
            lista_todos_id_cuentos = [cuento.id_cuento for cuento in todos_los_cuentos]
            
            #lista con las id de los cuentos que no estan en control
            lista_cuentos_no_control = list(set(lista_todos_id_cuentos) - set(lista_id_cuentos_usuario))
            if lista_cuentos_no_control :
                print(lista_cuentos_no_control )
                
                for i in lista_cuentos_no_control:
                    nuevo_control = Control(
                    id_usuario=usuario.id_usuario,
                    id_cuento=i,
                    estrella = 0
                    )
                    db.session.add(nuevo_control)
                    db.session.commit()
                print("se agrego nuevos cuentos al control")
            else:
                print('no hay nuevos cuentos agregados al control')
                    
            return jsonify({
                'message': 'usuario logeado correctamente',
                'status': 200,
                'data': data_usuario
            }), 200
        else:
            return jsonify({
                'message': 'credenciales incorrectas',
                'status': 404
            }), 404
    except Exception as e:
        error_data = {
            'message': 'Error al logear el usuario',
            'status': 500,
            'error': str(e)
        }
        return jsonify(error_data), 500