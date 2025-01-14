#Usaremos flask
'''
Primero tendremos que tener un estado el cual nos diga, que los cursos ya han sido guardados.
Pero eso se hara manualmente, ya que el web scraping solo sirve de forma local
Lo que se subira seran los cursos ya filtrados y eso.
Al tener los cursos, manualmente se agregara un file que tenga solo el comando, agregados, que retorne un 200, y si no hay 400
'''

from flask import Flask, jsonify, request
from flask_cors import CORS
from generador import get_available_courses as get_ac
from generador import get_total_credits as get_tc
from generador import get_course_details

app = Flask(__name__)
CORS(app)

@app.route('/horario', methods=['POST'])
def horarios():
    dato = request.get_json()
    available_courses = None
    for curs, valor in dato.items():
        available_courses = valor
    
    # Obtener las clases filtradas
    clases = get_course_details(available_courses)

    # Organizar las clases por días y horas
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    horario = {dia: {} for dia in dias_semana}

    for codigo, detalles in clases.items():
        for clase in detalles:
            dias = clase["Dias"]
            inicio = clase["Inicio"]
            final = clase["Final"]
            nombre_curso = clase["Nombre de Curso"]
            seccion = clase["Seccion"]
            catedratico = clase.get("Catedratico", "")
            star = clase.get("Star", "")
            modalidad = clase.get("Modalidad", "")
            edificio = clase.get("Edificio", "")
            salon = clase.get("Salon", "")
            aux = clase.get("Aux", "")
            restricciones = clase.get("Restricciones", "")

            for idx, dia in enumerate(dias):
                if dia == "X":
                    if inicio not in horario[dias_semana[idx]]:
                        horario[dias_semana[idx]][inicio] = []

                    horario[dias_semana[idx]][inicio].append({
                        "curso": nombre_curso,
                        "seccion": seccion,
                        "inicio": inicio,
                        "final": final,
                        "catedratico": catedratico,
                        "star": star,
                        "modalidad": modalidad,
                        "edificio": edificio,
                        "salon": salon,
                        "aux": aux,
                        "restricciones": restricciones
                    })

    return jsonify(horario)
    

if __name__ == '__main__':
    app.run(debug=True)