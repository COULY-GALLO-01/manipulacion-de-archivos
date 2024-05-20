import os

# Solicitar al usuario que inserte un número
num = int(input("Inserte un número entre 1 y 10: "))

# Generar la lista de multiplicación
multiplicacion = [1*num, 2*num, 3*num, 4*num, 5*num, 6*num, 7*num, 8*num, 9*num, 10*num]

def multip():
    nombre_archivo = "tabla-n.txt"
    
    try:
        # Verificar si el archivo existe
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                print("si existe")
               
        else:
            print("El archivo no existe.")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")

# Llamar a la función para leer el archivo
multip()
