from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField, FloatField
from flask_wtf import FlaskForm

class EmpleadoForm(Form):
    id = IntegerField("id", [
        validators.number_range(min=1, max=20, message="El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingresa un nombre válido")
    ])
    direccion = StringField("Dirección", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=5, max=100, message="Ingresa una dirección válida")
    ])
    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Regexp(r'^\d{10}$', message="Ingresa un teléfono válido")  # Verifica que tenga 10 dígitos numéricos
    ])
    correo = StringField("Correo", [
        validators.DataRequired(message="El campo es requerido")
    ])
    sueldo = IntegerField("Sueldo", [
        validators.DataRequired(message="El campo es requerido"),
    ])




