No es necesario el uso de un ordenamiento topologico para esto, ya que no tengo que hacer un roadmap de la carrera.
Solo debo de obtener los cursos posibles para el siguiente semestre. Esto lo hago usando los pre-requisitos.

Ya se pudo devolver los cursos posibles en base a los pre-requisitos.
Tener en cuenta que no estan los creditos, y esto puede afectar, para
aquellos cursos que tengan creditos como prerequisito.

Lo que hay que hacer es agregar los creditos, a todos los cursos.
Pensar como...

creditos agregados y ya regresa los cursos disponibles tomando en cuenta
los creditos.

Ahora con los cursos disponibles tengo que buscar los distintas secciones y horarios
Al tener todos los horarios, tendre que hacer comparaciones para no tener traslapes
Y seleccionar solo una seccion por curso.

He obtnido los cursos y sus clases correspondientes, junto con todos los datos
como seccion, si es lab o no.

Ahora que tengo todos estos datos es hora de filtrarlos, hacer los horarios del lado
del servidor para que solo envie un json con las distintas formas de creacion del
horario asi del lado del cliente solo mostrarlos en tablas y asi.

Que datos me son necesarios?
dias, inicio, final, seccion

Luego de ello ya se puede comenzar con la creacion del horario en el frontend.

GPT encontro una forma de ordenar los cursos en un grid de dias y horas como un horario
ahora estos se enviaran al frontend para que la aplicacion muestre todos las clases en un mismo
grid, asi el usuario pueda ver todas las opciones disponibles y el pueda seleccionar y disenar
su horario a la medida, mostrando los detalles de cada clase en un pop-up u otra manera.


{
    "Lunes": {
        "07:00": [
            {"curso": "0150 FISICA 1", "seccion": "A+", "inicio": "07:00", "final": "08:00"},
            {"curso": "0107 AREA MATEMATICA", "seccion": "A", "inicio": "07:00", "final": "08:50"}
        ],
        ...
    },
    "Martes": {
        ...
    },
    ...
}

