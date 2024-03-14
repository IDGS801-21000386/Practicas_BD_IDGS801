from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField, FloatField, RadioField, BooleanField, DateField
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

class CompraForm(Form):
    id = IntegerField("id", [
        validators.number_range(min=1, max=20, message="El campo es requerido")
    ])

    tamanio = RadioField("Tamaño Pizza", choices=[(40, "Chica $40"), (80, "Mediana $80"), (120, "Grande $120")])
    
    jamon = BooleanField("Jamón $10", default=1)
    pina = BooleanField("Piña $10", default=1)
    champinones = BooleanField("Champiñones $10", default=1)

    num_pizzas = StringField("Num. de Pizzas", [
        validators.DataRequired(message="El campo es requerido")
    ])    

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingresa un nombre válido")
    ])
    direccion = StringField("Direccion", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingresa un nombre válido")
    ])
    telefono = TelField("Telefono", [
        validators.DataRequired(message="El campo es requerido")
    ])
    

class PedidoForm(Form):
    id = IntegerField("id", [
        validators.number_range(min=1, max=20, message="El campo es requerido")
    ])

    tamanio = RadioField("Tamaño Pizza", choices=[(40, "Chica $40"), (80, "Mediana $80"), (120, "Grande $120")])
    
    jamon = BooleanField("Jamón $10", default=1)
    pina = BooleanField("Piña $10", default=1)
    champinones = BooleanField("Champiñones $10", default=1)

    num_pizzas = StringField("Num. de Pizzas", [
        validators.DataRequired(message="El campo es requerido")
    ])    

class ClienteForm(Form):
    id = IntegerField("id", [
        validators.number_range(min=1, max=20, message="El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingresa un nombre válido")
    ])
    direccion = StringField("Direccion", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=50, message="Ingresa un nombre válido")
    ])
    telefono = StringField("Telefono", validators=[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=10, max=15, message="La longitud del teléfono debe estar entre 10 y 15 caracteres")
    ])
    fecha_compra = DateField("Fecha de la compra", [
        validators.DataRequired(message="El campo es requerido")
    ])