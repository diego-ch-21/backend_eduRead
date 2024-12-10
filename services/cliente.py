from flask import Blueprint, request,jsonify,make_response
from models.cliente import Cliente
from utils.db import db
from schemas.cliente import cliente_schema,clientes_schema

cliente = Blueprint('cliente',__name__)

#crear un cliente
@cliente.route('/cliente/v1/crear',methods=['POST'])
def crear_cliente():
    nombre =  request.json.get('nombre')
    telefono = request.json.get('telefono')
    email = request.json.get('email')
    
    nuevo_cliente = Cliente(nombre,telefono,email)
    db.session.add(nuevo_cliente)
    db.session.commit()
    resultado = cliente_schema.dump(nuevo_cliente)
    
    return make_response(jsonify(resultado),201)

#Listar los clientes
@cliente.route('/cliente/v1/listar',methods=['GET'])
def listar_clientes():
    all_clientes= Cliente.query.all()
    resultado = clientes_schema.dump(all_clientes)
    
    return make_response(jsonify(resultado),200)


#buscar un cliente por id
@cliente.route('/cliente/v1/<int:id>',methods=['GET'])
def buscar_un_cliente(id):
    cliente = Cliente.query.get(id)
    
    if not cliente:
        data = {
            'message':'Cliente no encontrado',
            'status':404
        }
        return make_response(jsonify(data),404)
    
    resultado = cliente_schema.dump(cliente)
    return make_response(jsonify(resultado),200)

#actualizar un cliente por id
@cliente.route('/cliente/v1/actualizar/<int:id>',methods=['PUT'])
def actualizar_un_cliente(id):
    cliente_antiguo = Cliente.query.get(id)
    if not cliente:
        data = {
            'message':'Cliente no encontrado',
            'status':404
        }
        return make_response(jsonify(data),404)
    nombre = request.json.get('nombre')
    telefono = request.json.get('telefono')
    email = request.json.get('email')
    
    cliente_antiguo.nombre = nombre
    cliente_antiguo.telefono = telefono
    cliente_antiguo.email = email
    db.session.commit()
    
    resultado = cliente_schema.dump(cliente_antiguo)
    return make_response(jsonify(resultado),200)

#eliminar un cliente segun una id
@cliente.route('/cliente/v1/eliminar/<int:id>',methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        data = {
            'message':'Cliente no encontrado',
            'status':404
        }
        return make_response(jsonify(data),404)
    db.session.delete(cliente)
    db.session.commit()
    data = {
        'message':'Cliente eliminado correctamente',
        'status':200
    }
    
    return make_response(jsonify(data),200)
    
    
    