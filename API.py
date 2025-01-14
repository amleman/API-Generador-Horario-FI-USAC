from flask import Flask, jsonify, request
import os
import json
from flask_cors import CORS
from generador import get_available_courses as get_ac
from generador import get_total_credits as get_tc
from generador import get_course_details

#Usaremos flask
'''
Primero tendremos que tener un estado el cual nos diga, que los cursos ya han sido guardados.
Pero eso se hara manualmente, ya que el web scraping solo sirve de forma local
Lo que se subira seran los cursos ya filtrados y eso.
Al tener los cursos, manualmente se agregara un file que tenga solo el comando, agregados, que retorne un 200, y si no hay 400
'''


app = Flask(__name__)
CORS(app, resources={r"/horario/*": {"origins": "https://genera-tu-horario-fiusac.netlify.app"}})

def confirmacion():
    ruta_confirmacion = os.path.join(os.path.dirname(__file__), 'datos', 'confirmacion.json')
    
    #abro
    with open(ruta_confirmacion, 'r', encoding='utf-8') as f:
        confirm = json.load(f)
    
    return confirm


def get_data(pensum):    
    #abro
    with open(pensum, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    second_key = list(data.keys())[1]
    prerequisitos = data[second_key]
    third_key = list(data.keys())[2]
    creditos = data[third_key]
        
    return prerequisitos, creditos

@app.route('/horario', methods=['POST'])
def horarios():
    try:
        data = request.get_json()
        if not data or 'cursos_disponibles' not in data:
            return jsonify({"message": "Se requiere el campo 'cursos_disponibles' en el cuerpo de la solicitud."}), 400

        available_courses = data['cursos_disponibles']
        print(available_courses)
        
        if not isinstance(available_courses, list):
            return jsonify({"message": "El campo 'cursos_disponibles' debe ser una lista."}), 400
        
        if not all(isinstance(curso, str) for curso in available_courses):
            return jsonify({"message": "Los elementos en 'cursos_disponibles' deben ser strings."}), 400

        # Obtener las clases filtradas
        clases = get_course_details(available_courses)

        # Si no se encuentran clases para los cursos proporcionados
        if not clases:
            return jsonify({"message": "No se encontraron clases para los cursos proporcionados."}), 404

        # Organizar las clases por días y horas
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        horario = {dia: {} for dia in dias_semana}

        for codigo, detalles in clases.items():
            for clase in detalles:
                for idx, dia in enumerate(clase["Dias"]):
                    if dia == "X":
                        inicio = clase["Inicio"]
                        if inicio not in horario[dias_semana[idx]]:
                            horario[dias_semana[idx]][inicio] = []

                        horario[dias_semana[idx]][inicio].append({
                            "curso": clase["Nombre de Curso"],
                            "seccion": clase["Seccion"],
                            "inicio": inicio,
                            "final": clase["Final"],
                            "catedratico": clase.get("Catedratico", ""),
                            "star": clase.get("Star", ""),
                            "modalidad": clase.get("Modalidad", ""),
                            "edificio": clase.get("Edificio", ""),
                            "salon": clase.get("Salon", ""),
                            "aux": clase.get("Aux", ""),
                            "restricciones": clase.get("Restricciones", "")
                        })

        return jsonify(horario), 200

    except Exception as e:
        print(f"Error interno del servidor: {e}") # Imprimir el error para debugging
        return jsonify({"message": "Error interno del servidor."}), 500
    

@app.route('/cursosganados', methods=["POST"])
def ganados():
    datos = request.get_json()
    
    carrera = None
    cursos = None
    
    for clave, valor in datos.items():
        if clave == "cursos":
            cursos = valor
        else:
            carrera = valor

    ready = confirmacion()
    ready_all = ready['confirmacion']
    
    if ready_all != "200":
        #Horarios no publicados/ No data
        return "400"
        pass
    else:
        #aqui tengo que primero saber que carrera es para saber los pre y post requisitos
        match carrera:
            case "Sistemas":
                pensum_sistemas = os.path.join(os.path.dirname(__file__), 'listasAdyacencia', 'sistemas.json')
                prerequisitos, creditos = get_data(pensum_sistemas)
                total_credits = get_tc(cursos, creditos)
                available_courses = get_ac(cursos, prerequisitos, total_credits)

                return jsonify({'cursos_disponibles': list(available_courses)})
            case "Industrial":
                pass
            case None:
                return "400"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)