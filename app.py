# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request

import sys
sys.path.append( "src" )

from model.plan_ahorro import PlanAhorro
from model.logica_calculadora import calcular_cuota
from controller.plan_ahorro_controller import PlanAhorroController

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return render_template("crear_ahorro.html")

@app.route('/guardar_ahorro')
def guardar_ahorro():
    id_plan = request.args["id_plan"]
    nombre_meta = request.args["nombre_meta"]
    meta = float(request.args["meta"])
    tasa_interes = float(request.args["tasa_interes"])
    periodos = int(request.args["periodos"])
    abono_extra = float(request.args.get("abono_extra", 0) or 0)

    # Convertimos la tasa a decimal si se ingresó en porcentaje (ej: 1.5 -> 0.015)
    tasa_decimal = tasa_interes / 100 if tasa_interes > 1 else tasa_interes

    # Calculamos la cuota con la lógica del proyecto
    cuota = round(calcular_cuota(meta, tasa_decimal, periodos, abono_extra), 2)

    # Crear una instancia de PlanAhorro
    plan = PlanAhorro(
        id_plan=id_plan,
        nombre_meta=nombre_meta,
        meta=meta,
        tasa_interes=tasa_decimal,
        periodos=periodos,
        abono_extra=abono_extra,
        cuota_mensual=cuota
    )

    # Guardarla en la BD
    PlanAhorroController.insertar(plan)

    return f"Plan de ahorro '{nombre_meta}' insertado exitosamente con una cuota mensual de {cuota}. <br><br><a href='/'>Volver al formulario</a>"

@app.route('/crear_tablas')
def crear_tablas():
    PlanAhorroController.crear_tabla()
    return "Tablas creadas exitosamente. <br><br><a href='/'>Volver al formulario</a>"

@app.route("/buscar_ahorro")
def buscar_ahorro():
    id_buscado = request.args["id_buscado"]
    ahorro_encontrado = PlanAhorroController.buscar_por_id(id_buscado)
    return render_template("ahorro_buscado.html", ahorro=ahorro_encontrado)

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__ == '__main__':
    app.run(debug=True)
