from flask import Flask
from flask_jwt_extended import JWTManager 
from utils.db import db
from flask_cors import CORS
import os
from config import DATABASE_CONNECTION

from services.cliente import cliente

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

app.register_blueprint(cliente)


with app.app_context():
    db.create_all()

if __name__=="__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=puerto)
