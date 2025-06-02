import os
from app import app
from models.models import db, Radionovela

# Ruta a la carpeta de los audios
audios_dir = os.path.join(app.root_path, "static", "audios", "novelas")

def extraer_info(nombre_archivo):
    # Ejemplo: 01Kaliman los Profanadores de Tumbas capítulo 1.mp3
    base = nombre_archivo.rsplit('.', 1)[0]  # sin la extensión
    numero_str = ''.join(filter(str.isdigit, base[:2]))  # extrae el número inicial
    numero = int(numero_str) if numero_str else None

    titulo = base[2:]  # quita los primeros 2 caracteres (número)
    return numero, titulo.strip(), nombre_archivo

with app.app_context():
    archivos = [f for f in os.listdir(audios_dir) if f.endswith('.mp3')]
    nuevos = 0

    for archivo in archivos:
        numero, titulo, nombre_archivo = extraer_info(archivo)

        # Verifica si ya existe en la base de datos
        existente = Radionovela.query.filter_by(archivo=nombre_archivo).first()
        if not existente:
            cap = Radionovela(
                title=titulo,
                archivo=nombre_archivo,
                description=f"Capítulo {numero} de Kaliman",
                serie="Kalimán",
                )
            db.session.add(cap)
            nuevos += 1

    db.session.commit()
    print(f"✅ {nuevos} capítulos agregados.")
