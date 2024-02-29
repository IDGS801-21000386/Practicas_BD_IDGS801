from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

from flask import g
from config import DevelopmentConfig
from  models import db
from forms import EmpleadoForm
from  models import Empleados
import forms 

# Crear una instancia de la clase Flask
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

app.secret_key = "1234"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/ABC_Empleado", methods=['GET', 'POST'])
def ABC_Empleado():
    emp_form = forms.EmpleadoForm(request.form)
    empleado = Empleados.query.all()
    return render_template("empleados_vista.html", empleado = empleado)

@app.route("/registrar_empleado", methods=['GET', 'POST'])
def registrar_empleado():
    create_form = forms.EmpleadoForm(request.form)
    create_form.id.validators = []
    
    if request.method == "POST" and create_form.validate():
        emp = Empleados(nombre = create_form.nombre.data,
                        direccion = create_form.direccion.data,
                        telefono = create_form.telefono.data,
                        correo = create_form.correo.data,
                        sueldo = create_form.sueldo.data
                    )
        db.session.add(emp)
        db.session.commit()
    return render_template("empleados_form.html", form = create_form)

    
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()
