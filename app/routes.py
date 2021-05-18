from app import app, db, api
from flask import jsonify, request, render_template
from flask_restful import Resource
from .models import (Provinsi, Kabupaten, Distrik, Kampung, 
                ProvinsiResource, KabupatenResource, DistrikResource, DistriksResource, 
                KampungResource)

@app.route('/')
def index():    
    return render_template('index.html', judul='Beranda')

@app.route('/provinsi')
def provinsi():    
    data = Provinsi.query.all()
    return render_template('template.html',judul='Provinsi', data=data)

@app.route('/kabupaten')
def kabupaten():    
    data = Kabupaten.query.all()
    return render_template('template.html',judul='Kabupaten', data=data)

@app.route('/distrik')
def distrik():    
    data = Distrik.query.all()
    return render_template('template.html',judul='Distrik', data=data)

@app.route('/kampung')
def kampung():    
    data = Kampung.query.all()
    return render_template('template.html',judul='Kampung', data=data)

@app.route('/api')
def restful():        
    return render_template('api.html', judul='Dokumentasi')

# ENDPOINT API
api.add_resource(ProvinsiResource, '/api/provinsi') # Provinsi
api.add_resource(KabupatenResource, '/api/kabupaten') # Kabupaten
api.add_resource(DistrikResource, '/api/distrik') # Distrik
api.add_resource(DistriksResource, '/api/distrik/<int:pk>') # Distrik
api.add_resource(KampungResource, '/api/kampung') # Kampung