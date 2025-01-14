from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

import time
from datos import Cursos
from filtrar import buscar_seminario_en_cola as filtro
from categorizar import categorizar1

def obtenerCursos(driver, cursos):
    cursos_odd = []
    cursos_even = []
    cursos_y_propiedades1 = driver.find_elements(By.CLASS_NAME, "odd")
    cursos_y_propiedades2 = driver.find_elements(By.CLASS_NAME, "even")
    #al parecer hay dos clases de linea, odd y even
    for curso_y_prop in cursos_y_propiedades1:
        propiedades_curso = curso_y_prop.find_elements(By.TAG_NAME, "td")
        contador = 0
        curso = []
        dias_curso = []
        for td in propiedades_curso:
            contador = contador + 1
            if contador == 1:
                curso.append(td.text)
                #Ahora tengo que saber si es lab o no. buscando en el td 1 la clase fa-star, si existe es lab
                # hay 4 estrellas, lab (class badge-blue), dibujo (badge-success), practica (badge-danger), trabajo dirigido (badge-info)
                try:
                    star_blue = None
                    star_success = None
                    star_danger = None
                    star_info = None
                    # Intenta encontrar el elemento con la clase "badge"
                    try:
                        star_blue = td.find_element(By.CLASS_NAME, "badge-blue")
                    except NoSuchElementException:
                        pass
                    try:
                        star_success = td.find_element(By.CLASS_NAME, "badge-success")
                    except NoSuchElementException:
                        pass
                    try:
                        star_danger = td.find_element(By.CLASS_NAME, "badge-danger")
                    except NoSuchElementException:
                        pass
                    try:
                        star_info = td.find_element(By.CLASS_NAME, "badge-info")
                    except NoSuchElementException:
                        pass
                    
                    # Verificar cuál clase específica tiene el elemento
                    if star_blue != None:
                        curso.append('laboratorio')
                    elif star_success != None:
                        curso.append('dibujo')
                    elif star_danger != None:
                        curso.append('practica')
                    elif star_info != None:
                        curso.append('trabajo dirigido')
                    else:
                        curso.append("Clase normal")
                except NoSuchElementException:
                    # Si no se encuentra el elemento, lo pone como normal
                    print('error en las estrellas')
                    curso.append("Clase normal")
            elif contador == 8:
                pass
            elif contador == 9 or contador == 10 or contador == 11 or contador == 12 or contador == 13 or contador == 14 or contador == 15:
                # ya estamos dentro de la tabla de los dias
                if td.text == "X":
                    dias_curso.append(td.text)
                else:
                    dias_curso.append(None)
            else:  
                curso.append(td.text)
            if contador == 15:
                curso.append(dias_curso)
        cursos_odd.append(curso)
    #los impares son odd
    for curso_y_prop in cursos_y_propiedades2:
        propiedades_curso = curso_y_prop.find_elements(By.TAG_NAME, "td")
        contador = 0
        curso = []
        dias_curso = []
        for td in propiedades_curso:
            contador = contador + 1
            if contador == 1:
                curso.append(td.text)
                try:
                    star_blue = None
                    star_success = None
                    star_danger = None
                    star_info = None
                    # Intenta encontrar el elemento con la clase "badge"
                    try:
                        star_blue = td.find_element(By.CLASS_NAME, "badge-blue")
                    except NoSuchElementException:
                        pass
                    try:
                        star_success = td.find_element(By.CLASS_NAME, "badge-success")
                    except NoSuchElementException:
                        pass
                    try:
                        star_danger = td.find_element(By.CLASS_NAME, "badge-danger")
                    except NoSuchElementException:
                        pass
                    try:
                        star_info = td.find_element(By.CLASS_NAME, "badge-info")
                    except NoSuchElementException:
                        pass
                    
                    # Verificar cuál clase específica tiene el elemento
                    if star_blue != None:
                        curso.append('laboratorio')
                    elif star_success != None:
                        curso.append('dibujo')
                    elif star_danger != None:
                        curso.append('practica')
                    elif star_info != None:
                        curso.append('trabajo dirigido')
                    else:
                        curso.append("Clase normal")
                except NoSuchElementException:
                    # Si no se encuentra el elemento, lo pone como normal
                    print('error en las estrellas')
                    curso.append("Clase normal")
            elif contador == 8:
                pass
            elif contador == 9 or contador == 10 or contador == 11 or contador == 12 or contador == 13 or contador == 14 or contador == 15:
                if td.text == "X":
                    dias_curso.append(td.text)
                else:
                    dias_curso.append(None)
            else:
                curso.append(td.text)
            if contador == 15:
                curso.append(dias_curso)
        cursos_even.append(curso)
    combinar_arreglos(cursos_odd, cursos_even, cursos)
    
def combinar_arreglos(arreglo1, arreglo2, cursos):
    size_arreglo1 = len(arreglo1)
    for i in range(size_arreglo1):
        cursos.encolar(arreglo1[i])
        if i < len(arreglo2):
            cursos.encolar(arreglo2[i])
    print('added')

def navegacion(driver, cursos):
    obtenerCursos(driver, cursos)
    #obtengo el numero total de paginas
    total_pages_element = driver.find_element(By.XPATH, '//*[@id="tblHorarios_paginate"]/ul/li[8]')
    total_pages_num = int(total_pages_element.text)
    contador = 2
    while contador <= total_pages_num:
        #obtengo el boton de siguiente pagina.
        siguiente_page = driver.find_element(By.ID, "tblHorarios_next")
        siguiente_page.click()
        obtenerCursos(driver, cursos)
        contador = contador + 1

def main():
    titulos = []
    cursos = Cursos()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get("https://usuarios.ingenieria.usac.edu.gt/horarios/semestre/1")
    assert "Horarios" in driver.title

    #espero a que la pagina cargue    
    WebDriverWait(driver, 2800).until(
        lambda driver: driver.find_element(By.TAG_NAME, "table"))
    #ahora busco los elementos necesarios
    thNombreCurso = driver.find_element(By.CLASS_NAME, "sorting_asc")
    theaders = driver.find_elements(By.CLASS_NAME, "sorting")
    #obtengo los textos de los elementos encontrados y los almaceno en una lista.
    nombre_curso = thNombreCurso.text
    titulos.append(nombre_curso)
    for th in theaders:
        titulos.append(th.text)
    #----------------------------------------------------------------
    
    #Para esto hay que hacer un script que pase a la siguiente pagina.
    navegacion(driver, cursos)
    time.sleep(8)
    driver.quit()
    #guardo los datos en un excel
    #cursos.guardar_en_excel('cursos.xlsx')
    #ahora tengo que clasificar los datos en diferentes archivos json, para distribuir la cantidad de datos.
    filtro(cursos)
    categorizar1(cursos)
    return "Updated"

def prueba():
    return "exitoso"

if __name__ == "__main__":
    main()