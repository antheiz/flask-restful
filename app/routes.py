from app import app, db, api
from flask import jsonify, request, render_template
from flask_restful import Resource
from .models import (Provinsi, Kabupaten, Distrik, Kampung, 
                ProvinsiResource, KabupatenResource, DistrikResource, KampungResource)



# ENDPOINT API
api.add_resource(ProvinsiResource, '/api/provinsi') # Provinsi
api.add_resource(KabupatenResource, '/api/kabupaten') # Kabupaten
api.add_resource(DistrikResource, '/api/distrik') # Distrik
api.add_resource(KampungResource, '/api/kampung') # Kampung