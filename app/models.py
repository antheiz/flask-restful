from app import db, ma, api
from flask import request
from flask_restful import Resource

class Provinsi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_provinsi = db.Column(db.String(100), nullable=False)
    kabupaten = db.relationship('Kabupaten', backref='kabupaten', lazy=True)

    def __repr__(self):
        return f"{self.nama_provinsi}"

class Kabupaten(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_kabupaten = db.Column(db.String(100), nullable=False)
    provinsi = db.Column(db.String(100), db.ForeignKey('provinsi.id'), nullable=False)
    distrik_id = db.relationship('Distrik', backref='distrik', lazy=True)

    def __repr__(self):
        return (f"Distrik('{self.nama_kabupaten}')")

class Distrik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_distrik = db.Column(db.String(100), nullable=False)
    kabupaten = db.Column(db.String(100), db.ForeignKey('kabupaten.id'), nullable=False)
    kampung = db.relationship('Kampung', backref='kampung', lazy=True)

    def __repr__(self):
        return (f"Kampung({self.nama_distrik}')")

class Kampung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_kampung = db.Column(db.String(100), nullable=False)
    distrik = db.Column(db.Integer, db.ForeignKey('distrik.id'), nullable=False)
    
    def __repr__(self):
        return (f"Kampung({self.nama_distrik}')")

class ProvinsiSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_provinsi')
    
class KabupatenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_kabupaten', 'provinsi')

class DistrikSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_distrik', 'kabupaten')
    
class KampungSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_kampung', 'distrik')

#  Schema Provinsi
provinsi_schema = ProvinsiSchema()
provinsis_schema = ProvinsiSchema(many=True)

# Schema Kabupaten
kabupaten_schema = KabupatenSchema()
kabupatens_schema = KabupatenSchema(many=True)


#  Schema Distrik
distrik_schema = DistrikSchema()
distriks_schema = DistrikSchema(many=True)

# Schema Kampung
kampung_schema = KampungSchema()
kampungs_schema = KampungSchema(many=True)


# PROVINSI
class ProvinsiResource(Resource):
    def get(self):
        return provinsis_schema.dump(Provinsi.query.all())     

    def post(self):
        data = request.json
        new_provinsi = Provinsi(nama_provinsi=data['nama_provinsi'])   
        db.session.add(new_provinsi)
        db.session.commit()
        return provinsi_schema.dump(new_provinsi)

class KabupatenResource(Resource):
    def get(self):
        return kabupatens_schema.dump(Kabupaten.query.all())    
    
    def post(self):
        data = request.json
        print(data['provinsi'])
        data_provinsi = Provinsi.query.get(data['provinsi'])
        print(data_provinsi.id)
        new_kabupaten = Kabupaten(nama_kabupaten=data['nama_kabupaten'], provinsi=data_provinsi.nama_provinsi)
        db.session.add(new_kabupaten)
        db.session.commit()
        # return kampung_schema.dump(new_kabupaten)
        return kabupaten_schema.dump(new_kabupaten)

class DistrikResource(Resource):
    def get(self):
        return distriks_schema.dump(Distrik.query.all())    
    
    def post(self):
        data = request.json
        data_kabupaten = Kabupaten.query.filter_by(id=data['kabupaten']).first()
        new_distrik = Distrik(nama_distrik=data['nama_distrik'], distrik=data_kabupaten)
        db.session.add(new_distrik)
        db.session.commit()
        return distrik_schema.dump(new_distrik)

class KampungResource(Resource):
    def get(self):
        return kampungs_schema.dump(Kampung.query.all())    
    
    def post(self):
        data = request.json
        data_distrik = Distrik.query.filter_by(id=data['distrik_id']).first()
        new_kampung = Kampung(nama_kampung=data['nama_kampung'], distrik=data_distrik)
        db.session.add(new_kampung)
        db.session.commit()
        return kampung_schema.dump(new_kampung)