import pandas as pd

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cursos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if not self.esta_vacia():
            valor = self.primero.valor
            self.primero = self.primero.siguiente
            return valor
        else:
            raise IndexError("La cola está vacía")

    def size(self):
        contador = 0
        actual = self.primero
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def mostrar(self):
        if self.esta_vacia():
            return "Vacia"
        else:
            actual = self.primero
            while actual:
                print(actual.valor)
                actual = actual.siguiente
            return "done"
    
    # Método para guardar los datos en Excel
    def guardar_en_excel(self, archivo_excel):
        # Definir las columnas
        #star es para las
        columnas = ['Nombre de Curso', 'Star', 'Seccion', 'Modalidad', 'Edificio', 'Salon', 
                    'Inicio', 'Final', 'Dias', 'Catedratico', 'Aux', 'Restricciones']
        
        # Lista para almacenar los datos de cada nodo
        datos = []
        
        # Recorrer la cola y extraer los valores
        actual = self.primero
        while actual:
            datos.append(actual.valor)  # Cada nodo tiene un arreglo de 11 elementos
            actual = actual.siguiente
        
        # Crear el DataFrame con los datos
        df = pd.DataFrame(datos, columns=columnas)
        
        # Guardar el DataFrame en un archivo Excel
        df.to_excel(archivo_excel, index=False)