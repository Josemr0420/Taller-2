##By Jose Miguel Muñoz Ríos##

from flask import Flask, jsonify, render_template
import random
import socket

app = Flask(__name__)

pokeneas = [
    {"id": 1, "nombre": "Bulbasaur", "altura": "0.7m", "habilidad": "Espesura", "imagen": "pokenea1.jpg", "frase": "Ay gono Mario niño"},
    {"id": 2, "nombre": "Ivysaur", "altura": "1.0m", "habilidad": "Espesura", "imagen": "pokenea2.jpg", "frase": "Uy pa me va a decir la hora"},
    {"id": 3, "nombre": "Venusaur", "altura": "2.0m", "habilidad": "Espesura", "imagen": "pokenea3.jpg", "frase": "Ay coco como estás de cambiado"},
    {"id": 4, "nombre": "Charmander", "altura": "0.6m", "habilidad": "Mar Llamas", "imagen": "pokenea4.jpg", "frase": "Ah no sé pai porque tuki tuki muñeco"},
    {"id": 5, "nombre": "Charmeleon", "altura": "1.1m", "habilidad": "Mar Llamas", "imagen": "pokenea5.jpg", "frase": "Uy ñero"},
    {"id": 6, "nombre": "Charizard", "altura": "1.7m", "habilidad": "Mar Llamas", "imagen": "pokenea6.jpg", "frase": "Solo verdolaga a morir"},
    {"id": 7, "nombre": "Squirtle", "altura": "0.5m", "habilidad": "Torrente", "imagen": "pokenea7.jpg", "frase": "Nos pegamos los polnes o qué pa?"},
    {"id": 8, "nombre": "Wartortle", "altura": "1.0m", "habilidad": "Torrente", "imagen": "pokenea8.jpg", "frase": "Sea serio niño"},
    {"id": 9, "nombre": "Blastoise", "altura": "1.6m", "habilidad": "Torrente", "imagen": "pokenea9.jpg", "frase": "Uy pa llegaron los aguacates pa"},
    {"id": 10, "nombre": "Caterpie", "altura": "0.3m", "habilidad": "Polvo Escudo", "imagen": "pokenea10.jpg", "frase": "Maneje los tiempos pai"}
]

@app.route('/pokeneas', methods=['GET'])
def showPokenea():
    # Obtener el id del contenedor
    contenedor_id = socket.gethostname()

    #Obtener pokenea aleatorio
    pokenea = random.choice(pokeneas)

    # URL pública del bucket de GCP y obtener URL de la imagen
    bucket_name = 'pokemon_images_bucket'
    image_url = f"https://storage.googleapis.com/{bucket_name}/images/{pokenea['imagen']}"

    return render_template('pokenea.html', nombre=pokenea["nombre"], imagen=image_url, frase=pokenea["frase"], contenedor_id=contenedor_id)

@app.route('/pokeneas/json', methods=['GET'])
def showPokeneaJson():
    # Obtener el id del contenedor
    contenedor_id = socket.gethostname()

    # Obtener pokenea aleatorio
    pokenea = random.choice(pokeneas)

    # Generar respuesta JSON
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
