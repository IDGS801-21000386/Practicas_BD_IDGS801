from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
from  models import db
from forms import EmpleadoForm, CompraForm, ClienteForm
from  models import Empleados, Compras, Pedidos
from datetime import datetime
import forms 
from datetime import datetime, timedelta
from sqlalchemy import extract, func


# Crear una instancia de la clase Flask
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

app.secret_key = "1234"
pedidos_list = []
total = 0
mes = 0

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

#@app.route("/ventas_dia", methods=['GET', 'POST'])
#def ventas_dia():
#    compra_form = forms.CompraForm(request.form)

#    compra = Compras.query.all()
#    suma_total = sum(c.total_compra for c in compra)

#    return render_template("pizzeria_form.html", form = compra_form, compra=compra, suma_total=suma_total)
@app.route("/ventas_dia2", methods=['GET', 'POST'])
def ventas_dia2():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)
    
    global mes

    # Obtener el día seleccionado del formulario
    dia_seleccionado = int(request.form['dia_semana'])
    # Obtener el mes seleccionado
    mes_seleccionado = mes
    
    # Obtener todas las compras del mes seleccionado
    compra = Compras.query.filter(db.extract('month', Compras.fecha_compra) == mes_seleccionado).all()
    
    # Filtrar las compras por el día de la semana seleccionado
    compra_filtrada = [c for c in compra if c.fecha_compra.weekday() == dia_seleccionado - 1]
    
    # Calcular la suma total de las compras filtradas
    suma_total = sum(c.total_compra for c in compra_filtrada)

    # Obtener el nombre del mes seleccionado
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    mes_nombre = meses.get(mes_seleccionado, "")

    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    dia_nombre = dias_semana.get(dia_seleccionado, "")
    
    titulo_venta = f"VENTAS DEL MES DE {mes_nombre.upper()} DEL DIA {dia_nombre.upper()}"

    return render_template("pizzeria_form.html", form1=create_form1, form2=create_form2, compra=compra_filtrada, suma_total=suma_total, titulo_venta=titulo_venta)



@app.route("/ventas_mes2", methods=['GET', 'POST'])
def ventas_mes2():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)
    
    global mes

    mes_seleccionado = int(request.form['mes'])
    mes = mes_seleccionado
    compra = Compras.query.filter(db.extract('month', Compras.fecha_compra) == mes).all()
    suma_total = sum(c.total_compra for c in compra)

    meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
    }

    if mes_seleccionado in meses:
        mes_nombre = meses[mes_seleccionado]
    
    titulo_venta = f"VENTAS DEL MES DE {mes_nombre.upper()}"

    return render_template("pizzeria_form.html", form1=create_form1, form2=create_form2, compra=compra, suma_total=suma_total, titulo_venta=titulo_venta)


@app.route("/ventas_dia", methods=['GET', 'POST'])
def ventas_dia():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)
    
    hoy = datetime.now().date()
    compra = Compras.query.filter(db.cast(Compras.fecha_compra, db.Date) == hoy).all()
    suma_total = sum(c.total_compra for c in compra)

    titulo_venta = "VENTAS DEL DÍA"

    return render_template("pizzeria_form.html", form1 = create_form1, form2 = create_form2, compra=compra, suma_total=suma_total, titulo_venta=titulo_venta)

@app.route("/ventas_mes", methods=['GET', 'POST'])
def ventas_mes():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)
    
    mes_actual = datetime.now().month
    compra = Compras.query.filter(db.extract('month', Compras.fecha_compra) == mes_actual).all()
    suma_total = sum(c.total_compra for c in compra)

    titulo_venta = "VENTAS DEL MES"        
    return render_template("pizzeria_form.html", form1 = create_form1, form2 = create_form2, compra=compra, suma_total=suma_total, titulo_venta = titulo_venta)


"""
@app.route('/remover_pizza', methods=['GET', 'POST'])
def remover_pizza():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)

    global total

    total = 0;
    if request.method == "POST":
        if pedidos_list:
            pedidos_list.pop()
            for pedido in pedidos_list:
                total += pedido.sub_total

    return render_template("pizzeria_form.html", form1= create_form1, form2= create_form2, pedidos_list = pedidos_list, total = total)
"""

@app.route('/remover_pizza', methods=['POST'])
def remover_pizza():
    global total

    index = request.form.get('index')  # Usar get() para evitar KeyError
    print(index)
    if index is not None:  # Verificar si se recibió el índice
        index = int(index)
        if 0 <= index < len(pedidos_list):  # Asegurarse de que el índice sea válido
            pedidos_list.pop(index)

    total = sum(p.sub_total for p in pedidos_list)

    
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)

    return render_template("pizzeria_form.html", form1=create_form1, form2=create_form2, pedidos_list=pedidos_list, total=total)


@app.route('/pedido_form', methods=['GET', 'POST'])
def pedido_form():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)

    create_form1.id.validators = []

    global total

    if request.method == "POST" and create_form1.validate():
    # Obtener los datos del formulario
        ingre = (create_form1.champinones.data + create_form1.pina.data + create_form1.jamon.data)
        
        pedido = Pedidos(tamanio = create_form1.tamanio.data,
                    ingredientes = ingre,
                    num_pizzas = create_form1.num_pizzas.data,
                    sub_total = (int(create_form1.tamanio.data) + (int(ingre) * 10)) * int(create_form1.num_pizzas.data)
                )
        total += int(pedido.sub_total)
        pedidos_list.append(pedido)

    return render_template("pizzeria_form.html", form1 = create_form1, form2 = create_form2, pedidos_list = pedidos_list, total = total, )

@app.route("/pizzeria_form", methods=['GET', 'POST'])
def pizzeria_form():
    create_form1 = forms.PedidoForm(request.form)
    create_form2 = forms.ClienteForm(request.form)

    create_form2.id.validators = []

    global total

    if request.method == "POST" and create_form2.validate():
        compra = Compras(nombre=create_form2.nombre.data,
                        direccion=create_form2.direccion.data,
                        telefono=create_form2.telefono.data,
                        fecha_compra = create_form2.fecha_compra.data,
                        total_compra=total
                        )
        db.session.add(compra)

        for p in pedidos_list:
            tamanio = p.tamanio
            ingre = p.ingredientes
            num_pizzas = p.num_pizzas

            pedido = Pedidos(
                tamanio=tamanio,
                ingredientes=ingre,
                num_pizzas=num_pizzas,
                sub_total=(int(tamanio) + (int(ingre) * 10)) * int(num_pizzas)
            )

            pedido.compra = compra
            db.session.add(pedido)
        db.session.commit()
        pedidos_list.clear()
        total = 0

    return render_template("pizzeria_form.html", form1 = create_form1, form2 = create_form2, pedidos_list = pedidos_list, total = total)

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
