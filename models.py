from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
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

"""
class Compras(db.Model):
    __tablename__ = "Compras"
    id = db.Column(db.Integer, primary_key = True) 
    nombre = db.Column(db.String(50)) 
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    fecha_compra = db.Column(db.DateTime, default = datetime.datetime.now)


class Pedidos(db.Model):
    __tablename__ = "Pedidos"
    id = db.Column(db.Integer, primary_key = True) 
    tamanio = db.Column(db.String(50)) 
    ingredientes = db.Column(db.Integer)
    num_pizzas = db.Column(db.Integer)
    sub_total = db.Column(db.Double)

"""

class Compras(db.Model):
    __tablename__ = "Compras"
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(50)) 
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    fecha_compra = db.Column(db.DateTime, default=datetime.datetime.now)
    total_compra = db.Column(db.Integer)
    pedidos = relationship("Pedidos", back_populates="compra")

class Pedidos(db.Model):
    __tablename__ = "Pedidos"
    id = db.Column(db.Integer, primary_key=True) 
    tamanio = db.Column(db.String(50)) 
    ingredientes = db.Column(db.Integer)
    num_pizzas = db.Column(db.Integer)
    sub_total = db.Column(db.Float)
    compra_id = db.Column(db.Integer, ForeignKey('Compras.id'))
    compra = relationship("Compras", back_populates="pedidos")
