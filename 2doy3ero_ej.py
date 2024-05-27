import os

# Solicitar al usuario que inserte un número
num = int(input("Inserte un número entre 1 y 10: "))

# Generar la lista de multiplicación
multiplicacion = [1*num, 2*num, 3*num, 4*num, 5*num, 6*num, 7*num, 8*num, 9*num, 10*num]

def multip():
    nombre_archivo = "tabla-n.txt"
    
    try:
        # Verificar si el archivo existe
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()
            
            for numero in multiplicacion:
                encontrado = False
                for linea in contenido:
                    if str(numero) in linea:
                        encontrado = True
                        break
                
                if encontrado:
                    print(f"{numero} existe en el archivo.")
                else:
                    print(f"{numero} no existe en el archivo.")
    except IOError:
        print(f"No se pudo abrir el archivo '{nombre_archivo}'.")

# Llamar a la función para leer el archivo
multip()
