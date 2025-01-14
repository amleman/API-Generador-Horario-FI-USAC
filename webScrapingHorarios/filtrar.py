from datos import Cursos
import pandas as pd
def buscar_seminario_en_cola(cursos):
    #aqui tengo que desencolar los cursos la cola 1 y luego encolarlos en la cola 2, pero eliminando los seminarios.
    cursos_sin_seminarios = Cursos()
    while not cursos.esta_vacia():
        curso = cursos.desencolar()
        if "seminario" in curso[0].lower():
            #solo debe de pasar
            pass
        else:
            cursos_sin_seminarios.encolar(curso)
    restricciones(cursos_sin_seminarios, cursos)

def restricciones(cursos_sin_seminarios, cursos):
    # si un curso tiene "ver restricciones" es porque debe tener una seccion con + o -, estos son para par e impar respectivamente
    print("---------------------------------------------------------------------")
    while not cursos_sin_seminarios.esta_vacia():
        curso = cursos_sin_seminarios.desencolar()
        if "ver restricciones" in curso[11].lower():
            if curso[2].endswith('-'):
                curso[11] = "Solo Carnet de terminacion impar (1,3,5,7,9)"
            elif curso[2].endswith('+'):
                curso[11] = "Solo Carnet de terminacion par (0,2,4,6,8)"
            else:
                curso[11] = "Revisar en la pagina principal"
        cursos.encolar(curso)
    print("filtrados")
