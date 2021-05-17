from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_restful import Api, Resource
from flask_cors import CORS 

# INITIALISE
app = Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# INIT SQlALCHEMY DB
db = SQLAlchemy(app)

# INIT MARSHMALLOW
ma = Marshmallow(app)

# INIT API
api = Api(app)

# INIT CORS
cors = CORS(app, resources=r'/api/*')

from app import routes