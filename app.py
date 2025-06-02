from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy #objeto de la clase SQLAlchemy
from datetime import datetime
import os
from models.models import db,Radionovela , Visitas # Importar el objeto db desde models.models

app= Flask(__name__)

#--------
# Configuración de la base de datos
basedir= os.path.abspath(os.path.dirname(__file__   ))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "baseDatos", "radionovelas.db")}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # para que no se guarde en la base de datos

db.init_app(app)

with app.app_context():# Crear el contexto de la aplicación para poder usar db
    db.create_all() 
#------------------------------------

@app.route('/')
def index():
    capitulos_obj= Radionovela.query.order_by(Radionovela.id.asc()).all()# Obtener todos los capitulos de la base de datos
    capitulos=[cap.to_dict() for cap in capitulos_obj] # Convertir a lista de diccionarios

    #registrar visitas
    nueva_visita=Visitas() # Crear una nueva visita(Visitas es un modelo de la base de datos)
    db.session.add(nueva_visita) # Agregar la nueva visita a la sesión
    db.session.commit() # Guardar la sesión

    total_visitas=Visitas.query.count() # Contar el total de visitas

    return render_template('index.html', capitulos=capitulos,total_visitas=total_visitas) # Renderizar el template index.html y pasarle los capitulos




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    