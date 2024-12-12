from flask import Flask
from flask_jwt_extended import JWTManager 
from utils.db import db
from flask_cors import CORS
import os
from config import DATABASE_CONNECTION

from services.authService import auth_service
from services.cuentoService import cuento_service
from services.controlService import control_service
from services.usuarioService import usuario_service
from services.preguntaService import pregunta_service

env = os.environ.get('FLASK_ENV')
app= Flask(__name__)
CORS(app, origins='*')
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = os.environ['KEY_SECRET']
app.config["JWT_SECRET_KEY"] = os.environ['KEY_PRIVATE']
app.config['JWT_TOKEN_LOCATION'] = ['headers']
jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(auth_service)
app.register_blueprint(cuento_service)
app.register_blueprint(control_service)
app.register_blueprint(usuario_service)
app.register_blueprint(pregunta_service)


with app.app_context():
    db.create_all()

if __name__=="__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=puerto)
