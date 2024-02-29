from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Empleados(db.Model):
    __tablename__ = "Empleados"
    id = db.Column(db.Integer, primary_key = True) 
    nombre = db.Column(db.String(50)) 
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(50))
    sueldo = db.Column(db.Integer)

